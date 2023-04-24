# Generated by Django 4.2 on 2023-04-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('IT', 'Information technology')], default='IT', max_length=2),
            preserve_default=False,
        ),
    ]
