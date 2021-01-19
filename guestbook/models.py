from django.db import models

class GuestbookEntry (models.Model):
	entry_date = models.DateTimeField('date entered')
	entry_name = models.CharField(max_length = 100)
	entry_fav_pkmn = models.CharField(max_length = 100)
	entry_fav_joke = models.CharField(max_length=500)
	#entry_picture = models.ForeignKey(GuestbookFile, on_delete=models.CASCADE)
	entry_blurb = models.CharField('Anything you\'d like to say?', max_length = 400)

#class GuestbookFile(models.Model):
	#picture = models.ImageField()
	#picture_comment = models.CharField(max_length = 250)