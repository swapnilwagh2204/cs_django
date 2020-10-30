from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^Blog/', include('Blog.urls')),
    url(r'^growth/', include('growth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
