## Fast Template

Easily generate a template for your [FastAPI](http://fastapi.tiangolo.com) applications, complete with JWT authentication and Google sign-in.

### Installation

You can install Fast Template via `pip`:

```sh
pip install fast-template-python
```

Or using `poetry`:

```sh
poetry add fast-template-python
```

### Usage

To initialize a project in an existing folder:

```sh
fast-template init project_name .
```

To create a new project:

```sh
fast-template init project_name
```

Once the template is set up, you'll need to create a `.env` file as required by the `settings.py` file (feel free to modify it to suit your needs).
An example of a `.env` is:
```
POSTGRES_URL = postgresql+asyncpg://postgres@localhost/your_db_name

ACCESS_TOKEN_SECRET = Your-Access-Token-Secret
REFRESH_TOKEN_SECRET = Your-Refresh-Token-Secret
RESET_PASSWORD_SECRET = Your-Reset-Password-Secret

SECRET_KEY = Your-Secret-Key

JWT_ALGORITHM = HS256

MAIL_USERNAME = yourname@yourmail.com
MAIL_FROM_NAME = Your-Name
MAIL_PASSWORD = yourmailpassword
MAIL_FROM = yourname@yourmail.com
MAIL_PORT = 000 # 587 for gmail
MAIL_SERVER = your_mail_server # smtp.gmail.com for gmail

REDIS_HOST = localhost
REDIS_PORT = 6379

GOOGLE_CLIENT_ID = YOUR_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = YOUR_GOOGLE_CLIENT_SECRET
GOOGLE_REDIRECT_URI = https://yourdomain.com/auth/google/callback
```

#### Migrations

You can set up database migrations using Alembic:

```sh
alembic init —template async migrations
```

For more information on using Alembic, check the [official tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html#creating-an-environment).

### Features

#### Authentication
- JWT-based authentication is built-in.
- Google sign-in is fully integrated, right down to the database layer.

#### Extensible Folder Structure
The folder structure is designed to be modular and scalable, inspired by Philip Okiokio ([LinkedIn](https://www.linkedin.com/in/philip-okiokio/), [GitHub](https://github.com/philipokiokio)). It promotes loose coupling and clean separation of concerns.

Each operation is handled by three main layers:
1. **Router Layer**: Defines FastAPI routes.
2. **Service Layer**: Contains the business logic.
3. **Database Layer**: Manages database interactions.

The data flow is structured as follows:

```
Router Layer → Service Layer → Database Layer
```

The service layer handles the data exchange between the router and the database, while the router serializes requests and passes them to the service.

The folder structure on running
```sh
fast-template init totrac
```
is
```md
TOTRAC
├── database
│   ├── db_handlers
│   │   ├── __init__.py
│   │   ├── auth_db_handler.py
│   ├── orms
│   │   ├── __init__.py
│   │   ├── auth_orm.py
├── job_manager
│   ├── email
│   │   ├── mailer.py
│   ├── job_runner.py
├── root
│   ├── templates
│   │   ├── auth
│   │   │   ├── info_email_template.html
│   ├── utils
│   │   ├── abstract_base.py
│   │   ├── base_models_abstract.py
│   ├── app_routers.py
│   ├── app.py
│   ├── arq_worker.py
│   ├── constants.py
│   ├── database.py
│   ├── logging.py
│   ├── redis_manager.py
│   ├── settings.py
├── routers
│   ├── __init__.py
│   ├── auth_router.py
│   ├── miscellaneous_router.py
├── schemas
│   ├── __init__.py
│   ├── auth_schemas.py
│   ├── error_messages_schema.py
│   ├── file_upload_schema.py
│   ├── response_info_schema.py
├── services
│   ├── utils
│   │   ├── auth_utils.py
│   │   ├── exceptions.py
│   │   ├── file_downloader.py
│   │   ├── file_uploader_utils.py
│   │   ├── google_auth_utils.py
│   │   ├── token_utils.py
│   ├── auth_services.py
│   ├── miscellaneous_services.py
├── venv
├── __init__.py
├── .gitignore
├── make_db_migrations.py
├── Makefile
├── pyproject.toml
├── Readme.md
├── requirements.txt

```

#### Pre-configured Services
The root folder contains core services required for the backend, including:
1. Database setup
2. Redis caching
3. Email templates
4. Background workers (using ARQ)
5. Logging configuration
6. Application settings

#### Schema and Database Layers
- **Schema**: Pydantic models for serialization/deserialization, organized by feature (e.g., authentication schemas are in the `auth` folder).
- **Database**: Handlers and ORM integration using [SQLAlchemy](http://sqlalchemy.org).

### Work in Progress
This package is a work in progress, created to streamline the setup of backend projects.

### 🐛 Bugs/Feature Requests

Contributions are welcome! Feel free to open a pull request or an issue for feature requests or bug reports.

