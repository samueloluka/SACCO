from django.db import models

class Member(models.Model):
    member_name = models.CharField(max_length = 24)
    gender = models.CharField(max_length = 10)
    address = models.CharField(max_length = 28)
    contact = models.CharField(max_length = 15)
    savings_balance = models.IntegerField()
    photo = models.ImageField(upload_to="photos/")
    def __str__(self):
        return f"{self.member_name}-{self.gender}-{self.address}-{self.contact}-{self.savings_balance}"

class Saving(models.Model):
    saving_date = models.DateField(auto_now = False)
    saving_year = models.DateField(auto_now = True)
    saving_month = models.DateField(auto_now = True)
    amount = models.IntegerField()
    member = models.ForeignKey(Member, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.saving_date}-{self.saving_year}-{self.saving_month}-{self.amount}-{self.member}"

class Loan(models.Model):
    loan_date = models.DateField(auto_now = False)
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    loan_amount = models.IntegerField()
    repay_period =models.IntegerField()
    repayment_amount  = models.IntegerField()
    issued_by = models.CharField(max_length = 24)

    def __str__(self):
        return f"{self.loan_date}-{self.member}-{self.loan_amount}-{self.repay_period}-{self.repayment_amount}-{self.issued_by}"

class Loan_Payment(models.Model):
    payment_date = models.DateField(auto_now = False)
    Loan = models.ForeignKey(Loan, on_delete = models.CASCADE)
    amount_paid = models.IntegerField()
    received_by = models.CharField(max_length = 24)

