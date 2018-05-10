from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'^admin/', admin.site.urls),
	url(r'^map/', views.map, name='map')
]
