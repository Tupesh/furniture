# Furniture Web Application

A Django web app for managing and showcasing furniture inventory with a simple booking flow.

## What this repo contains

- Product catalog pages for furniture items, modular items, and chaukos.
- A booking form that saves customer interest requests to the database.
- Docker and Jenkins/Ansible automation for containerized builds and deployments.

## Features

- Furniture catalog with images, grades, prices, and descriptions.
- Modular items and chaukos listings.
- Booking form backed by a Django model.
- Django admin enabled for CRUD management.
- Media uploads stored under `media/`.

## Tech stack

- Django 4.2
- SQLite (default local database)
- Pillow (image handling)
- django-phonenumber-field (installed; not currently used in models)

## Project structure

- `basicapp/` Django app: models, views, URLs, templates, static assets
- `furniture/` project settings and URL configuration
- `media/` uploaded images
- `db.sqlite3` default SQLite database
- `ansibleconfigs/` Ansible inventory and playbooks for deploys
- `Dockerfile` container build
- `Jenkinsfile` CI/CD pipeline definition

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. (Optional) Create an admin user:

```bash
python manage.py createsuperuser
```

5. Start the dev server:

```bash
python manage.py runserver
```

The app will be available at `http://localhost:8000`.

## App routes

- `/` Home
- `/about/` About page
- `/contactus/` Contact page
- `/furnitureitems/` Furniture catalog
- `/book` Booking form
- `/modularItems` Modular items
- `/chaukos` Chaukos

## Running with Docker

### Build

```bash
docker image build -t djangoapp/furniture .
```

### Run

```bash
docker container run -d --name app-container -p 8000:8000 djangoapp/furniture
```

The application is ready at `http://localhost:8000`.

### Stop

```bash
docker container stop app-container
```

## Deployment (CI/CD)

- `Jenkinsfile` builds a Docker image, runs a Trivy scan, pushes to Docker Hub, and deploys to dev/prod via Ansible.
- Ansible entrypoint is `ansibleconfigs/playbook.yml` using `ansibleconfigs/inventory`.