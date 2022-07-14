from logging import exception
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from . models import ShortURL
from . forms import ShortURLForm
import uuid
import re
    

def create_short_URL(request):
    """Create model object that maps original url to a randomly
        generated 6 character string"""
    
    if request.method != 'POST':
        form = ShortURLForm()
        context = {'form': form }
        return render(request, 'urlshort/create.html', context)
    else:
        form = ShortURLForm(request.POST)

        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            alias = form.cleaned_data['alias']

            # check if user has chosen a custom alias for their short url
            if len(alias) > 0:
                
                # alias can only contain letters and numbers
                if re.search(r'[^a-zA-Z0-9]', alias):
                    return render(request, 'urlshort/bad_input.html')

                # check alias against database
                if ShortURL.objects.all().filter(short_url=alias).exists():
                    return render(request, 'urlshort/alias_taken.html')

                url_obj = ShortURL(original_url=original_url, short_url=alias, has_alias=True)
                
            else:

                # generate and vaildate short url if none was chosen by user
                while True:
                    short_url = str(uuid.uuid4())[:7]
                    
                    if ShortURL.objects.all().filter(short_url=short_url).exists() == False:
                        break
                
                url_obj = ShortURL(original_url=original_url, short_url=short_url)

        else:
            return render(request, 'urlshort/bad_input.html')

        url_obj.save()
        context = {'short_url': url_obj.short_url}
        return render(request, 'urlshort/created.html', context)
      

def redirect_url(request, pk):
    """Use a short url to obtain original address allowing a redirect"""
    try:
        short_url = ShortURL.objects.get(short_url=pk)
        return redirect(short_url.original_url)
    
    except ShortURL.DoesNotExist:
        return render(request, 'urlshort/pagenotfound.html')
