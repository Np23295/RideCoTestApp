from .models import Maps
from django.db.models import Q
from django.contrib import admin


class MapsAdmin(admin.ModelAdmin):
    list_display = ('label', 'point', 'created_by', 'get_shared_with')
    fieldsets = [
        (None, {'fields': ['label', 'point', 'shared_with']}),
    ]
    list_filter = (
        ('created_by', admin.RelatedOnlyFieldListFilter),
    )

    def save_model(self, request, obj, form, change):
        # Added Created By for the maps model - it will help figure out the owner of the maps item
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(MapsAdmin, self).get_queryset(request)
        # Allow Super User or ADMIN to access all of the maps
        if request.user.is_superuser:
            return qs
        return qs.filter(Q(created_by=request.user) | Q(shared_with__id=request.user.id))


admin.site.register(Maps, MapsAdmin)
