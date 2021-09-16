frappe.ui.form.on('Sales Order', {
	refresh: function(frm) {
		frm.add_custom_button(__("Create Shiprocket Order"), function() {
			console.log('Clicked');
		});
	}
});