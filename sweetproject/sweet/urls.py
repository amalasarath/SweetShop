from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name="sweet"
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:prod_slug>/', views.ProductDetail, name='ProdCatDetail'),
    path('/register', views.register_request, name="register"),
    path("/login", views.login_request, name="login"),


]