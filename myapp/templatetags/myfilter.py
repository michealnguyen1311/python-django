from django import template
from django.conf import settings

register = template.Library()

@register.filter
def make_range(number):
    return range(1, number + 1)
@register.filter
def make_index_paginattion(current_page, index):
    return settings.PAGINATE_BY * ( current_page - 1 ) + index
# @register.filter
# def make_index_pagination(current_page, index):
#     return settings.PAGINATE_BY * (current_page - 1)

# register = template.library()
# @register.filter
# def luy_thua(co_so,so_mu):
#     return co_so**so_mu
# @register.filter
# def make_range(number):
#     return range(1, number + 1 )
