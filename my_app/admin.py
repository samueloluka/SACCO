from django.contrib import admin

from .models import Member, Saving, Loan, Loan_Payment

class MemberAdmin(admin.ModelAdmin):
    list_display = ("member_name", "gender", "address", "contact", "savings_balance")



class SavingAdmin(admin.ModelAdmin):
    list_display = ("saving_date", "saving_year", "saving_month", "amount", "member")



class LoanAdmin(admin.ModelAdmin):
    list_display = ("loan_date", "member", "loan_amount", "repay_period", "repayment_amount", "issued_by")

 

class Loan_PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_date", "Loan", "amount_paid", "received_by")
	 
	
	

admin.site.register(Member, MemberAdmin)
admin.site.register(Saving, SavingAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Loan_Payment, Loan_PaymentAdmin)
