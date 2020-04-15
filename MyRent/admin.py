from django.contrib import admin
from django.utils.safestring import mark_safe

from MyRent.models import Flat, Tenant, Agreement, Operation, OperationDict, Landlord, Image


class FlatAdmin(admin.ModelAdmin):
    model = Flat
    list_display = ('__str__', 'is_for_rent', 'info')


class TenantAdmin(admin.ModelAdmin):
    model = Tenant
    list_display = ('__str__', 'phone', 'email', 'info')


class AgreementAdmin(admin.ModelAdmin):
    model = Agreement
    list_display = ('code', 'agreement_date', 'date_from', 'date_to',
                    'mth_payment_value', 'mth_payment_deadline', 'info')


class OperationAdmin(admin.ModelAdmin):
    model = Operation
    list_display = ('__str__', 'info')


class ImageAdmin(admin.ModelAdmin):
    model = Image
    readonly_fields = ["picture_image"]

    def picture_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.picture.url,
            width=obj.picture.width,
            height=obj.picture.height,
            )
        )

admin.site.register(Flat, FlatAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(OperationDict)
admin.site.register(Landlord)
admin.site.register(Image, ImageAdmin)
