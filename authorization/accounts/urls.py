from django.urls import path
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("user/", UserDetailsView.as_view(), name="user"),
    path("user/<int:pk>/", UserDetailsView.as_view(), name="userbyid"),
    path("products/", ProductView.as_view(), name="products"),
    path("products/<int:pk>/", ProductView.as_view(), name="deleteproduct"),
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/<int:pk>/", CartView.as_view(), name="deletecart"),
    path("order/", OrderView.as_view(), name="order"),
    path("order/<int:pk>/", OrderView.as_view(), name="deleteorder"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profilebyid"),
]
