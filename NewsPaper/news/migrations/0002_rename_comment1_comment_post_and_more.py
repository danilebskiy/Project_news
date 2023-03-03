# Generated by Django 4.1.7 on 2023-03-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment1',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment2',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating_comment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_text',
            field=models.CharField(max_length=5000),
        ),
    ]