# Generated by Django 5.1 on 2024-08-09 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icard', '0002_remove_person_current_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='current_company',
            field=models.CharField(default='none', max_length=15),
        ),
    ]
