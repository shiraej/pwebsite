from django.shortcuts import render, get_object_or_404
from .models import Adventure, AdventurePicture
from django.contrib.auth.decorators import login_required


@login_required
def adv_gallery(request):
	gallery = Adventure.objects.all()
	context = {'gallery': gallery, }
	return render(request, 'gallery/gallery.html', context)

@login_required
def adv_details(request, adventure_id):
	adv = get_object_or_404(Adventure, pk=adventure_id)
	#pics = get_object_or_404(AdventurePicture, pk=adventure_id)
	try:
		pics = AdventurePicture.objects.filter(adventure=adventure_id)
	except AdventurePicture.DoesNotExist:
		raise Http404("Pictures do not exist")
	context = {'adv' : adv, 'pics' : pics}
	return render(request, 'gallery/details.html', context)

