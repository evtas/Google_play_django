# Generated by Django 4.0.5 on 2022-06-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_games_apk'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='genre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
