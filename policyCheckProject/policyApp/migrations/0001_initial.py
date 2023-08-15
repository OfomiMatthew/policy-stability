# Generated by Django 4.2.3 on 2023-07-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_making_process', models.CharField(choices=[('Sensemaking', 'sensemaking'), ('option2', 'Option 2'), ('option3', 'Option 3')], default='', max_length=20)),
                ('user_name', models.CharField(max_length=100)),
                ('justified_yes', models.BooleanField(default=False)),
                ('justified_no', models.BooleanField(default=False)),
                ('justified_comment', models.TextField()),
                ('justified_file', models.FileField(upload_to='')),
                ('redistributive_yes', models.BooleanField(default=False)),
                ('redistributive_no', models.BooleanField(default=False)),
                ('redistributive_comment', models.TextField()),
                ('redistributive_file', models.FileField(upload_to='')),
                ('practical_yes', models.BooleanField(default=False)),
                ('practical_no', models.BooleanField(default=False)),
                ('practical_comment', models.TextField()),
                ('practical_file', models.FileField(upload_to='')),
                ('interventional_yes', models.BooleanField(default=False)),
                ('interventional_no', models.BooleanField(default=False)),
                ('interventional_comment', models.TextField()),
                ('interventional_file', models.FileField(upload_to='')),
                ('cost_yes', models.BooleanField(default=False)),
                ('cost_no', models.BooleanField(default=False)),
                ('cost_comment', models.TextField()),
                ('cost_file', models.FileField(upload_to='')),
                ('finance_yes', models.BooleanField(default=False)),
                ('finance_no', models.BooleanField(default=False)),
                ('finance_comment', models.TextField()),
                ('finance_file', models.FileField(upload_to='')),
            ],
        ),
    ]
