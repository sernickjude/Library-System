# Photo Album Management (based on Library-System)

This repository contains a Django project with a new `photo_album` app implementing basic album and photo management using Class-Based Views.

Quick start (local):

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Apply migrations and create a superuser:

```bash
.venv\Scripts\python manage.py migrate
.venv\Scripts\python manage.py createsuperuser
```

3. (Optional) create RBAC groups:

```bash
.venv\Scripts\python manage.py create_groups
```

4. Run the dev server:

```bash
.venv\Scripts\python manage.py runserver
```

5. Visit `http://127.0.0.1:8000/albums/`.

Production / Render notes:

- Set `DATABASE_URL` environment variable to a Postgres connection URL on Render.
- Set `CLOUDINARY_URL` for Cloudinary storage and the settings will enable Cloudinary storage.
- Configure `ALLOWED_HOSTS` as a comma-separated env var.

This README should be extended with your deployment URL and repo link when ready.
