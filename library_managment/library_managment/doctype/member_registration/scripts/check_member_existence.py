import frappe

def check_member_existence(first_name, last_name, email_address):
        exists = frappe.db.exists(
            "Library Member",
            {
                "first_name": first_name,
                "last_name": last_name,
                "email_address": email_address,
            },
        )
        if exists:
            return True
        return False