"""
URL configuration for sacco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from my_app.views import index_view, saving_view, member_view, loan_view, loan_payment_view, add_member_view, add_saving_view, add_loan_view, add_loan_payment_view, edit_member_view, edit_saving_view, edit_loan_view, edit_loan_payment_view, delete_member_view, delete_saving_view, delete_loan_view, delete_loan_payment_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index_page'),
    path( 'saving', saving_view, name='saving.html'),
    path( 'member', member_view, name='member.html'),
    path( 'loan', loan_view, name='loan.html'),
    path( 'loan_payment', loan_payment_view, name='loan_payment.html'),
    path('add_member', add_member_view, name="add_member_page"),
    path('add_saving', add_saving_view, name="add_saving_page"),
    path('add_loan', add_loan_view, name="add_loan_page"),
    path('add_loan_payment', add_loan_payment_view, name="add_loan_payment_page"),
    path('edit_member/<int:member_id>/', edit_member_view, name="edit_member_page"),
    path('edit_saving/<int:saving_id>/', edit_saving_view, name="edit_saving_page"),
    path('edit_loan/<int:loan_id>/', edit_loan_view, name="edit_loan_page"),
    path('edit_loan_payment/<int:loan_payment_id>/', edit_loan_payment_view, name="edit_loan_payment_page"),
    path('delete_member/<int:member_id>/', delete_member_view, name="delete_member_page"),
    path('delete_saving/<int:saving_id>/', delete_saving_view, name="delete_saving_page"),
    path('delete_loan/<int:loan_id>/', delete_loan_view, name="delete_loan_page"),
    path('delete_loan_payment/<int:loan_payment_id>/', delete_loan_payment_view, name="delete_loan_payment_page"),
    



]
