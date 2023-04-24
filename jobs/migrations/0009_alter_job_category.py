# Generated by Django 4.2 on 2023-04-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_job_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('1', 'Information technology'), ('2', 'Education'), ('3', 'Accounting'), ('4', 'Other')], default='1', max_length=3),
        ),
    ]
