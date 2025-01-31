from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('products/<product>', views.product_cat, name="productcat"),
    path('signup', views.signup, name="signup"), #signUp page
    path('products/<product_brand>/<product_slug>', views.product_page, name="product_page"),
]
