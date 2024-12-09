from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add/',views.add_musician,name='add_muscian'),
    path('edit/<int:id>',views.edit_musician,name='edit_muscian'),
]
