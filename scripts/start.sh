set -e

cd /opt/doodle


exec gunicorn -w 2 'doodle.main:app_factory'
