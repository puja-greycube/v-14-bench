import frappe
from frappe.model.document import Document

def execute():
    for member in frappe.db.get_all('Library Member',pluck='name'):
        doc = frappe.get_doc('Library Member',member)
        doc.compute_age()
        doc.save()