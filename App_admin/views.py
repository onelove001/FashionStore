from django.shortcuts import *
from django.contrib.auth import login as dlogin, logout as dlogout, authenticate
from django.contrib import messages
from .models import *
from App_store.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


@login_required
def admin_dashboard(request):
    messages = Messages.objects.all().count()
    lists = List.objects.all().count()
    visitors = messages + lists
    context = {"messages":messages, "lists":lists, "visitors":visitors}
    return render(request, "admin_templates/admin_index.html", context)


def login(request):
    context = {}
    return render(request, "admin_templates/login.html", context)


def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            dlogin(request, user)
            return redirect("admin_dashboard")
        else:
            messages.error(request, "Invalid Details!")
            return redirect("login")


@login_required
def logout(request):
    dlogout(request)
    return redirect("store_home")


@login_required
def contact(request):
    con = Contact.objects.filter(id=1)
    if len(con) > 0:
        context = {"contact":con.first()}
    else:
        context={}
    if request.method=="POST":
        location = request.POST.get("location")
        email = request.POST.get("email")
        phone = request.POST.get("cell_phone")
        location2 = request.POST.get("location2")
        email2 = request.POST.get("email2")
        phone2 = request.POST.get("cell_phone2")
        try:
            if len(con) == 0:
                contact = Contact(location=location, email=email, phone=phone)
                contact.save()
                messages.success(request, "Success!")
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                contact = Contact.objects.get(id=1)
                contact.location=location
                contact.location2=location2
                contact.email2=email2
                contact.email=email
                contact.phone2=phone2
                contact.phone=phone
                contact.save()
                messages.success(request, "Success!")
                return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))

    return render(request, "admin_templates/contact.html", context)


@login_required
def about(request):
    abt = About.objects.filter(id=1)
    if len(abt) > 0:
        context = {"about":abt.first()}
    else:
        context={}
    if request.method=="POST":
        bio = request.POST.get("bio")
        core_value = request.POST.get("corevalue")
        mission = request.POST.get("mission")
        vision = request.POST.get("vision")
        try:
            if len(abt) == 0:
                about = About(core_values=core_value, bio=bio, mission=mission, vision=vision)
                about.save()
                messages.success(request, "Success!")
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                about = About.objects.get(id=1)
                about.bio=bio
                about.core_values=core_value
                about.mission=mission
                about.vision=vision
                about.save()
                messages.success(request, "Success!")
                return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))

    return render(request, "admin_templates/about.html", context)


@login_required
def leads(request):
    leads = Messages.objects.all()
    context = {"leads":leads}
    return render(request, "admin_templates/leads.html", context)


@login_required
def lead_messages(request):
    messages = Messages.objects.all()
    context = {"messages":messages}
    return render(request, "admin_templates/messages.html", context)


@login_required
def view_list(request):
    lists = List.objects.all()
    context = {"lists":lists}
    return render(request, "admin_templates/List.html", context)



@login_required
def add_product(request):
    context = {}
    return render(request, "admin_templates/add_product.html", context)


@login_required
def add_product_save(request):
    if request.method=="POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category = request.POST.get("category")
        profile_pic = request.FILES["img"]
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            new_product = Product(name=name, description=description, price=price, category=category, image=profile_pic_url)
            new_product.save()
            messages.success(request, "Success!")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))


@login_required
def manage_products(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, "admin_templates/manage_products.html", context)


@login_required
def update_product(request, product_id):
    product = Product.objects.filter(id = product_id).first()
    context = {"product":product}
    return render(request, "admin_templates/update_product.html", context)


@login_required
def update_product_save(request):
    if request.method=="POST":
        product_id = request.POST.get("product_id")
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category = request.POST.get("category")
        try:
            product = Product.objects.filter(id = product_id).first()
            product.name = name
            product.description = description
            product.price = price
            product.category = category
            if request.POST.get("img") != "":
                profile_pic = request.FILES["img"]
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
                product.image = profile_pic_url
            product.save()
            messages.success(request, "Success!")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))


@login_required
def add_blog(request):
    context = {}
    return render(request, "admin_templates/add_blog.html", context)


@login_required
def add_blog_save(request):
    if request.method=="POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        profile_pic = request.FILES["img"]
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            new_blog = Blog(title=title, description=description, image=profile_pic_url)
            new_blog.save()
            messages.success(request, "Success!")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))


@login_required
def update_blog(request, blog_id):
    blog = Blog.objects.filter(id = blog_id).first()
    context = {"blog":blog}
    return render(request, "admin_templates/update_blog.html", context)


@login_required
def update_blog_save(request):
    if request.method=="POST":
        blog_id = request.POST.get("blog_id")
        title = request.POST.get("title")
        description = request.POST.get("description")
        try:
            blog = Blog.objects.filter(id = blog_id).first()
            blog.title = title
            blog.description = description
            if request.POST.get("img") != "":
                profile_pic = request.FILES["img"]
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
                blog.image = profile_pic_url
            blog.save()
            messages.success(request, "Success!")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Failed!")
            return redirect(request.META.get("HTTP_REFERER"))


@login_required
def manage_blogs(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request, "admin_templates/manage_blogs.html", context)


@login_required
def blog_comments(request):
    comments = BlogComment.objects.all()
    print(comments)
    context = {"comments":comments}
    return render(request, "admin_templates/blog_comments.html", context)
