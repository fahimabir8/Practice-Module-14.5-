from django.shortcuts import render
from .forms import SampleForm
# Create your views here.
def home(request):
    if (request.method == 'POST'):
        data = SampleForm(request.POST)
        if data.is_valid():
            print(data.cleaned_data)        
    else:
        data = SampleForm()
    return render(request, 'home.html', {'form' : data})