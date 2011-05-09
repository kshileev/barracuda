from django.contrib import admin
import models

admin.site.register(models.CargoExpenseType)
admin.site.register(models.Customs)
admin.site.register(models.Warehouse)

class ConveyancePointInline(admin.TabularInline):
    model = models.ConveyancePoint

class CCDInline(admin.StackedInline):
    model = models.CCD

class CargoExpensesInline(admin.TabularInline):
    model = models.CargoExpense

class ConveyanceAdmin(admin.ModelAdmin):
    inlines = [ConveyancePointInline, CCDInline, CargoExpensesInline]

admin.site.register(models.Conveyance, ConveyanceAdmin)



