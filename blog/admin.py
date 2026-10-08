from django.contrib import admin
from .models import Post , User , contact , Tag , Category , Comment
# Register your models here.
class postAdmin(admin.ModelAdmin) : 
    list_display = ('title' , 'author' , 'category'  , 'get_tags', 'status' , 'published_date')

    def get_tags(self , obj) : 
        return ", ".join([tag.name for tag in obj.tag.all()])

    get_tags.short_description = 'tags'

    list_filter = ('author' , 'category')

    search_fields = ['title' , 'content']

    date_hierarchy = 'created_date'

    empty_value_disply = '_notset_'

    exclude = ('counted_view',)



admin.site.register(Post , postAdmin)
admin.site.register(User)
admin.site.register(contact)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)