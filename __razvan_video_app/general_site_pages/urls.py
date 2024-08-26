#
#
#
#
#
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('evenimente-nunta-botez-constanta', views.ToateVideoclipurilePageView.as_view(), name="evenimente-nunta-botez-constanta"),
    path('despre-mine', views.DespreMinePageView.as_view(), name="despre-mine"),
    path('contact-constanta', views.ContactPageView.as_view(), name="contact-constanta"),
]