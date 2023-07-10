from wagtail import blocks
import lesgv.services

class GhostIndexBlock(blocks.StructBlock):
    ghost_tag = blocks.CharBlock(required=False)
    ghost_filter = blocks.CharBlock(required=False)
    ghost_order = blocks.CharBlock(required=False)
    # ghost_formats = blocks.CharBlock(required=False)
    ghost_limit = blocks.CharBlock(required=False)
    ghost_include = blocks.CharBlock(required=False)
    ghost_page = blocks.IntegerBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        post_filter = value.get('post_filter') or ''
        if post_filter != '' and value.get('ghost_tag'):
            post_filter += ","
        if value.get('ghost_tag'):
            post_filter += "primary_tag:{}".format(value.get('ghost_tag'))
        params = {
            'ghost_limit':value.get('ghost_limit') or  15, 
            'ghost_include':value.get('ghost_include') or 'tags,authors',
            'ghost_order':value.get('ghost_order') or "",
            'ghost_filter':post_filter,
            'ghost_page':"{}".format(value.get('ghost_page') or 1)
        }
        # print(params)
        context['posts'] = lesgv.services.get_blog_posts(params)
        return context

    class Meta:
      template = 'lesgv/blocks/ghost_index_block.html'
      icon = 'rss'