import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

def check_member_existence(first_name, last_name, email_address):
        exists = frappe.db.exists(
            "Library Member",
            {
                "first_name": first_name or first_name.lower() or first_name.upper() or first_name.capitalize(),
                "last_name": last_name or last_name.lower() or last_name.upper() or last_name.capitalize(),
                "email_address": email_address,
            },
        )
        if exists:
            return True