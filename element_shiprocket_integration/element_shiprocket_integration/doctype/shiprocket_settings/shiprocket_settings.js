// Copyright (c) 2020, Element Labs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shiprocket Settings', {
	refresh: function(frm) {
		frm.set_query("address", "shiprocket_addresses", function(doc, cdt, cdn) {
			return {
				query: 'frappe.contacts.doctype.address.address.address_query',
				filters: {
					link_doctype: 'Company',
					link_name: frappe.defaults.get_user_default("company")				
				}
			};
		});
	},
	get_token: function(frm){
		frappe.call({
			method: 'element_shiprocket_integration.element_shiprocket_integration.doctype.shiprocket_settings.shiprocket_settings.shiprocket_get_token',
			args: {
				email : frm.doc.email,
				password: frm.doc.password
			},
			callback: function(r){
				if(r.message.status_code == 400){
					frappe.msgprint(r.message.message);
				}else{
					frm.set_value('token',r.message.token);
					frm.set_value('password',"");
					show_alert("Authentication Successful.",10);
					frm.save();
				}				
			}
		})
	}
});
