// Copyright (c) 2016, SERVIO Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sample script report"] = {
	"filters": [
        {
            fieldname: "customer_type",
            label: __("Customer Type"),
            fieldtype: "Select",
            options: ["Company", "Individual"]
        }
	]
};
