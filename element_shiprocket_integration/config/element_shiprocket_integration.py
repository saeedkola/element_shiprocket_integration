# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{			
			"label": _("Shiprocket Order"),
			"items": [
				{
					"type": "doctype",
					"name": "Shiprocket Order"
				}
			]
		},
		{
			"label": _("Settings"),
			"items": [
				{
					"type": "doctype",
					"name": "Package Dimensions"
				},
				{
					"type": "doctype",
					"name": "Shiprocket Settings"
				}
			]
		}
	]
