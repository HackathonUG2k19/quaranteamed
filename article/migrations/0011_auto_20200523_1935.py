# Generated by Django 2.0 on 2020-05-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_bid_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='deadline',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='value',
            field=models.IntegerField(default=None, null=True),
        ),
    ]