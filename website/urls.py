from django.contrib import admin
from django.urls import path, include
from .views.start_page import redirect_to_index
import sys
sys.path.append('..')
from library import urls as library_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_index, name='redirect_to_index'),
    path('library/', include(library_urls)),
]
