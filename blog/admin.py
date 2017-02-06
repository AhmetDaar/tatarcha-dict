from django.contrib import admin
from .models import Post

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

admin.site.register(Post)