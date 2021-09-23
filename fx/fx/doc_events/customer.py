import frappe
from frappe import _

def customer_validate(doc, method):
    frappe.msgprint("hello customer {}".format(doc.customer_name))