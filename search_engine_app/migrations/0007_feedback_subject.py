# Generated by Django 3.0.2 on 2020-03-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine_app', '0006_userportal_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='subject',
            field=models.CharField(default='dd', max_length=400),
            preserve_default=False,
        ),
    ]
