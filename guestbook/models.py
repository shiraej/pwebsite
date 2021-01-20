from django.db import models
from django.forms import ModelForm


class GuestbookEntry (models.Model):

	entry_date = models.DateTimeField('date entered', auto_now=True)
	entry_name = models.CharField(max_length = 100)
	entry_fav_pkmn = models.CharField(max_length = 100)
	entry_fav_joke = models.CharField(max_length=500)
	entry_picture = models.ImageField(upload_to = 'uploads/', blank = True)
	entry_blurb = models.CharField('Anything you\'d like to say?', max_length = 400)



class GuestbookForm(ModelForm):
	class Meta:
		model = GuestbookEntry
		fields = "__all__"