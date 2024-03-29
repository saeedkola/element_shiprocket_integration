# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "element_shiprocket_integration"
app_title = "Element Shiprocket Integration"
app_publisher = "Element Labs"
app_description = "Create Shiprocket Order Via ERPNext"
app_icon = "fa fa-rocket"
app_color = "purple"
app_email = "saeed@elementlabs.xyz"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/element_shiprocket_integration/css/element_shiprocket_integration.css"
app_include_js = "/assets/js/element_shiprocket_integration.js"
app_include_css = ["/assets/css/custom_css.css"]
# include js, css files in header of web template
# web_include_css = "/assets/element_shiprocket_integration/css/element_shiprocket_integration.css"
# web_include_js = "/assets/element_shiprocket_integration/js/element_shiprocket_integration.js"
# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
	"Sales Order" : "public/js/sales_order.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "element_shiprocket_integration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "element_shiprocket_integration.install.before_install"
# after_install = "element_shiprocket_integration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "element_shiprocket_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"element_shiprocket_integration.tasks.all"
# 	],
# 	"daily": [
# 		"element_shiprocket_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"element_shiprocket_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"element_shiprocket_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"element_shiprocket_integration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "element_shiprocket_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "element_shiprocket_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "element_shiprocket_integration.task.get_dashboard_data"
# }

