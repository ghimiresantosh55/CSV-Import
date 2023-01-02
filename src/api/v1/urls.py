from django.urls import path, include

urlpatterns = [
    path('csvapp/', include('src.csvapp.urls')),
    
]
