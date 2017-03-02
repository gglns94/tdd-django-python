from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new-list'),
    url(r'^(\d+)/$', views.view_list, name='view-list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add-item')
]