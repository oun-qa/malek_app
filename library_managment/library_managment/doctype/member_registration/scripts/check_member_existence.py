import frappe

def check_member_existence(first_name, last_name, email_address):
        exists = frappe.db.exists(
            "Library Member",
            {
                "first_name": first_name or str(first_name).lower() or str(first_name).upper() or str(first_name).capitalize(),
                "last_name": last_name or str(last_name).lower() or str(last_name).upper() or str(last_name).capitalize(),
                "email_address": email_address,
            },
        )
        if exists:
            return True
        return False