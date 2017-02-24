from django.conf.urls import url

from . import views

app_name = 'improve'
urlpatterns = [
    # ex. /improve/
    url(r'^$', views.TicketList.as_view(), name='ticket_list'),
]
