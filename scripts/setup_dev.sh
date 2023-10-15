docker compose up -d

echo "Waiting container start-up"
sleep 10

docker exec doodle_backend /usr/bin/env python -m pip install .[dev]
