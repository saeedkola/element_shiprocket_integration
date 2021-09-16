// Copyright (c) 2020, Element Labs and contributors
// For license information, please see license.txt
frappe.ui.form.on('Shiprocket Order', {
	setup: function(frm) {
		frm.set_value('company', frappe.defaults.get_user_default("company"));
		frm.set_query('company_address', function(doc) {
			if(!doc.company) {
				frappe.throw(__('Please set Company'));
			}

			return {
				query: 'frappe.contacts.doctype.address.address.address_query',
				filters: {
					link_doctype: 'Company',
					link_name: doc.company
				}
			};
		});
		frm.set_query('customer_address', function(doc) {
			if(!doc.customer) {
				frappe.throw(__('Please set Customer'));
			}

			return {
				query: 'frappe.contacts.doctype.address.address.address_query',
				filters: {
					link_doctype: 'Customer',
					link_name: doc.customer
				}
			};
		});
		frm.set_query('shipping_address', function(doc) {
			if(!doc.customer) {
				frappe.throw(__('Please set Customer'));
			}

			return {
				query: 'frappe.contacts.doctype.address.address.address_query',
				filters: {
					link_doctype: 'Customer',
					link_name: doc.customer
				}
			};
		});
	},
	// before_submit: function(frm){

	// },
	courier_serviceabilty: function(frm){
		// if mandatory mandatory fields are set then
		if(
			!frm.doc.pickup_postcode || 
			(!frm.doc.delivery_postcode && !frm.doc.billing_postcode) ||
			!frm.doc.payment_type ||
			!frm.doc.weight ||
			!frm.doc.length ||
			!frm.doc.breadth ||
			!frm.doc.height
			){
			if(!frm.doc.pickup_postcode){
				frappe.msgprint(__("Pickup Postal Code Not Set"));
			}
			if(!frm.doc.delivery_postcode && !frm.doc.billing_postcode){
				frappe.msgprint(__("Delivery/Billing Postal Code Not Set"));
			}
			if(!frm.doc.payment_type){
				frappe.msgprint(__("Payment Type Not Set"));
			}
			if(!frm.doc.weight){
				frappe.msgprint(__("Package Weight Not Set"));
			}
			if (!frm.doc.length || !frm.doc.breadth || !frm.doc.height) {
				frappe.msgprint(__("Package Dimensions Not Set"));
			}
		}else{
			frappe.call({
				method: 'element_shiprocket_integration.element_shiprocket_integration.doctype.shiprocket_order.shiprocket_order.courier_serviceability',
				args: {
					"doc": frm.doc
				},
				callback: function(r){
					$(frm.fields_dict['html'].wrapper).html(
						r.message
					);
					$('#button1').click(function(event) {
						console.log("But1");
					});
					$('#button2').click(function(event) {
						console.log("But2");
					});
				}
			});
		}
		
	}
});