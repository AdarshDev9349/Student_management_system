# Generated by Django 4.2 on 2023-04-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillhub', '0006_alter_person_dept_alter_person_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
    ]
