from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from visualization.models import Post

# urlpatterns = [
# 	url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="visualization/visualization.html"))
# 	# url(r'^admin/', admin.site.urls),
# 	# url(r'^$', include('webapp.urls')),
# ]
