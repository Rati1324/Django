# Generated by Django 3.0.7 on 2020-07-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_edit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]