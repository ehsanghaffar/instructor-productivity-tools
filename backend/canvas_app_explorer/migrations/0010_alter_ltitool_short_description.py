# Generated by Django 3.2.14 on 2022-07-21 20:26

import backend.canvas_app_explorer.models
from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas_app_explorer', '0009_auto_20220623_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ltitool',
            name='short_description',
            field=tinymce.models.HTMLField(validators=[backend.canvas_app_explorer.models.MaxLengthIgnoreHTMLValidator(limit_value=120)]),
        ),
    ]
