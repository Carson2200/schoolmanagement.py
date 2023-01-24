# Generated by Django 4.1.5 on 2023-01-24 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stream_Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_Code', models.CharField(blank=True, max_length=4, null=True)),
                ('Subject_Name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='Student.jpg', null=True, upload_to='')),
                ('Stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seniorschool.stream')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seniorschool.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admission_no', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('Parent_phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='Student.jpg', null=True, upload_to='')),
                ('age', models.IntegerField(blank=True, default='0', null=True)),
                ('location', models.CharField(blank=True, max_length=300, null=True)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('Stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seniorschool.stream')),
            ],
        ),
    ]
