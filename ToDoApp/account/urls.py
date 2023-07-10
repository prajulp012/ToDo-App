from django.urls import path
from .views import *

urlpatterns = [
    path('home/',Home.as_view(),name='home'),
    path('signup/',SignupReg.as_view(),name='signup'),
    path('lgout',LgOut.as_view(),name='lgout'),
    path('details/',Details.as_view(),name='details'),
    path('delete/<int:tdel>',Delete.as_view(),name='deletee'),
    path('update/<int:tupd>',Update.as_view(),name='update')
]