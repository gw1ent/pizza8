# Generated by Django 4.1.3 on 2022-11-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='firstName',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phoneNumber',
            field=models.CharField(default=7, max_length=11),
        ),
        migrations.AddField(
            model_name='customuser',
            name='roleId',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='secondName',
            field=models.TextField(null=True),
        ),
    ]
