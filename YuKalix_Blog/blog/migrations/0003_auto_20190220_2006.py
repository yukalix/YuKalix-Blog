# Generated by Django 2.0 on 2019-02-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190220_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='classify',
            field=models.CharField(choices=[('python', 'Python'), ('web', '前端'), ('diary', '日记')], max_length=10, verbose_name='文章分类'),
        ),
    ]
