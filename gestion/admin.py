from django.contrib import admin
from django.db.models import Count
from .models import Produit, Client, Vente, AuditVente


admin.site.register(Produit)
admin.site.register(Client)
admin.site.register(Vente)


@admin.register(AuditVente)
class AuditVenteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AuditVente._meta.fields]

    change_list_template = "admin/auditvente_change_list.html"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        stats = (
            AuditVente.objects
            .values('type_operation')
            .annotate(total=Count('type_operation'))
        )

        summary = {
            'INSERT': 0,
            'UPDATE': 0,
            'DELETE': 0,
        }

        for item in stats:
            summary[item['type_operation']] = item['total']

        extra_context['summary'] = summary

        return super().changelist_view(request, extra_context=extra_context)