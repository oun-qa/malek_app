# Copyright (c) 2023, Malek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MemberRegistration(Document):
	pass	


@frappe.whitelist()
def create_library_membership(member_registration):
    member_registration_doc = frappe.get_doc('Member Registration', member_registration)

    library_membership_doc = frappe.new_doc('Library Membership')
    library_membership_doc.library_member = member_registration_doc.member_name
    library_membership_doc.first_name = member_registration_doc.first_name
    library_membership_doc.last_name = member_registration_doc.last_name
    library_membership_doc.email_address = member_registration_doc.email_address
    library_membership_doc.phone = member_registration_doc.phone

    library_membership_doc.insert(ignore_permissions=True)

    return library_membership_doc
