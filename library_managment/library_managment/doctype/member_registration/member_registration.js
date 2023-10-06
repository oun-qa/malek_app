// Copyright (c) 2023, Malek and contributors
// For license information, please see license.txt


frappe.ui.form.on('Member Registration', {
	refresh: function(frm) {
		const isLibrarian = frappe.user.has_role('Librarian');

		if (isLibrarian) {
			frm.add_custom_button('Approve Member', () => {
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
            });
			
			frm.add_custom_button('Reject Member', () => {
                if (frm.doc.status === 'Approved'){
                    frappe.throw("This Request is approved, you can delete the member from library members list")
                } else{
                    frm.set_value('status', 'Rejected');
                    frm.save();
                } 
			});
		}}
	})	


