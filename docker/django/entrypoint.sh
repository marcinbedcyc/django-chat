#!/bin/sh

set -o errexit  # same as set -e
# set -o pipefail does not work :/
set -o nounset  # same as set -u

postgres_ready() {
python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
        port="${POSTGRES_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}


redis_ready() {
python << END
import sys
import redis
connection = redis.Redis(
    host="${REDIS_URL}",
    port="${REDIS_PORT}",
    db="${REDIS_DB}",
)
try:
    connection.ping()
except Exception:
    sys.exit(-1)
sys.exit(0)
END
}

wait_db(){
    until postgres_ready; do
        >&2 echo 'Waiting for PostgreSQL to become available...'
        sleep 1
    done
    >&2 echo 'PostgreSQL is available'
}

wait_redis(){
    until redis_ready; do
        >&2 echo 'Waiting for Redis to become available...'
        sleep 1
    done
    >&2 echo 'Redis is available'
}

case "$1" in
    debug_server)
        wait_db
        wait_redis
        python manage.py migrate
        python manage.py runserver 0.0.0.0:8000
    ;;

    celery)
        wait_redis
        # if task result store in db -> call wait_db
        celery -A config.celery_app worker --loglevel=info
    ;;

    celery_beat)
        wait_redis
        # if task result store in db -> call wait_db
        # --pidfile= prevents to generate celerybeat.pid
        celery -A config.celery_app beat --loglevel=info --pidfile=
    ;;

    *)
        # run any command
        sh -c "$@"
    ;;
esac
