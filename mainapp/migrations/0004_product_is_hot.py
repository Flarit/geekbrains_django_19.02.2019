# Generated by Django 2.1.7 on 2019-03-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190301_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='является горячим продуктом?'),
        ),
    ]
