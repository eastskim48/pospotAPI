# Generated by Django 2.1.2 on 2018-10-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taglist',
            name='imgurls',
            field=models.CharField(default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='taglist',
            name='tag_name',
            field=models.CharField(max_length=20),
        ),
    ]
