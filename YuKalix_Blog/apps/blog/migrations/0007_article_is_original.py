# Generated by Django 2.0 on 2019-02-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190222_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_original',
            field=models.BooleanField(default=False, verbose_name='原创'),
        ),
    ]