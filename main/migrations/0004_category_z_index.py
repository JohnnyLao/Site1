# Generated by Django 4.2.2 on 2023-08-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_category_options_category_name_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="z_index",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Порядковый №"
            ),
        ),
    ]