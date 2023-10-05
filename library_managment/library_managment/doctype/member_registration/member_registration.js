// Copyright (c) 2023, Malek and contributors
// For license information, please see license.txt

frappe.ui.form.on('Member Registration', {
	refresh: function(frm) {
		const isLibrarian = frappe.user.has_role('Librarian');

		if (isLibrarian) {
			frm.add_custom_button('Approve Membership', () => {
				frm.set_value('status', 'Approved');
				frm.save().then(() => {
                    frappe.call({
                        method: 'member_registration.member_registration.create_library_membership',
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
			
			frm.add_custom_button('Reject Membership', () => {
				frm.set_value('status', 'Rejected');
				frm.save();
			});
		}}
	})
