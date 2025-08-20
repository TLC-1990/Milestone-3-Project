from django.conf import settings 


def append_customer_to_sheet(first_name, last_name, email, password):
   
    worksheet = settings.SHEET.worksheet('customers')
    new_row = [first_name, last_name, email, password]
    
    worksheet.append_row(new_row, value_input_option='RAW')
    return True
