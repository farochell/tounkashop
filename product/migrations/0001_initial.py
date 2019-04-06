# Generated by Django 3.0.dev20190330204916 on 2019-03-31 21:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]