# django-template
More complete django startproject with:
- Docker as development environment with docker compose,
- Celery - as separate docker container,
- Redis - as task broker - separate docker container too,
- better structure - separate config package and tests package from django application module
- base model for User and base timestamped abstract model for model classes
- tests run with pytest

### Reusing template
1. Adjust main project name (change `project` name for custom name, IDE rename tools as very useful there)
    - setup.cfg
    - config/api_routers.py
    - config/celery_app.py
    - config/urls.py
    - config/settings/base.py
    - project directory name
    - projecttemplates/base.html
    - project/users
        - apps.py
        - models.py
        - urls.py
        - apps.py
    - tests/conftest.py
    - tests/test_models.py
    - etc.

1. Adjust settings in config package.
1. Create .env in root directory, example file in .envs/.env_example

### Development with containers
1. Ensure docker & docker-compose are installed on your OS
1. Build images with docker-compose
    ```shell
    docker-compose -f local_docker_compose.yml build
    ```
1. Run builded images
    ```shell
    docker-compose -f local_docker_compose.yml up
    ```
1. To run commands eg. python manage.py createsuperuser:
    1. Get Django container ID:
        ```
        docker ps
        CONTAINER ID   IMAGE                ... NAME
        a67a7f1dc051   cookery_book_django  ... template_django_debug_server # <- This container's ID
        b2ffdb05d42a   cookery_book_django  ... template_celery
        93b8c012f0b5   cookery_book_django  ... template_celery_beat
        a0ee8348137e   postgres:14.1        ... template_postgres
        cf8dd254c372   redis:6.2.6-alpine   ... template_redis
        ```
    1. Run command
        ```bash
        docker exec -it a67a7f1dc051 python manage.pt createsuperuser
        ```

### Development fully local
1. Create virtual environment with venv or other stuff (poetry, virtualenv, virtualenvwrapper, pyenv)
    ```
    python -m venv venv
    ```
1. Activate virtual environment
    ```
    source ./venv/bin/activate
    ```
1. Install requirements from requirements (install all requirements recommended)
    ```
    pip install -r requirements/base.txt
    pip install -r requirements/dev.txt
    pip install -r requirements/prod.txt
    pip install -r requirements/test.txt
    ```
1. Ensure Postgres & Redis are running (or just use SQLite3 and ) and adjust settings and environment variables in `.env` file. (Create if it does not exist.)
1. If want to use .env file set `DJANGO_READ_DOT_ENV_FILE` environment variable.
    ```shell
    export DJANGO_READ_DOT_ENV_FILE=True
    ```
1. Run standard django project commands during development:
    ```shell
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    # OR
    python manage.py runserver_plus
    ```

### Unit tests
1. If `DJANGO_SETTINGS_MODULE` is set ensure it is equal `config.settings.test` or run tests with `--ds=config.settings.test` parameter.
1. Run tests with pytest using command:
    ```
    pytest
    ```
