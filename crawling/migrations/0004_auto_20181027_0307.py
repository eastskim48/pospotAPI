# Generated by Django 2.1.2 on 2018-10-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0003_auto_20181027_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taglist',
            name='imgurls',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]