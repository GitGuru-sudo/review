from django.shortcuts import render, redirect
from app.models import activity, Review

# Login view
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Save login data
        login_entry = activity(username=username, password=password)
        login_entry.save()

        return redirect("index")
    return render(request, "login.html")


# Index view
def index(request):
    return render(request, "index.html")


# Review form view
def review(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        drc = request.POST.get("drc")

        review_entry = Review(name=name, email=email, phone=phone, drc=drc)
        review_entry.save()

        return redirect("index")

    return render(request, "review.html")
