from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .hikemap import process_gpx, generate_map

from .models import Adventure

@receiver(pre_save, sender=Adventure)
def change_map_file(sender, instance, **kwargs):
    instance.gps_changed = False
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.gpstrax != instance.gpstrax and instance.gpstrax: # Field has changed
            instance.gps_changed = True

@receiver(post_save, sender=Adventure)
def make_map_file(sender, instance, **kwargs):
	if kwargs['created'] or instance.gps_changed:
		generate_map(instance.gpstrax.path, instance.id)

#Still need register signals.py - make an apps module with AppsConfig