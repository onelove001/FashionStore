
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from App_store.views import *
from App_admin.views import *

urlpatterns = [

    # Store
    path('admin/', admin.site.urls),
    path('', store_home, name="store_home"),
    path('contact_us', contact_us, name="contact_us"),
    path('about_us', about_us, name="about_us"),
    path('gallery', gallery, name="gallery"),
    path('faq', faq, name="faq"),
    path('blog', blog, name="blog"),
    path('blog_details/<blog_id>', blog_details, name="blog_details"),
    path('blog_comment_save', blog_comment_save, name="blog_comment_save"),
    path('message', message, name="message"),
    path('blog_comments', blog_comments, name="blog_comments"),

    # Admin
    path('adminn', admin_dashboard, name="admin_dashboard"),
    path('login', login, name="login"),
    path('login_user', login_user, name="login_user"),
    path('logout', logout, name="logout"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('leads', leads, name="leads"),
    path('lists', lists, name="lists"),
    path('view_list', view_list, name="view_list"),
    path('lead_messages', lead_messages, name="lead_messages"),
    path('add_product', add_product, name="add_product"),
    path('add_product_save', add_product_save, name="add_product_save"),
    path('update_product/<product_id>/', update_product, name="update_product"),
    path('update_product_save', update_product_save, name="update_product_save"),
    path('manage_products', manage_products, name="manage_products"),
    path('add_blog', add_blog, name="add_blog"),
    path('add_blog_save', add_blog_save, name="add_blog_save"),
    path('update_blog/<blog_id>/', update_blog, name="update_blog"),
    path('update_blog_save', update_blog_save, name="update_blog_save"),
    path('manage_blogs', manage_blogs, name="manage_blogs"),

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
