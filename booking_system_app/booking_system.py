from .models import Reservation

class BookingSystem:
    def create_reservation(self, name, email, phone_number, requested_time, other_notes=""):
        reservation = Reservation.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            requested_time=requested_time,
            other_notes=other_notes
        )
        return reservation