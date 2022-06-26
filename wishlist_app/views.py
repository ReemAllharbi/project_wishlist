from django.http import HttpResponse
from django.shortcuts import render, redirect
from wishlist_app.models import User, Wishlist
import bcrypt
from django.contrib import messages


def index(request):
    return render(request, "index.html")

def registration(request):
     if request.method=="POST":
          errors = User.objects.basic_validator(request.POST)
          if len(errors) > 0:
              for key , value in errors.items():
                  messages.error(request, value)
              return redirect("/")
          else:
            name = request.POST["name"]
            username = request.POST["username"]
            password = request.POST["password"]
            confirm_password = request.POST["confirm_password"]
            datehired = request.POST["datehired"] 

            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(password.encode(), salt)
    
            user = User()
            user.name = name
            user.username = username
            user.datehired = datehired
            user.password = hash.decode()
            user.save()
            request.session['userId']=user.id
            return redirect("/dashboard")
     return render(request,"index.html")


def login(request):
    if request.method=="POST":
        errors_login_validator = User.objects.login_validator(request.POST)
        if len(errors_login_validator) > 0:
            for key , value in errors_login_validator.items():
                messages.error(request, value)
            return redirect ("/")
        
        username = request.POST["username-login"]
        password = request.POST["password-login"]
        
        try:
          user = User.objects.get(username=username)
          if bcrypt.checkpw(password.encode(), user.password.encode()):
              request.session['userId']=user.id
              return redirect("/dashboard")
          else:
            return render(request,"index.html")
        except User.DoesNotExist:
          return render(request,"index.html")


def dashboard(request):
    if "userId" not in request.session:
        return HttpResponse("Please authenticate first")
    else:
        select_user = User.objects.get(id=request.session['userId'])
        withlists = select_user.users.all()
        fiv = select_user.fav_item.all()
        withlist_not_include = Wishlist.objects.exclude(added_by=select_user).exclude(id__in=fiv)
        context = {
        "user": select_user,
        "withlists": fiv,
       "withlist_not_include": withlist_not_include
        
        }
        return render(request,"dashboard.html",context)

def create_wish(request):
      if request.method=="POST":

        errors = User.objects.basic_validator_item(request.POST)
        if len(errors) > 0:
            for key , value in errors.items():
                messages.error(request, value)
            return redirect ("/wish_items")
        else:
          select_user = User.objects.get(id=request.session['userId'])
          item = request.POST["item_add"]
          selected_wishlist=  Wishlist.objects.create(item=item,added_by=select_user)
          select_user.fav_item.add(selected_wishlist)
          messages.success(request,"Successfully Added!")
          return redirect("/wish_items")
      return render(request,'create_wish.html')


def view_wishlist(request, wishlist_id):
    selected_wishlist=Wishlist.objects.get(id=wishlist_id)
    context = {
        "selected_wishlist": selected_wishlist,
      }
    return render(request,'viewlist.html',context) 




def remove(request,wishlist_id):
    selected_wishlist=Wishlist.objects.get(id=wishlist_id)
    select_user = User.objects.get(id=request.session['userId'])
    select_user.fav_item.remove(selected_wishlist)
    return redirect("/dashboard")


def delete(request, wishlist_id):
    selected_wishlist=Wishlist.objects.get(id=wishlist_id)
    selected_wishlist.delete()
    return redirect("/dashboard")


def add_to(request, wishlist_id):
    select_user = User.objects.get(id=request.session['userId'])
    selected_wishlist=Wishlist.objects.get(id=wishlist_id)
    select_user.fav_item.add(selected_wishlist)
    select_user.save()
    return redirect("/dashboard")

   

def logout(request):
    del request.session['userId']
    return redirect("/")



