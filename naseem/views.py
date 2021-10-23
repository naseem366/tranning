from django.shortcuts import render,redirect
from .models import Category, Customer, customer
from django.http import HttpResponse, request 
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CustomerForm,CategoryForm
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.
#def change_password(request):


#def index(request):
    #return render(request,'admin_panel/index.html')
class Index(View):
    def get(self, request):
        users = User.objects.all().count()
        Authors = Customer.objects.all()
        total_Author = Authors.count()
        user = request.user
    
        context = {
            'users':users,
            'user':user,
            'total_podcaster':total_Author,
            'podcasters':Authors,
        }
        return render(request, 'admin_panel/index.html', context)


@login_required(login_url='login')
def profile(request):
    return render(request,'admin_panel/profile.html')
@login_required(login_url='login')

def add_category(request):
	if request.method=="POST":
		name=request.POST['name']
		ins=Category(name=name)
		ins.save()
		return redirect('category_management')
	else:
		return render(request,'admin_panel/add-category.html')

@login_required(login_url='login')
def edit_category(request,id):
	#category=request.category
	form=Category.objects.get(id=id)
	return render(request,'admin_panel/edit-category.html',{'form':form})

@login_required(login_url='login')
def update(request, id):  
    employee = Category.objects.get(id=id)  
    form = CategoryForm(request.POST,instance=employee)  
    if form.is_valid():  
        form.save()  
        return redirect("category_management")  
    return render(request, 'admin_panel/edit-category.html', {'employee': employee})

#def update(request, id):
#	employee = Category.objects.get(id=id)
#	form=CategoryForm(request.POST,instance=employee)
#	if form.is_valid():
#		form.save()
 #       return redirect("category_management")
#	return render(request, 'admin_panel/edit-category.html', {'employee': employee})

#	employee = Category.objects.get(id=id)  
#	if request.method=="POST":
#		name=request.POST and instance=employee
#		ins=Category(name=name)
#		ins.save()
#		return redirect('category_management')
#	else:
#		return render(request,'admin_panel/add-category.html')
    
@login_required(login_url='login')
def delete(request,id):  
    form = Category.objects.get(id=id)  
    form.delete()  
    return redirect("category_management")
@login_required(login_url='login')
def delete1(request,id):  
    form = User.objects.get(id=id) 
    form.delete() 
    return redirect("user_management")

@login_required(login_url='login')
def category_management(request):
	form=Category.objects.all()
	
	context={
		'form':form
		
	}
	return render(request,'admin_panel/category-management.html',context)

@login_required(login_url='login')
def user_management(request):
	form=User.objects.all()
	customer=Customer.objects.all()
	context={
		'form':form,
		'customer':customer
	}
	return render(request,'admin_panel/user-management.html',context)


@login_required(login_url='login')
def edit_profile(request):
	customer=request.user.customer
	#user=request.user
	#form1=CreateUserForm(instance=user)
	form=CustomerForm(instance=customer)
	if request.method == 'POST':
		form=CustomerForm(request.POST,request.FILES,instance=customer)
		#form1=CreateUserForm(request.POST,instance=user)
		if form.is_valid():
			form.save()

			return redirect('profile')
	context={
		'form':form
	}

	return render(request,'admin_panel/edit-profile.html',context)


def register(request):
	form=CreateUserForm()
	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,'Account was created for ' +user)
			return redirect('login')
	context={'form':form}
	return render(request,'admin_panel/register.html',context)
	
def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,"invalid credentials")
			return redirect('login')
	else:

		return render(request,'admin_panel/login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.status import (
                                        HTTP_200_OK,
                                    	HTTP_400_BAD_REQUEST,
                                    	HTTP_204_NO_CONTENT,
                                    	HTTP_201_CREATED,
                                    	HTTP_500_INTERNAL_SERVER_ERROR,
                                        HTTP_404_NOT_FOUND,
                                        
                                    ) 
from .serializers import *
from .models import *


class BlockUserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        user_id = self.kwargs['pk']
        try:
            user=User.objects.get(id=user_id)
        except:
            return Response({
                'success':'False',
                'message':'No user to block'
                },status=HTTP_400_BAD_REQUEST)

        if user.is_active == True:
            user.is_active = False
            user.save()
            return Response({
                        'success':'True',
                        'message':'User blocked successfully'
                        },status=HTTP_200_OK)
        else:
            return Response({
                        'success':'False',
                        'message':'Already Blocked'
                        },status=HTTP_400_BAD_REQUEST)

class UnblockUserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        user_id = self.kwargs['pk']
        try:
            user=User.objects.get(id=user_id)
        except:
            return Response({
                'success':'False', 
                'message':'No user to unblock'
                },status=HTTP_400_BAD_REQUEST)
                
        if user.is_active == False:
            user.is_active = True
            user.save()
            return Response({
                        'success':'True',
                        'message':'User unblocked successfully'
                        },status=HTTP_200_OK)
        else:
            return Response({
                        'success':'False',
                        'message':'Already unblocked'
                        },status=HTTP_400_BAD_REQUEST)


class UserProfileDetailsAPIView(APIView):
    def get(self,request,*args,**kwargs):
        user_id =  self.kwargs['pk']
        
        try:
            obj = UserOtherInfo.objects.get(user__id=user_id)
        except:
            return Response({
                'success' : 'False',
                'message' : 'No user found',
            },status=HTTP_404_NOT_FOUND)

        serializer = UserDetailsSerializer(obj)
        data = serializer.data  
        return Response({
            'success'  :'True',
            'message'  : 'Data retrieved successfully',
            'data'     : data  
        },status=HTTP_200_OK)


class DeleteUserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        
        user_id = self.kwargs['pk']
        print('user_id',user_id)
        try:
            obj = User.objects.get(id=user_id)
        except:
            return Response({
                'success' : 'False',
                'message' :'No user to delete'
                },status=HTTP_400_BAD_REQUEST)

        obj.delete()
        return Response({
            'success' : 'True',
            'message' : 'User deleted successfully',
        },status=HTTP_200_OK)



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer


@api_view(['GET', 'POST'])
def customer_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Customer.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
