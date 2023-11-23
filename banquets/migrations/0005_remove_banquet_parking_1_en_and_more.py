# Generated by Django 4.2.2 on 2023-11-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("banquets", "0004_banquet_parking_1_en_banquet_parking_1_kk_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="banquet",
            name="parking_1_en",
        ),
        migrations.RemoveField(
            model_name="banquet",
            name="parking_1_kk",
        ),
        migrations.RemoveField(
            model_name="banquet",
            name="parking_1_ru",
        ),
        migrations.RemoveField(
            model_name="banquet",
            name="parking_2_en",
        ),
        migrations.RemoveField(
            model_name="banquet",
            name="parking_2_kk",
        ),
        migrations.RemoveField(
            model_name="banquet",
            name="parking_2_ru",
        ),
        migrations.AlterField(
            model_name="banquet",
            name="parking_1",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Охраняемая", "Охраняемая"),
                    ("Guarded", "Guarded"),
                    ("Қорғалған", "Қорғалған"),
                    ("Неохраняемая", "Неохраняемая"),
                    ("Unguarded", "Unguarded"),
                    ("Күзетсіз", "Күзетсіз"),
                ],
                default="Неохраняемая",
                max_length=256,
                null=True,
                verbose_name="Парковка: Охраняемая/Неохраняемая",
            ),
        ),
        migrations.AlterField(
            model_name="banquet",
            name="parking_2",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Платная", "Платная"),
                    ("Paid", "Paid"),
                    ("Ақылы", "Ақылы"),
                    ("Бесплатная", "Бесплатная"),
                    ("Free", "Free"),
                    ("Тегін", "Тегін"),
                ],
                default="Бесплатная",
                max_length=256,
                null=True,
                verbose_name="Парковка: Платная/Бесплатная",
            ),
        ),
    ]