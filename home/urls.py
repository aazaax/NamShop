from . import views
from django.urls import path


urlpatterns = [
    path("index/", views.index, name=("HoaiNam")),
    path("order/", views.order, name=("order")),
    path("detail/", views.detail, name=("detail")),
    path("contact/", views.contact, name=("contact")),
    path("feedback/", views.feedback, name=("feedback")),
    path("listproducts/", views.products, name=("listproducts")),
    path("sanpham/", views.sanpham, name=("sanpham")),
    path("signup/", views.signup, name=("signup")),
    path("login/", views.login, name=("login")),
    path("aboutus/", views.aboutus, name=("aboutus")),
]
