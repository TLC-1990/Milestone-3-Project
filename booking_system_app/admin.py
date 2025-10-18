from django.contrib import admin
from .models import Table, TableReservationSlot


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
	list_display = ("name", "location", "capacity")
	list_filter = ("location",)
	search_fields = ("name",)


@admin.register(TableReservationSlot)
class TableReservationSlotAdmin(admin.ModelAdmin):
	list_display = (
		"customer_name",
		"table",
		"time_slot",
        "date",
		"amount",
		"available",
	)
	list_filter = ("table", "available")
	search_fields = ("customer_name", "email", "notes")
	date_hierarchy = "date"
	ordering = ("-date",)