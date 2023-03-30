from django.shortcuts import *
from .models import *
from django.contrib import messages
from App_admin.models import *


def store_home(request):
    products = Product.objects.all()
    context = {"products":products[:3]}
    return render(request, "app_store/index.html", context)


def about_us(request):
    about = About.objects.all().first()
    context = {"about":about}
    return render(request, "app_store/about.html", context)


def contact_us(request):
    contact = Contact.objects.all().first()
    context = {"contact":contact}
    return render(request, "app_store/contact.html", context)


def gallery(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, "app_store/gallery.html", context)


def faq(request):
    context = {}
    return render(request, "app_store/faq.html")


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request, "app_store/blog.html", context)


def lists(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            new_list = List(email=email)
            new_list.save()
            messages.success(request, "Mail Address Sent!")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Mail Not Sent!")
            return redirect(request.META.get("HTTP_REFERER"))


def message(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        number = request.POST.get("number")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        try:
            new_message = Messages(email=email, full_name=name, phone=number, message_sub=subject, message_text=message)
            new_message.save()
            messages.success(request, "Mesage Sent Success!")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Message Not Sent!")
            return redirect(request.META.get("HTTP_REFERER"))


def blog_details(request, blog_id):
    blog = Blog.objects.filter(id = blog_id).first()
    context = {"blog":blog}
    return render(request, "app_store/blog_details.html", context)


def blog_comment_save(request):
    if request.method == "POST":
        blog_id = request.POST.get("blog_id")
        comment = request.POST.get("comment")
        # try:
        blog = Blog.objects.filter(id = blog_id).first()
        new_comment = BlogComment(blog_id = blog, comment = comment)
        new_comment.save()
        messages.success(request, "Comment Success!")
        return redirect(request.META.get("HTTP_REFERER"))
        # except:
        #     messages.success(request, "Comment Failed!")
        #     return redirect(request.META.get("HTTP_REFERER"))
