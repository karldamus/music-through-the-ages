from django_component import Library, Component

register = Library()

@register.component
class Card(Component):
    template = "myapp/card.html"