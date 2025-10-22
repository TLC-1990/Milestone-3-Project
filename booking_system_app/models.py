"""Models for the booking_system_app."""
from django.db import models
from django.core.exceptions import ValidationError

MAX_TABLES_PER_LOCATION = {
    'inside': 5,
    'outside': 5,
}


class Table(models.Model):
    """Model representing a table in the restaurant."""

    LOCATION_CHOICES = [('inside', 'Inside'), ('outside', 'Outside')]
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    capacity = models.PositiveBigIntegerField()

    def __str__(self):
        """Return a representation of the Table."""
        return f"{self.name} ({self.get_location_display()},capacity {self.capacity})"


class TableReservationSlot(models.Model):
    """Model representing a reservation slot for a table."""

    table = models.ForeignKey(Table,
                              on_delete=models.CASCADE,
                              related_name='slots')
    time_slot = models.TimeField()
    date = models.DateField(null=True, blank=True)
    amount = models.PositiveBigIntegerField(default=1)
    available = models.BooleanField(default=True)
    max_amount = models.PositiveBigIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=False, null=False)

    @property
    def available_amount(self):
        """Calculate available amount for the reservation slot."""
        return max(self.max_amount - self.amount, 0)

    class Meta:
        """Meta options for TableReservationSlot model."""

        unique_together = ('table', 'time_slot', 'date')

    def clean(self):
        """Validate to ensure booking limits per location are not exceeded."""
        super().clean()

        location = self.table.location

        existing_bookings = TableReservationSlot.objects.filter(
            table__location=location,
            time_slot=self.time_slot,
        ).exclude(pk=self.pk).count()

        if existing_bookings >= MAX_TABLES_PER_LOCATION[location]:
            raise ValidationError(
                f"Sorry! All {MAX_TABLES_PER_LOCATION[location]} {location} tables are already booked for this time. Please pick a different time or location."
            )

    @property
    def num_people(self):
        """Get number of people for the reservation."""
        return self.amount

    @num_people.setter
    def num_people(self, value):
        """Set number of people for the reservation."""
        self.amount = value

    def __str__(self):
        """Return a representation of the TableReservationSlot."""
        return (
            f"{self.table.name} ({self.table.get_location_display()},"
            f"capacity {self.table.capacity}) at {self.time_slot} on {self.date} "
            f"for {self.num_people} people")
