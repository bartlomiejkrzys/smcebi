from django.conf.urls import url

from .views import LowerGroundFloorView
from .views import GroundFloorView
from .views import FirstFloorView
from .views import SecondFloorView

urlpatterns = [
    url('^lowerground$', LowerGroundFloorView.as_view(), name='lowerground_floor'),
    url('^ground$', GroundFloorView.as_view(), name='ground_floor'),
    url('^first$', FirstFloorView.as_view(), name='first_floor'),
    url('^second$', SecondFloorView.as_view(), name='second_floor'),
]
