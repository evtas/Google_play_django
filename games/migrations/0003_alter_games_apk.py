# Generated by Django 4.0.5 on 2022-06-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_games_apk_alter_games_star_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='apk',
            field=models.FilePathField(),
        ),
    ]
