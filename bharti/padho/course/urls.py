from django.contrib import admin
from django.urls import path
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index, name='course'),
    path('logout', views.logoutuser,name="logout"),
    path('login', views.loginuser,name="login"),
    path('cart', views.cart,name="cart"),
    path('signup', views.signupusers,name="signup"),
    path('aftlogin', views.aftlogin,name="aftlogin"),
]
