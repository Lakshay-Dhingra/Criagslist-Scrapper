# Generated by Django 3.1.1 on 2020-10-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'Searches'},
        ),
        migrations.AddField(
            model_name='search',
            name='city',
            field=models.CharField(default='Delhi', max_length=50),
            preserve_default=False,
        ),
    ]
