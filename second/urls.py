"""
URL configuration for second project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),  # Include URLs from the home app
    path('addproduct/', addProduct, name="add_product"),  # Add product view
    path('edit/<int:id>', editProduct, name="edit_product"),  # Edit product view
    path('delete/<str:id>', deleteProduct, name="delete_product"),  # Delete product view
    path('signup/', signUpUser, name="signup_user"),  # User signup view
    path('login/', signInUser, name="login_user"),  # User login view
    path('logout/', signOutUser, name="logout_user"),  # User logout view
    path('about/', about, name="about"),  # About page view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files in development
