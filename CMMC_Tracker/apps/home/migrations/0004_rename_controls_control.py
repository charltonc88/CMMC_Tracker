# Generated by Django 3.2.6 on 2022-03-31 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_organization_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Controls',
            new_name='Control',
        ),
    ]