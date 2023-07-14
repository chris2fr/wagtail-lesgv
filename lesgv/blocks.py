# from wagtail import blocks
# import lesgv.services

# class GhostIndexBlock(blocks.StructBlock):
#     ghost_tag = blocks.CharBlock(required=False)
#     ghost_filter = blocks.CharBlock(required=False)
#     ghost_order = blocks.CharBlock(required=False)
#     # ghost_formats = blocks.CharBlock(required=False)
#     ghost_limit = blocks.CharBlock(required=False)
#     ghost_include = blocks.CharBlock(required=False)
#     ghost_page = blocks.IntegerBlock(required=False)

#     def get_context(self, value, parent_context=None):
#         context = super().get_context(value, parent_context=parent_context)
#         # print(params)
#         context['posts'] = lesgv.services.get_blog_posts(lesgv.services.ProcessGhostParams(value))
#         return context

#     class Meta:
#       template = 'lesgv/blocks/ghost_index_block.html'
#       icon = 'rss'