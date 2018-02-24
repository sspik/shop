from django import template
from Shop.models import Catalog

register = template.Library()


@register.inclusion_tag('shop/top_menu.html', name='top_menu')
def show_top_menu():
    qs = Catalog.objects.filter(level=0)
    tree = {}
    for el in qs:
        sub_tree = {}
        for sub_el in el.get_children():
            sub_tree.update({sub_el: [i for i in sub_el.get_children()]})
        tree.update({el: sub_tree})

    return {'top_menu': sorted(tree.iteritems(), key=lambda (k, v): (k.tree_id, v))}
