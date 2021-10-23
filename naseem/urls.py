from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from.forms import MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
from.views import BlockUserAPIView,UnblockUserAPIView,Index

urlpatterns = [

    path('blockuser',BlockUserAPIView.as_view(),name="blockuser"),
    path('unblockuser',UnblockUserAPIView.as_view(),name="unblockuser"),

    path('',views.Index.as_view(),name="home"),
    path('home',views.Index.as_view(),name="home"),
    path('profile',views.profile,name="profile"),
    path('login',views.login,name="login"),
    path('serializer',views.profile,name="serializer"),

    #path('forget_password',views.forget_password,name="forget_password"),
    path('logout',views.logout,name="logout"),
    path('register',views.register,name="register"),
    path('add_category',views.add_category,name="add_category"),
    path('edit_category/<str:id>',views.edit_category,name="edit_category"),
    path('update/<str:id>',views.update,name="update"),
    path('delete/<str:id>',views.delete,name="delete"),
    path('delete1/<str:id>',views.delete1,name="delete"),
    path('category_management',views.category_management,name="category_management"),
    path('user_management',views.user_management,name="user_management"),
   # path('change_password',(views.ChangePasswordView.as_view()),name='change_password'),
    #path('edit_category',(views.EditCategoryView.as_view()),name='edit_category'),
    #path('change_password',views.change_password,name="change_password"),
    path('edit_profile',views.edit_profile,name="edit_profile"),


    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='admin_panel/change_password.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name="passwordchange"),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='admin_panel/passwordchangedone.html'),name="passwordchangedone"),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='admin_panel/forget-password.html',form_class=MyPasswordResetForm),name="password_reset"),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='admin_panel/password_reset_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='admin_panel/password_reset_confirm.html',form_class=MySetPasswordForm),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='admin_panel/password_reset_complete.html'),name="password_reset_complete"),


    

]