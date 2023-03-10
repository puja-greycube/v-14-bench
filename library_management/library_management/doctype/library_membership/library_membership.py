# Copyright (c) 2023, Puja and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryMembership(Document):

	def validate(self):
		# if self.to_date <= self.from_date:
		# 	frappe.throw("To date can not be earlier from from date")
		# get loan period and compute to_date by adding loan_period to from_date

		loan_period = frappe.db.get_single_value('Library Settings', 'loan_period')
		self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
	
	def before_submit(self):
		exists = frappe.db.exists(
			'Library Membership',
			{
				'library_member':self.library_member,
				'docstatus':1,
				'to_date':('>',self.from_date),
			},
		)
		if exists:
			frappe.throw('There is an active membership for this member')

		