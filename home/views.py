from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/HoaiNam.html")


def detail(request):
    return render(request, "pages/detail.html")


def order(request):
    return render(request, "pages/order.html")


def feedback(request):
    return render(request, "pages/feedback.html")


def login(request):
    return render(request, "pages/login.html")


def products(request):
    return render(request, "pages/listproducts.html")


def sanpham(request):
    return render(request, "pages/sanpham.html")


def signup(request):
    return render(request, "pages/signup.html")


def contact(request):
    return render(request, "pages/contact.html")


def aboutus(request):
    return render(request, "pages/aboutus.html")
