from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rango'
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'about/$', views.about, name='about'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'add_category/$', views.add_category, name='add_category'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^visitor_cookie_handler',views.visitor_cookie_handler, name='visitor_cookie_handler'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^register/$', views.register, name='register'), ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)