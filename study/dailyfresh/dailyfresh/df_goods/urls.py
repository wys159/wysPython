from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^(\d+)$',views.detail),
    url(r'^base$',views.base),
]