from django.db import models
from django.forms import ModelForm, Textarea, TextInput, FileInput



class GuestbookEntry (models.Model):

	entry_date = models.DateTimeField('Date Entered', auto_now=True)
	entry_name = models.CharField('Name', max_length = 100, blank = False)
	entry_fav_pkmn = models.CharField('What is your favourite Pokemon?', max_length = 100, blank=True)
	entry_fav_joke = models.CharField('Tell me your favourite joke!', max_length=500, blank = True)
	entry_blurb = models.CharField('Anything else you\'d like to say?', max_length = 400, blank = True)

	def __str__(self):
		return self.entry_name
		
	def clean(self):
		if self.entry_fav_pkmn == '':
			self.entry_fav_pkmn = 'Potatomon'
		if self.entry_fav_joke == '':
			self.entry_fav_joke = 'How many ants can you fit in an appartment building? \n \n -ten-ants!'
			#make loop function to loop through silly jokes
		if self.entry_blurb == '':
			self.entry_blurb = "something interesting"

class GuestbookForm(ModelForm):
	class Meta:
		model = GuestbookEntry
		widgets = {
			'entry_name' : TextInput(attrs={'class':'form-control col-6'}),
			'entry_fav_pkmn' : TextInput(attrs={'class':'form-control', 'value':""}),
			'entry_fav_joke' : Textarea(attrs={'cols': 40, 'rows':2, 'class':'form-control'}),
			

			'entry_blurb': Textarea(attrs={'cols': 40, 'rows': 5, 'class':'form-control'}),

		}

		fields = "__all__"

