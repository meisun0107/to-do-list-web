# Generated by Django 4.0.4 on 2022-05-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]