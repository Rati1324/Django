# Generated by Django 3.0.7 on 2020-06-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_auto_20200630_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments_amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
