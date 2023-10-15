FROM python:3.11-bookworm

LABEL maintainer="Arthur Harduim"

ARG SERVICE_UID=1000
ARG SERVICE_GID=1000

ENV SERVICE_NAME=doodle
ENV SERVICE_BASE_PATH=/opt
ENV SERVICE_PATH=$SERVICE_BASE_PATH/$SERVICE_NAME

RUN apt update \
    && apt install -y --no-install-recommends  git tini tzdata \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN addgroup --gid "${SERVICE_GID}" "${SERVICE_NAME}"
RUN adduser --quiet "${SERVICE_NAME}" --uid "${SERVICE_UID}" --gid "${SERVICE_GID}"
RUN mkdir "${SERVICE_PATH}"
RUN mkdir /var/log/"${SERVICE_NAME}"/
RUN mkdir "${SERVICE_PATH}"/reports
RUN mkdir "${SERVICE_PATH}"/static
RUN chown -R "${SERVICE_NAME}":"${SERVICE_NAME}" "${SERVICE_PATH}"

USER "${SERVICE_NAME}"
ENV TZ="America/Sao_Paulo"

WORKDIR "${SERVICE_PATH}"
ADD pyproject.toml .
ADD README.md .
ADD doodle "${SERVICE_PATH}"/doodle

RUN export PATH="/home/${SERVICE_NAME}/.local/bin:$PATH"
RUN echo 'export PATH="/home/${SERVICE_NAME}/.local/bin:$PATH"' >> /home/"${SERVICE_NAME}"/.bashrc
RUN pip install --no-warn-script-location --no-cache-dir -e .

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["sleep", "infinity"]
EXPOSE 3001
