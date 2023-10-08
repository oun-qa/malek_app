// Copyright (c) 2023, Malek and contributors
// For license information, please see license.txt


frappe.ui.form.on('Member Registration', {
	refresh: function(frm) {
		const isLibrarian = frappe.user.has_role('Librarian');

		if (isLibrarian && frm.doc.status === 'Approved by Library members leader') {
			frm.add_custom_button('Approve Request', () => {
                if (frm.doc.status === 'Rejected'){
                    frappe.msgprint("You cannot approve a request that has already been rejected.")
                } else {
                    frm.set_value('status', 'Approved');
                    frm.save().then(() => {
                        frappe.call({
                            method: 'library_managment.library_managment.doctype.member_registration.scripts.create_library_member_record.create_library_member',
                            args: {
                                member_registration: frm.doc.name
                            },
                            callback: function(response) {
                                if (!response.exc) {
                                    frappe.msgprint('Library Member added successfully.');
                                }
                            }
                        });
                    });
                }
            }, "Actions");
			
			frm.add_custom_button('Reject Request', () => {
                if (frm.doc.status === 'Approved'){
                    frappe.throw("This Request is approved, you can delete the member from library members list")
                } else{
                    frm.set_value('status', 'Rejected');
                    frm.save();
                } 
			}, "Actions");
		}}
	})	
