# Generated by Django 4.1 on 2022-09-03 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('em_first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('em_last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('em_employee_num', models.CharField(max_length=30, verbose_name='Employee Number')),
                ('em_phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('em_email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'ordering': ('em_last_name', 'em_first_name'),
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_name', models.CharField(max_length=150, verbose_name='Project Name')),
                ('pr_number', models.CharField(max_length=20, verbose_name='Project Number')),
                ('pr_created', models.DateTimeField(verbose_name='Date Created')),
                ('pr_address', models.CharField(max_length=255, verbose_name='Project Address')),
                ('pr_contract_contact', models.CharField(max_length=200, verbose_name='Project Contract Contact')),
                ('pr_contract_phone', models.CharField(max_length=15, verbose_name='Project Contract Contact Phone')),
                ('pr_created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_by', to='modalFBV.employees', verbose_name='Created By')),
                ('pr_fortec_site_contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fortec_site_contact', to='modalFBV.employees', verbose_name='Fortec Site Contact')),
                ('pr_manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_manager', to='modalFBV.employees', verbose_name='Project Manager')),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ('pr_name',),
            },
        ),
    ]