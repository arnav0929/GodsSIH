# Generated by Django 4.1 on 2022-08-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_title', models.CharField(max_length=300)),
                ('Description', models.CharField(max_length=300)),
                ('skills_req', models.CharField(max_length=300)),
            ],
        ),
    ]
