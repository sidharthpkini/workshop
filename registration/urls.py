from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration import views
from registration.views import *
from registration.models import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='register/templates/register/user_update_form.html'),
        name='user_registration_success'),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(),
         name="chocolate_detail"),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='edit_profile'),

	]