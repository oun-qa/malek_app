# Copyright (c) 2023, Malek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            article = frappe.get_doc("Article", self.article)
            article.status = "Issued"
            article.save()

        if self.type == "Return":
            self.validate_return()
            article = frappe.get_doc("Article", self.article)
            article.status = "Available"
            article.save()

    def validate_issue(self):
        self.validate_membership()
        article = frappe.get_doc("Article", self.article)
        
        if article.status == "Issued" and article.library_member == self.library_member:
            frappe.throw("Article is already issued by this member") 
        elif article.status == "Issued":
            frappe.throw("Article is already issued by another member")

    def validate_return(self):
        article = frappe.get_doc("Article", self.article)  
        if article.status == "Available":
            frappe.throw("Article cannot be returned without being issued first")

    def validate_membership(self):
        valid_membership = frappe.db.exists("Library Membership", {
            "library_member": self.library_member,
            "docstatus": DocStatus.submitted(),
            "from_date": ("<", self.date),
            "to_date": (">", self.date),
        },)

        if not valid_membership:
            frappe.throw("The member does not have a valid membership")

