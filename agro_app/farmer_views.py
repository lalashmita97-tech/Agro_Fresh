from django.shortcuts import render,redirect
from .models import Farmer,Product
from django.contrib import messages


def edit_profile(request):
  if request.method=="GET":
    farmer_email=request.session["web_key"]
    farmer_obj=Farmer.objects.get(email=farmer_email)
    farmer_dict={ 
      "farmer_key":farmer_obj 
      } 
    return render(request,"agro_app/farmer/edit_profile.html",farmer_dict)
  if request.method=="POST":
   farmer_name=request.POST["name"]  
   farmer_phone=request.POST["phone"]  
   farmer_pic=request.FILES.get("profile_pic") 
   farmer_city=request.POST["city"]  
   farmer_address=request.POST["address"]
   farmer_email=request.session["web_key"]
   farmer_obj=Farmer.objects.get(email=farmer_email)
   if farmer_pic is not None:
    farmer_obj.profile_pic=farmer_pic
  farmer_obj.name=farmer_name  
  farmer_obj.phone=farmer_phone  
  farmer_obj.city=farmer_city  
  farmer_obj.address=farmer_address
  farmer_obj.save()
  messages.success(request,"Profile Updated Successfully😇")
  return redirect("home")  





def farmer_logout(request):
  request.session.flush()
  messages.success(request,"🤗 Successfully logged out!! 🤗")
  return redirect("login")

def home(request):
  ## fetching email from session to indentify the farmer
  if request.method=="GET":
    farmer_email=request.session["web_key"]
    farmer_obj=Farmer.objects.get(email=farmer_email) #it will return a single obejct
    ## sending from view to html(template) page
    # create a dictionary and bind the data with a key
    # send the dict with render fun() 
    farmer_dict={ "farmer_key":farmer_obj } 
 
  return render(request,"agro_app/farmer/farmer_home.html",farmer_dict)


def farmer_login(request):
    if request.method=="GET":
      return render(request,"agro_app/farmer/farmer_login.html")
    if request.method=="POST":
      user_email=request.POST["email"]
      user_password=request.POST["password"]

      farmer_list=Farmer.objects.filter(email=user_email,password=user_password)
      if len(farmer_list)>0:
        request.session["web_key"]=user_email #binding emial in a session to track user for multiple requests
    
        return redirect("home")
      else:
        messages.error(request,"😟Invalid Credentials😟")
        return redirect("login") 


def register(request):
  if request.method=="GET":
    return render(request,"agro_app/farmer/farmer_register.html") 
  if request.method=="POST":
    user_email=request.POST["email"] ##control name input feild
    user_password=request.POST["password"]
    user_name=request.POST["name"]
    user_phone=request.POST["phone"]
    user_city=request.POST["city"]
    user_address=request.POST["address"]
    user_pic=request.FILES["profile_pic"]

    #OR Mapping frameworks##
    ##create object of user model
    ##set values
    ## save obeject->it automatically stores values in table

    farmer_obj=Farmer(name=user_name,email=user_email,password=user_password,phone=user_phone,city=user_city,address=user_address,profile_pic=user_pic)
    farmer_obj.save()
    return redirect("login")


def add_product(request):
    if request.method=="GET":
      return render(request,"agro_app/farmer/add_product.html")
    if request.method=="POST":
      email = request.session["web_key"]
      farmer = Farmer.objects.get(email=email)
      product_category=request.POST["category"]
      product_name=request.POST["name"]
      product_price=request.POST["price"]
      product_pic=request.FILES["pic"] 

      pro_obj=Product(farmer=farmer,product_category=product_category,product_name=product_name,product_price=product_price,product_pic=product_pic)
      pro_obj.save()
      return redirect("add_product") 
    

def my_product(request):
  if request.method=="GET":
   farmer_email=request.session["web_key"]
   farmer_obj=Farmer.objects.get(email=farmer_email)

   Product_list=Product.objects.filter(farmer=farmer_obj)

   product_dict={
     "product_key":Product_list 
   }
   return render(request,"agro_app/farmer/my_product.html",product_dict)
  

     