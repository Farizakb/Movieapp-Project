from django import template

register = template.Library()

@register.filter
def display_rating(raiting_count):
    html = ""
    print(raiting_count)
    for i in range(5):
        if i<int(raiting_count):
            
            html +='<i class="fa fa-star active"></i>'
        else:
            html +='<i class="fa fa-star"></i>'

        
    return html
        