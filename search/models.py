from django.db import models

# Create your models here.


class Ingredient(models.Model):
    CATEGORY_MEAT = ("MEAT", "육류")
    CATEGORY_FISH = ("FISH", "어류")
    CATEGORY_EGG = ("EGG", "난류")
    CATEGORY_MILK = ("MILK", "우유")
    CATEGORY_ETC = ("ETC", "기타")

    CATEGORY_SELECT = (
        CATEGORY_MEAT,
        CATEGORY_FISH,
        CATEGORY_EGG,
        CATEGORY_MILK,
        CATEGORY_ETC,
    )

    name = models.CharField(max_length=60)
    category = models.CharField(choices=CATEGORY_SELECT, max_length=4)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Ingredient_detail", kwargs={"pk": self.pk})