from django.conf.urls import url
import views
urlpatterns = [
    url(r'^register/$',views.register ),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_exsit$',views.register_exsit),
    url(r'^register_exsit/$',views.register_exsit),
]
