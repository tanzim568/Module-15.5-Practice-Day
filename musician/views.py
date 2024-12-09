from django.shortcuts import render,redirect
from .import forms
from .models import Musician
# Create your views here.


def add_musician(request):
    if request.method == 'POST':
        musiciain=forms.MusicianForm(request.POST)
        if musiciain.is_valid():
            musiciain.save(commit=True)
            return redirect ('add_muscian')
        
    else:
        musiciain=forms.MusicianForm()
    return render(request,'add_musician.html',{'form':musiciain})
        
        
def edit_musician(request,id):
    data=Musician.objects.get(pk=id)
    musiciain=forms.MusicianForm(instance=data)
    
    
    if request.method == 'POST':
        musiciain=forms.MusicianForm(request.POST ,instance=data)
        if musiciain.is_valid():
            musiciain.save(commit=True)
            return redirect ('homepage')
        
    # else:
    #     musiciain=forms.MusicianForm()
    return render(request,'add_musician.html',{'form':musiciain})
        
        