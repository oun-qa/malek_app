frappe.listview_settings['Member Registration'] = {
    onload: function(listview) {
        listview.get_list = function(txt, page, callback) {
            frappe.call({
                method: 'library_managment.library_managment.doctype.member_registration.scripts.filter_current_user_requests.get_filtered_records',
                args: {
                    doctype: 'Member Registration',
                    txt: txt,
                    filters: listview.filter_list.get_filters(),
                    limit_start: page * listview.page_length,
                    limit_page_length: listview.page_length,
                    order_by: listview.sort_selector.get_sql_string(),
                    sort_order: listview.sort_order,
                    user: frappe.session.user
                },
                callback: function(r) {
                    if (r.message) {
                        callback(r.message);
                    }
                }
            });
        };
    }
};
