from django.db import models

from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=20, verbose_name=_("Name"))
    # 하위 카테고리를 등록하면, 상위 카테고리 모두 등록된 것으로 판단한다.
    parent_category = models.IntegerField(blank=True, verbose_name=_("Parent Category"))
    category = models.ForeignKey(
        to="Category",
        verbose_name=_("Categories"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="categories",
    )

    class Meta:
        db_table = "category"
        verbose_name = _("Category")
        verbose_name_plural = f'{verbose_name} {_("List")}'
        ordering = ["-id"]

    def __str__(self):
        return f"Category(pk={self.pk}, name={self.name})"
