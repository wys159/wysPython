from django.conf.urls import include, url
import views
urlpatterns = [
	url('^$',views.order),
	url('^order_handle/$',views.order_handle),
]