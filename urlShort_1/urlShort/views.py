from django.shortcuts import render, redirect
import random
import string
from .forms import Url  # Assuming Url is your form class for URL input
from .models import UrlData

def url_shorten(request):
    context = {}
    
    if request.method == 'POST':
        form = Url(request.POST)
        
        if form.is_valid():
            # Generate a random slug
            slug = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            url = form.cleaned_data["url"]
            
            # Create a new UrlData object
            new_url = UrlData.objects.create(url=url, slug=slug)
            
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Associate the new URL with the authenticated user (if needed)
                request.user.urldata.add(new_url)
            
            # Redirect to success page
            return redirect('shorten_success')
    else:
        form = Url()
    
    # Provide data to the template
    base_url = request.build_absolute_uri('/')
    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data,
        'base_url': base_url
    }
    
    return render(request, 'index.html', context)

def url_redirect(request, slug):
    try:
        data = UrlData.objects.get(slug=slug)
        return redirect(data.url)
    except UrlData.DoesNotExist:
        # Handle case where slug does not exist (e.g., show a 404 page)
        return render(request, '404.html')



def shorten_success(request):
    return render(request, 'shorten_success.html')