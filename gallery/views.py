from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Adventure, AdventurePicture
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt

@login_required
def adv_gallery(request):
	gallery = Adventure.objects.all()
	context = {'gallery': gallery, }
	return render(request, 'gallery/gallery.html', context)

@login_required
def adv_details(request, adventure_id):
	adv = get_object_or_404(Adventure, pk=adventure_id)
	try:
		pics = AdventurePicture.objects.filter(adventure=adventure_id)
		firstpic = pics[0]
	except (AdventurePicture.DoesNotExist, IndexError):
		pics = False
		firstpic = False
	context = {'adv' : adv, 'pics' : pics, 'firstpic':firstpic}
	return render(request, 'gallery/details.html', context)

@login_required
@xframe_options_exempt
def adv_map(request, adventure_id):
	return render(request, 'gallery/maps/{0}.html'.format(adventure_id))

