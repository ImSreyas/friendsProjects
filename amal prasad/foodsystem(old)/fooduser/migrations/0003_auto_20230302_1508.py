# Generated by Django 3.1.7 on 2023-03-02 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fooduser', '0002_uprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UProfile',
            new_name='HotProfile',
        ),
    ]