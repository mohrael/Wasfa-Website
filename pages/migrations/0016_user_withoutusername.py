# Generated by Django 4.2.13 on 2024-05-23 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_withoutusername',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, null=True, unique=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
