from django.conf.urls import url
from . import views

# this stuff will be referenced within the local namespace
# because I gave the namespace reviews in the project urls.py
urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?<review_id>[0-9]+/', views.review_detail, name='review_detail'),
    # ex: /wine/
    url(r'^wine$', views.wine_list, name='wine_list'),
    # ex: /wine/5
    url(r'^wine/(?<wine_id>[0-9]+/', views.wine_detail, name='wine_detail'),
]