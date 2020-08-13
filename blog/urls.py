from django.urls import path
from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.home, name = 'home_page_view'),
    path('page/<int:page>', views.home, name = 'home_page_view'),
    url(r'^blog/(?P<slug>[\w-]+)/$(?i)', views.detail, name = 'detail_post_view'),
    url(r'^category/(?P<slug>[\w]+)/$(?i)', views.category, name = 'category_view'),
]