# Generated by Django 4.2.6 on 2023-11-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_loan_repay_period_loan_repayment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(default=0, upload_to='photos/'),
            preserve_default=False,
        ),
    ]
