# Generated by Django 3.2.6 on 2022-04-06 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_controls_control'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='level',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='3', max_length=3),
        ),
        migrations.AlterField(
            model_name='organization',
            name='level',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='3', max_length=3),
        ),
    ]
