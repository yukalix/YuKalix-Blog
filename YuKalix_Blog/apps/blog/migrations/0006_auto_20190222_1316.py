# Generated by Django 2.0 on 2019-02-22 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_recommend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='recommend',
            new_name='is_recommend',
        ),
    ]