from django.shortcuts import render, redirect

from my_app.forms import MemberForm, SavingForm, LoanForm, Loan_PaymentForm
from my_app.models import Member, Saving, Loan, Loan_Payment

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def index_view(request):
        return render(request, 'index.html')

def saving_view(request):
        return render(request, 'saving.html')

def member_view(request):
        return render(request, 'member.html')

def loan_view(request):
        return render(request, 'loan.html')

def loan_payment_view(request):
        return render(request, 'loan_payment.html')
@login_required
def add_member_view(request):
        message=''
        if request.method == "POST":
                member_form = MemberForm(request.POST)

                if member_form.is_valid():
                        member_form.save()

                        messages.success(request, "Member Added Successfully")
                       

       
        member_form = MemberForm()

        members = Member.objects.all()

        context = {

                'form':member_form,
                'msg':message,
                'members':members
        }
        return render(request, "add_member.html", context)
@login_required
def add_saving_view(request):
        message=''
        if request.method == "POST":
                saving_form = SavingForm(request.POST)

                if saving_form.is_valid():
                        saving_form.save()

                        messages.success(request, "Saving Added Successfully")
                       

       
        saving_form = SavingForm()

        savings = Saving.objects.all()

        context = {

                'form':saving_form,
                'msg':message,
                'savings':savings
        }
        return render(request, "add_saving.html", context)
@login_required
def add_loan_view(request):
        message=''
        if request.method == "POST":
                loan_form = LoanForm(request.POST)

                if loan_form.is_valid():
                        loan_form.save()

                        messages.success(request, "Loan Added Successfully")
                       

        
        loan_form = LoanForm()

        loans = Loan.objects.all()

        context = {

                'form':loan_form,
                'msg':message,
                'loans':loans
        }
        return render(request, "add_loan.html", context)
@login_required
def add_loan_payment_view(request):
        message=''
        if request.method == "POST":
                loan_payment_form = Loan_PaymentForm(request.POST)

                if loan_payment_form.is_valid():
                        loan_payment_form.save()

                        messages.success(request, "Loan Payment Added Successfully")
                        
                        
                        


        
        loan_payment_form = Loan_PaymentForm()

        loan_payments = Loan_Payment.objects.all()

        context = {

                'form':loan_payment_form,
                'msg':message,
                'loan_payments':loan_payments
        }
        return render(request, "add_loan_payment.html", context)

@login_required
def edit_member_view(request, member_id):
        message=''
        member = Member.objects.get(id=member_id)

        if request.method =="POST":
                member_form = MemberForm( request.POST,instance=member)

                if member_form.is_valid():
                        member_form.save()
                        messages.success(request, "Member Edited Successfully")
                        return redirect(add_member_view)

                else:
                        message= "Form has invalid data"

        else:
                member_form = MemberForm( instance = member)

        context ={
                'form':member_form,
                'member':member,
                'message':message
                
        }

        return render(request, 'edit_member.html', context)
        
@login_required
def edit_saving_view(request, saving_id):
        message=''
        saving = Saving.objects.get(id=saving_id)

        if request.method =="POST":
                saving_form = SavingForm(request.POST, instance=saving)

                if saving_form.is_valid():
                        saving_form.save()
                        messages.success(request, "Saving Edited Successfully")
                        return redirect(add_saving_view)

                else:
                        message= "Form has invalid data"

        else:
                saving_form = SavingForm( instance = saving)

        context ={
                'form':saving_form,
                'saving':saving,
                'message':message
        }

        return render(request, 'edit_saving.html', context)

@login_required
def edit_loan_view(request, loan_id):
        message = ''
        loan = Loan.objects.get(id=loan_id)

        if request.method =="POST":
                loan_form = LoanForm(request.POST, instance=loan)

                if loan_form.is_valid():
                        loan_form.save()
                        messages.success(request, "Loan Edited Successfully")
                        return redirect(add_loan_view)

                else:
                        message= "Form has invalid data"

        else:
                loan_form = LoanForm( instance = loan)

        context ={
                'form':loan_form,
                'loan':loan,
                'message':message
        }

        return render(request, 'edit_loan.html', context)
@login_required        
def edit_loan_payment_view(request, loan_payment_id):
        message=''
        loan_payment = Loan_Payment.objects.get(id=loan_payment_id)

        if request.method =="POST":
                loan_payment_form = Loan_PaymentForm(request.POST, instance=loan_payment)

                if loan_payment_form.is_valid():
                        loan_payment_form.save()
                        messages.success(request, "Loan Payment Edited Successfully")
                        return redirect(add_loan_payment_view)

                else:
                        message= "Form has invalid data"

        else:
                loan_payment_form = Loan_PaymentForm( instance = loan_payment)

        context ={
                'form':loan_payment_form,
                'loan_payment':loan_payment,
                'message':message
        }

        return render(request, 'edit_loan_payment.html', context)
        
@login_required
def delete_member_view(request, member_id):
        member = Member.objects.get(id=member_id)

        member.delete()

        return redirect(add_member_view)
@login_required
def delete_saving_view(request, saving_id):
        saving = Saving.objects.get(id=saving_id)

        saving.delete()

        return redirect(add_saving_view)
@login_required
def delete_loan_view(request, loan_id):
        loan = Loan.objects.get(id=loan_id)

        loan.delete()

        return redirect(add_loan_view)
@login_required
def delete_loan_payment_view(request, loan_payment_id):
        loan_payment = Loan_Payment.objects.get(id=loan_payment_id)

        loan_payment.delete()

        return redirect(add_loan_payment_view)


def sign_up_view(request):
        if request.method=="POST":
                sign_up_form=UserCreationForm(request.POST)
                if sign_up_form.is_valid():
                        sign_up_form.save()

                        message="User Created Successfully"

                else:
                        message="Something went wrong"

        else:
                sign_up_form=UserCreationForm()

        context={
        'form':sign_up_form
        }

        return render(request, 'registration/sign_up.html', context)