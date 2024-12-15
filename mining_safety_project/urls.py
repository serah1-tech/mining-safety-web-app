from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Imported HttpResponse for the view
from . import views  # Import the home view
from django.conf.urls.static import static
from django.conf import settings
from education import views  # Ensure this points to the correct app


# Defined the home view
def home(request):
    return HttpResponse("<h1>Welcome to the Mining Safety App</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Map the root URL to the homepage view
    path('education/', include('education.urls')),  # Education app URLs
    path('hazards/', include('hazards.urls')),        # Hazards app URLs
    path('auth/', include('django.contrib.auth.urls')),  # Authentication views
    path('users/', include('users.urls')),  # Users app URLs
    
    
]

# Serve static files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
