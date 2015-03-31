# -*- coding: utf-8 -*-

from django import template


register = template.Library()


@register.inclusion_tag('widget_1.html')
def show_widget_1(title):

    return {
        'title': title,
        'wrapper': 'wrapper_1.html',
    }


@register.inclusion_tag('widget_2.html')
def show_widget_2(title):
    return {
        'title': title,
        'wrapper': 'wrapper_2.html',
    }
