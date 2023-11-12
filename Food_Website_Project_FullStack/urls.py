"""
URL configuration for Food_Website_Project_FullStack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Food_Website_Project_FullStack import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = 'home_using_nameAttribute' ),
    path('services/', views.services, name = 'services_using_nameAttribute'),
    path('client/',views.client, name = 'client_using_nameAttribute'),
    path('contact/',views.contact, name = 'contact_using_nameAttribute'),
    path('joinnow/',views.Joinnow, name = 'join_using_nameAttribute'),
    path('calculator/',views.calculator,),
    path('even-odd/',views.evenOdd,),
    path('markssheet/',views.markSheet),
    path('newsdetails/<slug>',views.newsDetails),
    path('saveenquriy/',views.saveEnquiry, name = 'save_en'),

]

# Video 49--
from django.conf import settings 
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 