# Generated by Django 4.0.6 on 2022-07-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_page_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title']},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.SmallIntegerField(default=0),
        ),
    ]
