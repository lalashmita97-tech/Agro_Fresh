from django.shortcuts import render,redirect
from .models import Contact,Feedback,Product,Farmer 
from django.contrib import messages

# Create your views here.

def view_products(request):
    if request.method=="GET":
        product_list= Product.objects.all() #select * from product
        context={
        "product_key":product_list
        }
        return render(request,"agro_app/html/view_products.html",context)
    
    if request.method=="POST":
        pro_category=request.POST["category"]
        product_list=Product.objects.filter(product_category= pro_category)
        
        context={
        "product_key":product_list
        }
        return render(request,"agro_app/html/view_products.html",context)
        




def home(request):
    feedback=Feedback.objects.all()
    
    Feedback_dict={

          "feedback_key":feedback  
    }
        
    return render(request,'agro_app/html/index.html',Feedback_dict)

def about(request):
    return render(request,'agro_app/html/about_us.html')

def contact(request):
    if request.method=="GET":
        return render(request,"agro_app/html/contact_us.html")
    if request.method=="POST":
        user_name=request.POST["name"]
        user_email=request.POST["email"]
        user_phone=request.POST["phone"]
        user_query=request.POST["query"]

        fam_obc=Contact(name=user_name,email=user_email,phone=user_phone,query=user_query)
        fam_obc.save()
        messages.success(request,"🤗thank you ")
        return redirect("contact")

def feedback(request):
    if request.method=="GET":
     return render(request,"agro_app/html/user_feedback.html")
    if request.method=="POST":
        user_name=request.POST["name"]
        user_email=request.POST["email"] 
        user_rating=request.POST["rating"]
        user_remarks=request.POST["remarks"]

        famer_obj=Feedback(name=user_name,email=user_email,rating=user_rating,remarks=user_remarks)
        famer_obj.save()
        messages.success(request,"🤗thank you ")
        return redirect("feedback")



def protein(request):
    return render(request,"agro_app/html/protein_rich.html")

def carbs(request):
    return render(request,"agro_app/html/carbs_rich.html")

def fats(request):
    return render(request,"agro_app/html/fats_rich.html")

def seasonal(request):
    return render(request,"agro_app/html/seasonal_pro.html")