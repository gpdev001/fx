# Copyright (c) 2013, SERVIO Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    # data = [['a', 1], ['b', 2], ['c', 9999]]

    data = frappe.get_all('Customer', filters=filters, fields=['name', 'customer_name', 'customer_type', 'territory', 'test_currency_1'])
    message = 'Total number of customers: <span class="font-weight-bold primary">{}</span>'.format(len(data))

    chart = {
        'data': {
            'labels': [
                'asymptomatic',
                'mild',
                'severe',
                'critical'
            ],
            'datasets': [
                {
                    'name': 'Fully Vaccinated',
                    'values': [45, 80, 22, 10]
                },
                {
                    'name': 'Not Vaccinated',
                    'values': [120, 280, 72, 30]
                }
            ]
        },
        'type': 'bar'
    }

    report_summary = [
        {
            "label":"cases",
            "value":len(data),
            "indicator": "Blue"
        },
        {
            "label":"positivity rate",
            "value":"26.5",
            "indicator": "Red"
        }
    ]

    return columns, data, message, chart, report_summary

def get_columns():
    columns = [
        {
            'fieldname': 'name',
            'label': _("Name"),
            'fieldtype': 'Link',
            'options': 'Customer',
            'width': 200
        },
        {
            'fieldname': 'customer_name',
            'label': _("Customer Name"),
            'fieldtype': 'Data',
            'width': 120
        },
        {
            'fieldname': 'customer_type',
            'label': _("Customer Type"),
            'fieldtype': 'Data',
            'width': 120
        },
        {
            'fieldname': 'territory',
            'label': _("Territory"),
            'fieldtype': 'Data',
            'width': 120
        },
        {
            'fieldname': 'test_currency_1',
            'label': _("Test Currency 1"),
            'fieldtype': 'Currency',
            'width': 120
        },
    ]
    return columns
