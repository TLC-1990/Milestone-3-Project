from django.test import TestCase
from .forms import TableReservationForm

class TestTableReservationForm(TestCase):
    
    def test_form_is_valid(self):
        form_data = {
            "customer_name": "John Doe",
            "date": "28-08-2025",
            "time": "12:00",
            "table": 1,
            "amount": 2,
            "email": "test@exampleprovider.com"
        }
        form = TableReservationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        
    def test_form_is_invalid_without_date(self):
        form_data = {
            "customer_name": "John Doe",
            "time": "12:00",
            "amount": 2,
            "email": "test@exampleprovider.com",
            "table": 1
        }
        form = TableReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("date", form.errors)

    def test_form_is_invalid_with_bad_email(self):
        form_data = {
            "customer_name": "John Doe",
            "date": "2025-08-28",
            "time": "12:00",
            "amount": 2,
            "email": "not-an-email",
            "table": 1
        }
        form = TableReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
        
        print(form.fields.keys())