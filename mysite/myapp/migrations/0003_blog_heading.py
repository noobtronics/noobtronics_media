# Generated by Django 2.2.11 on 2020-04-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200405_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='heading',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
