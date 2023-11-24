from django.forms import ModelForm

from my_app.models import Member, Saving, Loan, Loan_Payment


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class SavingForm(ModelForm):
    class Meta:
        model = Saving
        fields = '__all__'


class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'


class Loan_PaymentForm(ModelForm):
    class Meta:
        model = Loan_Payment
        fields = '__all__'


