from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose


def make_pic_path (instance, filename):
	advname = instance.adventure.name
	path = 'AdvPics/{0}/{1}'.format(advname, filename)
	return path

def make_gps_path (instance, filename):
	advname = instance.adventure.name
	path = 'AdvGPS/{0}/{1}'.format(advname, filename)
	return path

#def cover_photo (instance):
	#cover = instance.Adventure.objects.filter(adventurepicture__cover = True)
	#return instance.adventurepicture.objects.(cover = True)

class Adventure(models.Model):
	name = models.CharField(max_length = 100)
	dates = models.CharField(max_length = 100) 
	description = models.CharField(max_length = 1000)
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
	picture_smole = ImageSpecField(source='picture',
                                  processors=[Transpose(), ResizeToFill(200, 100)],
                                  format='JPEG',
                                  options={'quality': 60})
	
	def __str__(self):
		return self.picture_desc