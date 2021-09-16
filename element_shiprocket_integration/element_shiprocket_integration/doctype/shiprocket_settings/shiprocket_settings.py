# -*- coding: utf-8 -*-
# Copyright (c) 2020, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests, json
from frappe.model.document import Document

class ShiprocketSettings(Document):
	pass

@frappe.whitelist()
def shiprocket_get_token(email,password):
	url = "https://apiv2.shiprocket.in/v1/external/auth/login"
	headers = {'content-type': 'application/json'}
	p = {
		"email" : email,
		"password": password
	}
	payload = json.dumps(p)
	response = requests.request("POST", url, data=payload, headers=headers)
	return json.loads(response.text)