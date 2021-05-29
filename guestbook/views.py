from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from .models import GuestbookForm, GuestbookEntry
@login_required
def guestentry(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GuestbookForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect(reverse('thankyou'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GuestbookForm()
        homepage_link = reverse('homepage')
    return render(request, 'guestbook/form.html', {'form': form, 'homepage_link':homepage_link})
@login_required
def guestbook(request):
    latest_guestbook = GuestbookEntry.objects.order_by('entry_date').reverse()
    context = {'latest_guestbook': latest_guestbook}
    return render(request, 'guestbook/guestbook.html', context)

def thankyou(request):
    return(render(request, 'guestbook/thankyouredirect.html'))



