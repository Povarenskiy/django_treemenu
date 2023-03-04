# Generated by Django 4.1.7 on 2023-03-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menuitem_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.CharField(default=2, editable=False, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='url',
            field=models.CharField(default=1, editable=False, max_length=250),
            preserve_default=False,
        ),
    ]
