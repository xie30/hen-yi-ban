# Generated by Django 3.1.1 on 2021-12-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_test', '0005_auto_20211129_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caselist',
            name='check_type',
        ),
        migrations.AddField(
            model_name='caselist',
            name='include',
            field=models.CharField(max_length=1024, null=True, verbose_name='前置config/test'),
        ),
        migrations.AlterField(
            model_name='caselist',
            name='check',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='caselist',
            name='params',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='caselist',
            name='re_header',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='caselist',
            name='url',
            field=models.CharField(max_length=3000),
        ),
    ]
