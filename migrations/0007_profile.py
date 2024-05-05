# Generated by Django 3.2 on 2023-09-19 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_ment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='profile/avator.png', upload_to='')),
                ('birth_date', models.DateField(default='None')),
                ('region', models.CharField(default='', max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('country', models.CharField(default='Tanzania', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
