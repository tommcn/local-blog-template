from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .models import contact, blogPost, dashboardElement


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'web/home.html')
    else:
        return render(request, 'web/login.html')


def login_view(request):
    username = "dummy_user"
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return index(request)
    else:
        return render(request, "web/login.html", {"message": "Wrong Password."})


def view(request):
    if request.user.is_authenticated:
        context = {
            "c": contact.objects.all(),
        }
        return render(request, 'web/view.html', context)
    else:
        return render(request, 'web/login.html')


def add(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'web/add.html')
        else:
            name = request.POST["name"]
            address = request.POST["address"]
            phone = request.POST["phone"]
            email1 = request.POST["primaryEmail"]
            email2 = request.POST["secondaryEmail"]

            c = contact()
            c.name = name
            c.address = address
            c.phoneNumber = phone
            c.primaryEmail = email1
            c.secondaryEmail = email2
            c.save()
            return view(request)
    else:
        return render(request, 'web/login.html')


def info(request):
    if request.user.is_authenticated:
        urls = dashboardElement.objects.all()
        context = {
            "urls": urls,
        }
        return render(request, 'web/info.html', context)
    else:
        return render(request, 'web/login.html')

def blog(request):
    if request.user.is_authenticated:
        context = {}
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

            
        blogs = blogPost.objects.filter(posted=True)
        context["b"] = blogs
        return render(request, 'web/blog.html', context=context)
    else:
        return render(request, 'web/login.html')
