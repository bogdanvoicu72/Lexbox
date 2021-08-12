from django.urls import path
from LEXBOXapp import views



urlpatterns = [
    path('', views.home),
    path('Cerere', views.cerere),
    path('Parcare',views.parcare),
    path('avo', views.avo),
#    path('info_avo', views.info_avo ,name='info_avo'),
    #path('login',views.login_page, name='login'),
    path('user_page',views.user_page,name='user_page'),
    path('user_login',views.user_login,name='user_login'),
    path('user_singin', views.user_signin, name='user_singin'),
    path('cerere_test',views.cerere_test, name = 'cerere_teste'),
    path('test_wizard',views.test_wizard, name = 'test_wizard'),
    path('test_institutii',views.test_institutii, name = 'test_institutii'),

]