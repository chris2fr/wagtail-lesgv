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
        if hasattr(value,'ghost_tag') and value.ghost_tag:
           if value.ghost_filter:
              value.ghost_filter += ",primary_tag:{ghost_tag}"
           else:
               value.ghost_filter = "primary_tag={ghost_tag}"
        params = {'ghost_limit':getattr(value,'ghost_limit', 15), 'ghost_include':getattr(value,'ghost_include','tags,authors'),'ghost_order':getattr(value,'ghost_order',""),'ghost_filter':getattr(value,'ghost_filter',""),'ghost_page':"{}".format(getattr(value,'ghost_page',1))}
        context['posts'] = lesgv.services.get_blog_posts(params)
        return context

    class Meta:
      template = 'lesgv/blocks/ghost_index_block.html'
      icon = 'rss'