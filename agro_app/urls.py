from django.urls import path,include
from . import farmer_views, views
urlpatterns = [
   path("",views.home,name="home"), 
   path("about/",views.about,name="about"), 
   path("contact/",views.contact,name="contact"),
   path("feedback/",views.feedback,name="feedback"),  
   path("login/",farmer_views.farmer_login,name="login"), 
   path("register/",farmer_views.register,name="register"),  
   path("protein_rich/",views.protein,name="protein"),  
   path("carbs_rich/",views.carbs,name="carbs"),  
   path("fats_rich/",views.fats,name="fats"),  
   path("home/",farmer_views.home,name="home"),  
   path("farmer_logout/",farmer_views.farmer_logout,name="farmer_logout"),  
   path("add_product/",farmer_views.add_product,name="add_product"),  
   path("view_products/",views.view_products,name="view_products"),  
   path("my_product/",farmer_views.my_product,name="my_product"),   
   path("seasonal_pro/",views.seasonal,name="seasonal"),  
   path("edit_profile/",farmer_views.edit_profile,name="edit_profile"),  
]
