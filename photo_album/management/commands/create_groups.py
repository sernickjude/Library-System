from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Create RBAC groups for the photo album app'

    def handle(self, *args, **options):
        # Create album_admin group with add/change/delete permissions on Album and Photo
        from photo_album.models import Album, Photo

        album_ct = ContentType.objects.get_for_model(Album)
        photo_ct = ContentType.objects.get_for_model(Photo)

        perms = []
        for ct in (album_ct, photo_ct):
            perms += list(Permission.objects.filter(content_type=ct))

        group, created = Group.objects.get_or_create(name='album_admin')
        group.permissions.set(perms)
        group.save()

        self.stdout.write(self.style.SUCCESS('Created/updated group album_admin with album/photo permissions'))
