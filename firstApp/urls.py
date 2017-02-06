from django.conf.urls import include, url
from django.contrib import admin
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]