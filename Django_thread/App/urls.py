from django.urls import path, re_path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import *

urlpatterns = [
    path('' , home, name='home'  ),
    path('datasend/' , datasend, name='datasend'  ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
