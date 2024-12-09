from django.shortcuts import render,redirect
from .import forms
from .models import Album

# Create your views here.

def add_album(request):
    if request.method =="POST":
        albumform=forms.AlbumForm(request.POST)
       
        if albumform.is_valid():
            albumform.save(commit=True)
            return redirect('add_album')
        
    
    else:
        albumform=forms.AlbumForm()
    return render(request,'add_album.html',{'form':albumform})

def edit(request,id):
    data= Album.objects.get(pk=id)
    albumform=forms.AlbumForm(instance=data)
    
    # print(data)
    if request.method =="POST":
        albumform=forms.AlbumForm(request.POST,instance=data)
       
        if albumform.is_valid():
            albumform.save(commit=True)
            return redirect('homepage')
        
    
    # else:                  #as the edit request is on coming on post method so this block will execute so we need to terminate this block,otherwise albumform=forms.Albumform() will replace above albumform
    #     albumform=forms.AlbumForm()
    return render(request,'add_album.html',{'form':albumform})
    
def delete(request,id):
    data=Album.objects.get(pk=id)
    data.delete()
    return redirect('homepage')
    # if request.method =="POST":
    #     albumform=forms.AlbumForm(request.POST)
       
    #     if albumform.is_valid():
    #         albumform.save(commit=True)
    #         return redirect('add_album')
        
    
    # else:
    #     albumform=forms.AlbumForm()
    # return render(request,'add_album.html',{'form':albumform})
