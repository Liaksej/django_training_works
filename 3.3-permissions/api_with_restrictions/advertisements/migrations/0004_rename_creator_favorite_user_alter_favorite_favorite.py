# Generated by Django 4.1.3 on 2022-11-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0003_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='creator',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='favorite',
            field=models.BooleanField(),
        ),
    ]
