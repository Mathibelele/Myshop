from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Feedback
from django.contrib import messages
from django.views import View

from .forms import FeedbackForm
# Create your views here.

class IndexView(View):
    def get(self, request):
        product_numb = 4
        products = Product.objects.all().order_by('id')[:4]
        suits = Product.objects.filter(brand__title = "Tom Ford")
        return render(request, "products/home.html", {
            "name": "donald",
            "number": product_numb,
            "products": products
        })
    def post(self, request):
        pass
def index(request):
    product_numb = 4
    products = Product.objects.all().order_by('id')[:4]
    suits = Product.objects.filter(brand__title = "Tom Ford")
    return render(request, "products/home.html", {
        "name": "donald",
        "number": product_numb,
        "products": products
    })
def signup(request):
    return render(request, "products/signup.html")

def product_cat(request, product):
    if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
        return HttpResponse(f"Here is the list of our {product}")
    else:
        return HttpResponse("The page does not exists.")
    
def product_page(request, product_brand, product_slug):
    product = Product.objects.get(slug =product_slug)
    my_feedback = Feedback.objects.get(product = product, id=1)
    form = FeedbackForm(instance = my_feedback)
    reviews = Feedback.objects.filter(product = product)
    if request.method == "GET":
        return render(request, "products/product.html", {
            "product": product,
            "form": form,
            "reviews": reviews,
         })
    else:
        form = FeedbackForm(request.POST,instance = my_feedback)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback was submitted successfully.")
            
        return render(request, "products/product.html", {
            "product": product,
            "form": form,
            "reviews": reviews,
         })
    