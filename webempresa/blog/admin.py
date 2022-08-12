from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('author', 'published')
    
    #Esto agrega un buscador del campo que quieras
    #El autor en este caso es una llave foranea y lo mismo para categories por eso se llama asi
    search_fields = ('title', 'content', 'author__username', 'categories__name')

    #Esto ordena por jerarquias de fechas
    date_hierarchy = 'published'

    #Esto filtro
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
        post_categories.short_description = "Categories"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)