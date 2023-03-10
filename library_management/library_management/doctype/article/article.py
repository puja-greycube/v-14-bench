# Copyright (c) 2023, Puja and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
# from frappe.website.website_generator import WebsiteGenerator


class Article(WebsiteGenerator):
	# pass
	# whitelisted method will be available to call from client side
	@frappe.whitelist()

	#call below method to directly set isbn field value on server side 
	def set_isbn(self):
		self.isbn = frappe.generate_hash('Article',10)



	# call below method if want to call from client side and set value in isb field
	# def get_isbn(self):
	# 	return frappe.generate_hash('Article',10)


#below method we will call by frappe.call instead of frm.call
#when frappe.call is used,we have to specify full path in client script .
# frappe.call is define outside of class like below. 

# @frappe.whitelist()
# def get_isbn():
# 	return frappe.generate_hash('Article',10)
