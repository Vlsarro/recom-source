from django.conf.urls import url, include
from django.contrib import admin


# Later it should be divided in sub-categories, weapon, wine, etc.
urlpatterns = [
    url(r'^reviews/', include('reviews.urls', namespace="reviews")),
    url(r'^admin/', admin.site.urls),
    url('^accounts/', include('django.contrib.auth.urls', namespace="auth"))
]
