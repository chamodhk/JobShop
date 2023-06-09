# Generated by Django 4.2 on 2023-04-24 15:26

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('jobs', '0006_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('1', 'Information technology'), ('2', 'Education'), ('3', 'Accounting'), ('4', 'Other')], default='Education', max_length=60),
        ),
    ]
