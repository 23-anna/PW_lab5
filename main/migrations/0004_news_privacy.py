# Generated by Django 4.0.4 on 2022-05-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_cathegory_category_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='privacy',
            field=models.BooleanField(default=False),
        ),
    ]
