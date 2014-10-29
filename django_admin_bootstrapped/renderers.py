from bootstrap3 import renderers

class DABFieldRenderer(renderers.FieldRenderer):
    """
    A django-bootstrap3 field renderer that renders just the field
    """
    def render(self):
        # Hidden input requires no special treatment
        if self.field.is_hidden:
            return text_value(self.field)
        # Render the widget
        self.add_widget_attrs()
        html = self.field.as_widget(attrs=self.widget.attrs)
        return html

def render_field(field, **kwargs):
    return DABFieldRenderer(field, **kwargs).render()
