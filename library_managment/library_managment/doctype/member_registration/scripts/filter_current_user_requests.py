import frappe

def get_filtered_records(doctype, txt, filters, limit_start, limit_page_length, order_by, sort_order, user):
    filtered_records = frappe.get_all(doctype, filters={'owner': user}, fields=['first_name', 'last_name', 'email_address', 'phone', 'status'], limit_start=limit_start, limit_page_length=limit_page_length, order_by=order_by, sort_order=sort_order)

    return filtered_records
