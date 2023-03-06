from django import template
from menu.models import MenuItem
from django.utils.safestring import mark_safe


register = template.Library()

def _build_items_tree(slug):
    """
    Группирует вкладки меню по id родителя
    """
    items = list(MenuItem.objects.filter(menu__slug=slug).values())

    items_parent_connections = {}
    for item in items:
        parent_id = item.pop('parent_id')
        items_parent_connections.setdefault(parent_id, []).append(item)
    return items_parent_connections


def _build_items_inline(items, path, parent_id=None):
    """
    Рекурсивная функция для построения HTML макета вкладок меню всех уровней
    по указанному пути
    """
    inline_items = items.pop(parent_id, [])
    
    res = ''
    for item in inline_items:
        inline = _build_items_inline(items, path, item['id']) if item['slug'] in path else ''
        res += f'<li><a href="{item["path"]}">{item["slug"]}</a><ul>{inline}</ul></li>'
    return res
    

def _build_menu_inline(slug, path):
    """
    Функция строит вкладки меню, если путь ссылается на данное меню
    """
    if slug in path:
        items_tree = _build_items_tree(slug)
        return _build_items_inline(items_tree, path)
    else:
        return ''

def _build_menu(slug, path): 
    """
    Функция для построения HTML макета меню 
    """
    inline = _build_menu_inline(slug, path)  
    return f'<div><a href="/{slug}">{slug}</a><ul>{inline}</ul></div>'    


@register.simple_tag(takes_context=True)
def draw_menu(context, slug):
    path = context['request'].path[1:].split('-')
    return mark_safe(_build_menu(slug, path))