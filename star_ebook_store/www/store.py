import frappe


def get_context(context):
	context.ebooks = frappe.get_all(
		"ebook",
		fields=[
			"name",
			"cover_image",
			"price",
			"format",
			"route",
			"creation",
			"author.full_name as author_name",
		],
		filters={"is_published": 1},
		order_by="creation desc"
	)