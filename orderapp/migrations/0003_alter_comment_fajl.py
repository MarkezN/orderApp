# Generated by Django 3.2.5 on 2021-08-24 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_comment_fajl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='fajl',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='orderapp.pdfs'),
        ),
    ]
