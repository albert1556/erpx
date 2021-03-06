# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='XfndFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_name', models.CharField(max_length=100, unique=True)),
                ('parameters', models.CharField(blank=True, max_length=240)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'xfnd_functions',
            },
        ),
        migrations.CreateModel(
            name='XfndFunctionExecLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execution_start_time', models.DateField()),
                ('execution_end_time', models.DateField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndFunction')),
            ],
            options={
                'db_table': 'xfnd_function_exec_logs',
            },
        ),
        migrations.CreateModel(
            name='XfndLoginLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_time', models.DateField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'xfnd_login_logs',
            },
        ),
        migrations.CreateModel(
            name='XfndMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=100, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'xfnd_menus',
            },
        ),
        migrations.CreateModel(
            name='XfndMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item_name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndFunction')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndMenu')),
            ],
            options={
                'db_table': 'xfnd_menu_items',
            },
        ),
        migrations.CreateModel(
            name='XfndProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodgram_type', models.CharField(max_length=10)),
                ('program_name', models.CharField(max_length=100, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'xfnd_programs',
            },
        ),
        migrations.CreateModel(
            name='XfndReportGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_group_name', models.CharField(max_length=100, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'xfnd_report_groups',
            },
        ),
        migrations.CreateModel(
            name='XfndReportGroupItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndFunction')),
                ('report_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndReportGroup')),
            ],
            options={
                'db_table': 'xfnd_report_group_items',
            },
        ),
        migrations.CreateModel(
            name='XfndResp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resp_name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndMenu')),
                ('report_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndReportGroup')),
            ],
            options={
                'db_table': 'xfnd_resps',
            },
        ),
        migrations.CreateModel(
            name='XfndUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=60, unique=True)),
                ('email', models.CharField(blank=True, max_length=60)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'xfnd_users',
            },
        ),
        migrations.CreateModel(
            name='XfndUserResp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DecimalField(decimal_places=0, max_digits=10)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('resp', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndResp')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndUser')),
            ],
            options={
                'db_table': 'xfnd_user_resps',
            },
        ),
        migrations.AddField(
            model_name='xfndloginlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndUser'),
        ),
        migrations.AddField(
            model_name='xfndfunctionexeclog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndUser'),
        ),
        migrations.AddField(
            model_name='xfndfunction',
            name='program_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xfnd.XfndProgram'),
        ),
        migrations.AlterUniqueTogether(
            name='xfnduserresp',
            unique_together=set([('user', 'resp')]),
        ),
        migrations.AlterUniqueTogether(
            name='xfndreportgroupitem',
            unique_together=set([('report', 'id')]),
        ),
    ]
