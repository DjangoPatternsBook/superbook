import pudb as dbg              # Change to any *db

from django.template import Library, Node

register = Library()


class PdbNode(Node):

    def render(self, context):
        dbg.set_trace()         # Debugger stops here
        return ''


@register.tag
def pdb(parser, token):
    return PdbNode()
