from django.shortcuts import render
from django.contrib import messages
from contact.forms import ContactView

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent. Thank you.')
            return render(request, 'index.html')
    else:
        form = ContactView()
    return render(request, 'contact.html', {'form': form})