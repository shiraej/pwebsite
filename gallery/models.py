from django.db import models
#from django.db.models.signals import post_save
from .hikemap import process_gpx, generate_map

def make_pic_path (instance, filename):
	advname = instance.adventure.name
	path = 'AdvPics/{0}/{1}'.format(advname, filename)
	return path

def make_gps_path (instance, filename):
	advname = instance.name
	ext = filename.split('.')[-1]
	path = 'AdvGPS/{0}.{1}'.format(advname,ext)
	return path

#def cover_photo (instance):
	#cover = instance.Adventure.objects.filter(adventurepicture__cover = True)
	#return instance.adventurepicture.objects.(cover = True)

class Adventure(models.Model):
	name = models.CharField(max_length = 100)
	dates = models.CharField(max_length = 100) 
	description = models.TextField(max_length = 5000)
	gpstrax = models.FileField(upload_to = make_gps_path, blank = True)
	
	def cover_photo (self):
		cov = self.adventurepicture_set.get(cover = True)
		return cov.picture
	
	cover = cover_photo
	def __str__(self):
		return self.name

class AdventurePicture(models.Model):
	picture = models.ImageField(upload_to = make_pic_path, blank = True)
	picture_desc = models.CharField(max_length=200)
	adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
	cover = models.BooleanField()
	
	def __str__(self):
		return self.picture_desc