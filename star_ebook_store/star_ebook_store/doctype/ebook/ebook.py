# Copyright (c) 2025, Samarth and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator # type: ignore


class ebook(WebsiteGenerator):
	def get_context(self, context):
		context.author = frappe.db.get_value(
            "Author", self.author, ["full_name as name", "bio"], as_dict=True
        )
