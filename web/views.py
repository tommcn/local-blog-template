from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import contact, blogPost, dashboardElement, siteSetting


# Create your views here.
def index(request):
    context = {}
    context["settings"] = getSettings()
    return render(request, 'web/home.html', context)


def login_view(request):
    if request.method == 'POST':
        username = "dummy_user"
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("view")
        else:
            return render(request, "web/login.html", {"message": "Wrong Password."})
    else:
        return render(request, "web/login.html")

@login_required
def view(request):
    context = {
        "c": contact.objects.all(),
    }
    context["settings"] = getSettings()
    return render(request, 'web/view.html', context)

@login_required
def add(request):
    if request.method == 'GET':
        context = {}
        context["settings"] = getSettings()
        return render(request, 'web/add.html', context)
    else:
        name = request.POST["name"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        email1 = request.POST["primaryEmail"]
        email2 = request.POST["secondaryEmail"]
        try:
            c = contact()
            c.name = name
            c.address = address
            c.phoneNumber = phone
            c.primaryEmail = email1
            c.secondaryEmail = email2
            c.save()
        except:
            context = {
                "message": "Someone already registered this email",
                "settings": getSettings()
            }
            return render(request, 'web/add.html', context)
        return redirect("/view")

def info(request):
    urls = dashboardElement.objects.all()
    context = {
        "urls": urls,
    }
    context["settings"] = getSettings()
    return render(request, 'web/info.html', context)

def blog(request):
    context = {}
    context["settings"] = getSettings()
    if request.method == 'POST':
        email = request.POST["email"]
        title = request.POST["title"]
        content = request.POST["content"]
        try:
            author = contact.objects.filter(primaryEmail=email)[0]
            b = blogPost()
            b.author = author
            b.title = title
            b.content = content
            b.save()

        except IndexError:
            context['message']=  "The submitted email does not match an email associated with a user"

        
    blogs = blogPost.objects.filter(posted=True).order_by('-created')
    context["b"] = blogs
    return render(request, 'web/blog.html', context=context)



def getSettings():
    settings = siteSetting.objects.first()
    context = {
        "title": settings.site_title,
        "banner": settings.info_banner,
        "color": settings.color,
        "landing": settings.landing_page_text
    }
    return context