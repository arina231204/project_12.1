# Generated by Django 3.2 on 2023-01-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='answer',
            field=models.TextField(blank=True, default=0, null=True),
        ),
    ]
