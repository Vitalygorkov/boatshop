# Generated by Django 4.1.2 on 2022-12-04 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryblog',
            old_name='title',
            new_name='name',
        ),
    ]
