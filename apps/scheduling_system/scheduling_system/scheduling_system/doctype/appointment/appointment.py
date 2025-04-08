# Copyright (c) 2025, Kauan Pardini and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Appointment(Document):
	pass

@frappe.whitelist()
def check_conflicting_appointments(seller, start_date, end_date, docname=None):
    conflicts = frappe.get_all(
        "Appointment",
        filters={
            "seller": seller,
            "status": ["!=", "Canceled"],
            "start_date": ["<", end_date],
            "end_date": [">", start_date],
            "name": ["!=", docname]
        },
        fields=["name", "start_date", "end_date"]
    )
    return conflicts
