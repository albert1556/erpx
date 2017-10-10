# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class XfndUser(models.Model):
    user_name = models.CharField(unique=True, max_length=60)
    email = models.CharField(max_length=60, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return self.user_name
        
    class Meta:
        db_table = 'xfnd_users'


class XfndProgram(models.Model):
    program_type = models.CharField(max_length=10)
    program_name = models.CharField(unique=True, max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return self.program_type + self.program_name
        
    class Meta:
        db_table = 'xfnd_programs'


class XfndFunction(models.Model):
    function_name = models.CharField(unique=True, max_length=100)
    program_id = models.ForeignKey(XfndProgram, models.DO_NOTHING)
    parameters = models.CharField(max_length=240, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return self.function_name
        
    class Meta:
        db_table = 'xfnd_functions'


class XfndMenu(models.Model):
    menu_name = models.CharField(unique=True, max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return self.menu_name
        
    class Meta:
        db_table = 'xfnd_menus'


class XfndMenuItem(models.Model):
    menu = models.ForeignKey('XfndMenu', models.DO_NOTHING)
    menu_item_name = models.CharField(max_length=100)
    function = models.ForeignKey(XfndFunction, models.DO_NOTHING)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return self.menu_item_name;
        
    class Meta:
        db_table = 'xfnd_menu_items'


class XfndReportGroup(models.Model):
    report_group_name = models.CharField(unique=True, max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return self.report_group_name
        
    class Meta:
        db_table = 'xfnd_report_groups'


class XfndReportGroupItem(models.Model):
    report_group = models.ForeignKey('XfndReportGroup', models.DO_NOTHING)
    report = models.ForeignKey(XfndFunction, models.DO_NOTHING)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return 'TODO - XfndReportGroupItem'
        
    class Meta:
        db_table = 'xfnd_report_group_items'
        unique_together = (('report', 'id'),)


class XfndResp(models.Model):
    resp_name = models.CharField(max_length=100, blank=False)
    menu = models.ForeignKey(XfndMenu, models.DO_NOTHING)
    report_group = models.ForeignKey(XfndReportGroup, models.DO_NOTHING)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return self.resp_name
        
    class Meta:
        db_table = 'xfnd_resps'


class XfndUserResp(models.Model):
    user = models.ForeignKey('XfndUser', models.DO_NOTHING)
    resp = models.ForeignKey(XfndResp, models.DO_NOTHING)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return 'TODO - XfndUserResp'
        
    class Meta:
        db_table = 'xfnd_user_resps'
        unique_together = (('user', 'resp'),)


class XfndLoginLog(models.Model):
    user = models.ForeignKey('XfndUser', models.DO_NOTHING)
    login_time = models.DateField()
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return 'TODO - XfndLoginLog'
        
    class Meta:
        db_table = 'xfnd_login_logs'


class XfndFunctionExecLog(models.Model):
    user = models.ForeignKey('XfndUser', models.DO_NOTHING)
    function = models.ForeignKey('XfndFunction', models.DO_NOTHING)
    execution_start_time = models.DateField()
    execution_end_time = models.DateField(blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    update_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return 'TODO - XfndFunctionExecLog'
        
    class Meta:
        db_table = 'xfnd_function_exec_logs'

        
