from django.shortcuts import render
from .models import Adventure, AdventurePicture
from django.contrib.auth.decorators import login_required

@login_required
def adv_gallery(request):
	gallery = Adventure.objects.all()
	context = {'gallery': gallery, }
	return render(request, 'gallery/gallery.html', context)
