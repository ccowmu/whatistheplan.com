"""Define basic routes"""
from django.conf.urls import include, url
from django.contrib import admin

# Import the views from views.py
from whatistheplan import views

urlpatterns = [ # pylint: disable=invalid-name
    # Examples:
    # url(r'^$', 'whatistheplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Main app routes
    url(r'^$', views.index, name='Home'),
    url(r'^home/', views.index, name='Home'),
    url(r'^events/', views.events, name='Events'),
    url(r'^about/', views.about, name='About'),
    url(r'^forum/', views.forum, name='Forum'),
    url(r'^signup/', views.user_signup, name='Sign Up'),
    url(r'^login/', views.user_login, name='Log In'),
    url(r'^logout/', views.user_logout, name='Log Out')
]
