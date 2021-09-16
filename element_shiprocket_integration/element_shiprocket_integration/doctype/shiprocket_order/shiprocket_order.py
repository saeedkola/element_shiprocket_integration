# -*- coding: utf-8 -*-
# Copyright (c) 2020, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, requests, json
from frappe.model.document import Document

class ShiprocketOrder(Document):
	def validate(self):
		pass

	def on_submit(self):
		settings = frappe.get_single('Shiprocket Settings')
		url = "https://apiv2.shiprocket.in/v1/external/shipments/create/forward-shipment"
		payload = {}
		headers = {
		'content-type': "application/json",
		"authorization": "Bearer "+settings.token
		}			   

		response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

		print(response.text)


@frappe.whitelist()
def make_shiprocket_order(so_name):
	mapper = {
		"Sales Order": {
			"doctype": "Shiprocket Order",
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"Sales Order Item":{
			"doctype" : "Shiprocket Order Item"
		}
	}
	return get_mapped_doc("Sales Order", so_name, mapper)

@frappe.whitelist()
def courier_serviceability(doc):
	url = "https://apiv2.shiprocket.in/v1/external/courier/serviceability/"

	# vari = {"customer_name" : customer_name}
	doc = json.loads(doc)
	if not 'shipping_postcode' in doc:
		delivery_postcode = doc['billing_postcode']
	else:
		delivery_postcode = doc['shipping_postcode']

	if doc['payment_type'] == "COD":
		payment_type = 1
	else:
		payment_type = 0
	
	if doc['weight'] >= 0.5:
		weight = doc['weight']
	else:
		weight = 0.5
	
	p = {
	"pickup_postcode" 	: doc['pickup_postcode'],
	"delivery_postcode"	: delivery_postcode,
	"cod"				: payment_type,
	"weight"			: weight
	}

	if doc['length'] and doc['breadth'] and doc['height']:
		p["length"] 	= doc['length']
		p["breadth"] 	= doc['breadth']
		p["height"]		= doc['height']

	if doc['shipping_mode']:
		p["mode"]		= doc['shipping_mode']

	settings = frappe.get_single('Shiprocket Settings')

	headers = {
    'content-type': "application/json",
    'authorization': "Bearer "+settings.token
    }

	response = requests.request("GET", url, data=json.dumps(p), headers=headers)
	html = frappe.render_template('public/js/templates/available_couriers.html', json.loads(response.text))
	
	return html