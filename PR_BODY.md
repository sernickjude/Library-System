PR Title: Add Photo Album app with local + optional Cloudinary storage

Summary
-------
Adds a Photo Album app with CRUD for albums and photos, role-based access utilities, and optional Cloudinary storage. Local development uses `ImageField` and MEDIA settings; Cloudinary is used only when `CLOUDINARY_URL` is set.

Key changes
-----------
- photo_album: models, views, templates for album/photo CRUD
- photo upload form: added `enctype="multipart/form-data"`
- Photo model: uses `ImageField` locally, `CloudinaryField` when `CLOUDINARY_URL` set
- config/settings.py: MEDIA_URL, MEDIA_ROOT, WhiteNoise middleware, STATIC_ROOT, STATICFILES_STORAGE
- config/urls.py: serve media files in DEBUG
- requirements.txt: added `whitenoise` and Pillow installed in environment

How to test locally
-------------------
1. Activate venv and install deps:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

2. Apply migrations and collect static:

```powershell
python manage.py migrate
python manage.py collectstatic --noinput
```

3. Run server and verify:

```powershell
python manage.py runserver
```

- Visit http://127.0.0.1:8000/, create an album, add a photo, confirm it displays.
- Verify uploaded file exists under `media/photos/`.
- Check admin for Photo entries.

Render deployment notes
-----------------------
- Build command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
- Start command: `gunicorn config.wsgi:application`
- Required env vars: `SECRET_KEY`, `DEBUG=false`, `ALLOWED_HOSTS` (Render domain), `DATABASE_URL` (if using Postgres), optional `CLOUDINARY_URL`.

Checklist for reviewer
----------------------
- [ ] Photo upload works locally (file saved under `media/photos/`)
- [ ] Admin shows `Photo` entries with images
- [ ] No unapplied migrations
- [ ] Static files served correctly after `collectstatic`
- [ ] Requirements up to date

Notes
-----
Cloudinary integration is optional; local uploads are used by default in development to avoid requiring external credentials.
