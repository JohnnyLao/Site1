# Generated by Django 4.2.2 on 2023-11-12 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("banquets", "0018_banquet_subhalls"),
    ]

    operations = [
        migrations.AddField(
            model_name="subhall",
            name="hall_no",
            field=models.IntegerField(blank=True, null=True, verbose_name="№ Зала"),
        ),
    ]
