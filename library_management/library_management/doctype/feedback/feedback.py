# Copyright (c) 2023, Puja and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class feedback(Document):
	pass
	# @frappe.whitelist()

	# def set_rating(docname):
	# 	d = frappe.get_doc("feedback",docname)
	# 	d.feedback_rating = "frm.feedback_rating"
	# 	d.save()
	# 	return True