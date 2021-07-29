from django import template


register = template.Library()

@register.filter(name='get_list_value')
def get_list_value(lt):
    if not lt:
        return '--'
    return lt[0]