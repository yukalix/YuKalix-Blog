# Generated by Django 2.0 on 2019-02-20 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190219_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageUserPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_photo', models.ImageField(upload_to='message/users/%Y/%m/%d', verbose_name='用户头像')),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='user_photo',
            field=models.URLField(verbose_name='用户头像'),
        ),
    ]
