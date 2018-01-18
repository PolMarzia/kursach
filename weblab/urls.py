from django.conf.urls import url
from weblab import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^main_url/$', views.show_site, name="show_site"),
    url(r'^buy_usl/(?P<usl_id>\d+)$', views.buy_usl, name="buy_usl"),
    url(r'^admin_panel/$', views.admin_panel, name="admin_panel"),
    url(r'^add_usl/$', views.add_usl, name="add_usl"),
    url(r'^delete_usl/(?P<usl_id>\d+)$', views.delete_usl, name="delete_usl"),
    url(r'^edit_usl/(?P<usl_id>\d+)$', views.edit_usl, name="edit_usl"),
    url(r'^auth_url/$', views.auth_url, name="auth_url"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
