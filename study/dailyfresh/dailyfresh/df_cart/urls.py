from django.conf.urls import include, url
import views

urlpatterns = [
	url('^$',views.cart),
	url('^add/(\d+)_(\d+)/$',views.add),
	url('^edit/(\d+)_(\d+)/$',views.edit),
	url('^cdel/(\d+)/$',views.cdel)
]