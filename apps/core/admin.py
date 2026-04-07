from django.contrib import admin

admin.site.site_header = "Painel do Mini Mercado"
admin.site.site_title = "Admin"
admin.site.index_title = "Gestão do Sistema"
readonly_fields = ('created_at', 'updated_at')
list_filter = ('status', 'created_at')