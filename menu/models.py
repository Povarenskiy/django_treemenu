from django.db import models


class Menu(models.Model):
    """Модель меню"""
    slug = models.SlugField()
    path = models.CharField(max_length=50, editable=False)

    def __str__(self):
        return f'Menu ({self.slug})'
    
    def save(self, *args, **kwargs):
        self.path = f'{self.slug}'
        return super().save(*args, **kwargs)


class MenuItem(models.Model):
    """Модель вкладки меню"""
    slug = models.SlugField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    path = models.CharField(max_length=250, editable=False)

    def save(self, *args, **kwargs):
        if not self.menu:
            self.menu = self.parent.menu
        parent_path = f'{self.menu.slug}' if not self.parent else f'{self.parent.path}'
        self.path = f'{parent_path}-{self.slug}'
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Item ({self.path})'
