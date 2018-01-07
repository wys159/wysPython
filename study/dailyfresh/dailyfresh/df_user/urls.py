from django.conf.urls import url
import views
urlpatterns = [
    url(r'^register/$',views.register ),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_exsit$',views.register_exsit),
    url(r'^register_exsit/$',views.register_exsit),
    url(r'^login/$',views.login),
    url(r'^logout/$', views.logout),
	url(r'^login_handle/$',views.login_handle),
	url(r'^info/$',views.info),
	url(r'^order(\d{0,})/$',views.order),
	# url(r'^order/(\d+)/$',views.order),
	url(r'^site/$',views.site),

]
