from django.contrib import admin
from django.urls import path
from .  import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', views.Home,name='home'),
    path('About/',views.About,name='about'),    
    path('Contact/',views.Contact,name='contact'),
    path('insertTask/',views.insertTask,name='insertTask'),
 
    
]
