from django import template



from blog.models import FooterText


register = template.Library()
# https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/


# @register.simple_tag(takes_context=True)
# def get_site_root(context):
#     # This returns a core.Page. The main menu needs to have the site.root_page
#     # defined else will return an object attribute error ('str' object has no
#     # attribute 'get_children')
#     return Site.find_for_request(context['request']).root_page


# def has_menu_children(page):
#     # This is used by the top_menu property
#     # get_children is a Treebeard API thing
#     # https://tabo.pe/projects/django-treebeard/docs/4.0.1/api.html
#     return page.get_children().live().in_menu().exists()


# def has_children(page):
#     # Generically allow index pages to list their children
#     return page.get_children().live().exists()


# def is_active(page, current_page):
#     # To give us active state on main navigation
#     return (current_page.url_path.startswith(page.url_path) if current_page else False)


# # Retrieves the top menu items - the immediate children of the parent page
# # The has_menu_children method is necessary because the Foundation menu requires
# # a dropdown class to be applied to a parent


@register.inclusion_tag('blog/includes/footer_text.html', takes_context=True)
def get_footer_text(context):
    footer_text = ""
    footer = FooterText.objects.first() 
    if footer is not None:
        footer_text = footer.body
    return {
        'footer_text': footer_text,
    }
