# Generated by Django 4.2.2 on 2023-11-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("banquets", "0005_remove_banquet_parking_1_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="banquet",
            name="parking_1_en",
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
        migrations.AddField(
            model_name="banquet",
            name="parking_1_kk",
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
        migrations.AddField(
            model_name="banquet",
            name="parking_1_ru",
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
        migrations.AddField(
            model_name="banquet",
            name="parking_2_en",
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
        migrations.AddField(
            model_name="banquet",
            name="parking_2_kk",
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
        migrations.AddField(
            model_name="banquet",
            name="parking_2_ru",
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
