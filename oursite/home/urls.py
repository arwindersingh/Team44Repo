from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'^admin/', admin.site.urls),
	url(r'^aboutus/', views.aboutus, name='aboutus'),
	url(r'^cancer/', views.cancer, name='cancer'),
	url(r'^tweet/', views.tweet, name='aboutus'),
	url(r'^visualization/', views.visualization, name='visualization'),

]
