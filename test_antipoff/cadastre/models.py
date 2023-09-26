from django.db import models


MAX_LENGTH = 255


# Модель для сохранения запросов
class CadastreData(models.Model):
    cadastre_number = models.CharField(
        "Кадастровый номер",
        max_length=MAX_LENGTH,
        blank=False
    )
    latitude = models.FloatField(
        "Широта",
        blank=False
    )
    longitude = models.FloatField(
        "Долгота",
        blank=False
    )
    create_date = models.DateTimeField(
        "Дата создания",
        auto_now_add=True
    )

    class Meta:
        ordering = ("-create_date",)
        verbose_name = "Кадастровый номер"
        verbose_name_plural = "Кадастровые номера"

    def __str__(self):
        return self.cadastre_number


# Модель сохраняющая результат и запрос
class Result(models.Model):
    cadastre_number = models.ForeignKey(
        CadastreData,
        on_delete=models.CASCADE,
        verbose_name="Кадастровый номер",
        blank=False,
        null=True
    )
    result = models.BooleanField(
        "Результат",
        blank=False,
        null=True
    )

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"

    def __str__(self):
        return f"У {self.cadastre_number} результат {self.result}"
