"""Define basic routes"""
from django.conf.urls import include, url
from django.contrib import admin

# Import the views from views.py
from . import views

urlpatterns = [ # pylint: disable=invalid-name
    # Examples:
    # url(r'^$', 'whatistheplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Main app routes
    url(r'^$', views.index, name='Home'),
    url(r'^events/', views.events, name='Events'),
    url(r'^about/', views.about, name='About'),
    url(r'^signup/', views.signup, name='Sign Up'),
    url(r'^login/', views.login, name='Log In'),
    url(r'^logout/', views.logout, name='Log Out')
]
