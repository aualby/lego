from django.db import models


class Employees(models.Model):
    em_first_name = models.CharField('First Name', max_length=200)
    em_last_name = models.CharField('Last Name', max_length=200)
    em_employee_num = models.CharField('Employee Number', max_length=30)
    em_phone = models.CharField('Phone', max_length=15)
    em_email = models.EmailField('Email')

    class Meta:
        verbose_name_plural = 'Employees'
        ordering = ('em_last_name', 'em_first_name',)

    def __str__(self):
        return '{} {}'.format(self.em_first_name, self.em_last_name)


class Projects(models.Model):
    pr_name = models.CharField('Project Name', max_length=150)
    pr_number = models.CharField('Project Number', max_length=20)
    pr_created_by = models.ForeignKey(Employees, on_delete=models.PROTECT, verbose_name='Created By', related_name='created_by')
    pr_created = models.DateTimeField('Date Created')
    pr_address = models.CharField('Project Address', max_length=255)
    pr_manager = models.ForeignKey(Employees, on_delete=models.PROTECT, verbose_name='Project Manager', related_name='project_manager')
    pr_contract_contact = models.CharField('Project Contract Contact', max_length=200)
    pr_contract_phone = models.CharField('Project Contract Contact Phone', max_length=15)
    pr_fortec_site_contact = models.ForeignKey(Employees, on_delete=models.PROTECT, verbose_name='Fortec Site Contact',
                                               related_name='fortec_site_contact')

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ('pr_name',)

    def __str__(self):
        return self.pr_name
