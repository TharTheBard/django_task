# Generated by Django 2.1.5 on 2019-02-07 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190208_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
