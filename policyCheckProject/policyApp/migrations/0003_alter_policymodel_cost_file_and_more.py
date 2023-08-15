# Generated by Django 4.2.3 on 2023-08-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policyApp', '0002_remove_policymodel_policy_making_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policymodel',
            name='cost_file',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='policymodel',
            name='finance_file',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='policymodel',
            name='interventional_file',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='policymodel',
            name='justified_file',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='policymodel',
            name='practical_file',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='policymodel',
            name='redistributive_file',
            field=models.FileField(upload_to='documents/'),
        ),
    ]