from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q


# Create your views here.


def CategoryView(request):
    # data = Category.objects.all()
    if request.method == 'POST':
        form = CreateCategory(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/subcategory/")
        # else:
        #     form = CreateCategory()
    else:
        form = CreateCategory()
    con = {"form": form}
    return render(request, "category.html", con)


def SubcategoryView(request):
    data = Subcategory.objects.all()
    if request.method == "POST":
        form = CreateSubcategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/product/")
    else:
        form = CreateSubcategory()
    con = {"form": form}
    return render(request, "subcategory.html", con)


def ProductView(request):
    # data = Product.objects.all()
    if request.method == "POST":
        form = CreateProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/index/")
        else:
            form = CreateProduct()
    else:
        form = CreateProduct()
    con = {"form": form}
    return render(request, "product.html", con)


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Product.objects.filter(name__icontains=q)
        # data = Product.objects.filter(owner_name__icontains=q)
    else:
        data = Product.objects.all()
    con = {'data': data}
    return render(request, "index.html", con)


def AddProduct(request):
    context = {}
    context["form"] = CreateProduct()

    if request.method == "POST":

        form = CreateProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(""))
        else:
            context["form"] = form
            return render(request, "product.html", context)

    return render(request, "product.html", context)


def EditProduct(request, id):
    form = Product.objects.get(id=id)
    if request.method == "POST":
        form = CreateProduct(request.POST, instance=form)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CreateProduct(instance=form)
    context = {'data': form}
    return render(request, "edit.html", context)


def DelProduct(request, id):
    form = Product.objects.get(id=id)
    form.delete()
    return redirect("/index/")
