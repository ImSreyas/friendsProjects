# Generated by Django 3.1.7 on 2023-03-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooduser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=250, null=True)),
                ('place', models.CharField(max_length=250, null=True)),
                ('adrss', models.CharField(max_length=250, null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('mobs', models.TextField(max_length=10)),
                ('hid', models.TextField(max_length=10)),
            ],
        ),
    ]
