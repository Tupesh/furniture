# Furniture Web Application

A Django-based web application for managing furniture inventory with CRUD functionality and booking system. Built using Django's MVT (Model-View-Template) architecture.


## Running with Docker 

### Build and Run

```bash
docker image build -t djangoapp/furniture .
```

The application wis ready at `http://localhost:8000`

### Stop the Application

```bash
docker container run -d --name app-container -p 8000:8000 djangoapp/furniture
```

