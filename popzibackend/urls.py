from django.contrib import admin  
from django.urls import path, include  

urlpatterns = [  
    path('admin/', admin.site.urls),
    path('api/', include('problems.urls')),  # Dedicated path for 'problems' app
    path('api/', include('notes.urls')),  # Dedicated path for 'notes' app
]