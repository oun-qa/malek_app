# Copyright (c) 2023, Malek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from library_managment.library_managment.doctype.member_registration.scripts.check_member_existence import check_member_existence

class MemberRegistration(Document):
	
    def before_save(self):
        if check_member_existence(self.first_name, self.last_name, self.email_address):
            frappe.throw("This person is already a member in the library")

