from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Try to use CloudinaryField when available; fallback to URLField so local
# testing still works without Cloudinary installed.
try:
    from cloudinary.models import CloudinaryField
    _USE_CLOUDINARY = True
except Exception:
    CloudinaryField = None
    _USE_CLOUDINARY = False

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # Use CloudinaryField when available; otherwise store an image URL.
    if _USE_CLOUDINARY:
        image = CloudinaryField('image')
    else:
        image = models.URLField(max_length=1024)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title
