from django.conf.urls import url

from . import admin

urlpatterns = [
    url(r'^test_admin/admin/', admin.site.urls),
]
