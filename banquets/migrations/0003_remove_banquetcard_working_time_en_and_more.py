# Generated by Django 4.2.2 on 2023-11-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("banquets", "0002_banquetcard_photo1_banquetcard_photo2_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="banquetcard",
            name="working_time_en",
        ),
        migrations.RemoveField(
            model_name="banquetcard",
            name="working_time_kk",
        ),
        migrations.RemoveField(
            model_name="banquetcard",
            name="working_time_ru",
        ),
        migrations.AlterField(
            model_name="banquetcard",
            name="url_name",
            field=models.CharField(
                max_length=30, unique=True, verbose_name="/url=client url"
            ),
        ),
    ]
