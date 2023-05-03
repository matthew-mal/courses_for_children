from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('courses/', include('courses.urls')),
                  path('news/', include('news.urls')),
                  path('user/', include('user.urls')),
                  path('login/', include('login.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
