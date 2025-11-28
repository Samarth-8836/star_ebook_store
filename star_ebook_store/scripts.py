import frappe
from frappe.utils.file_manager import save_file

def create_ebook():
    # 1. Setup your file data (Use this if files are on your local disk)
    # You need to read the file as binary 'rb'
    with open("/home/samarth/Downloads/1003w-Qb8uSVdJDzw.webp", "rb") as f:
        cover_content = f.read()
    
    with open("/home/samarth/Downloads/sample-local-pdf.pdf", "rb") as f:
        asset_content = f.read()

    # 2. Upload the files to Frappe to get their URLs
    # save_file(filename, content, dt, dn, folder, is_private)
    # We set is_private=0 for Cover Image (public) and is_private=1 for Asset (protected)
    cover_file = save_file("cover.jpg", cover_content, None, None, is_private=0)
    asset_file = save_file("book.pdf", asset_content, None, None, is_private=1)

    # 3. Create the eBook Document
    doc = frappe.get_doc({
        "doctype": "ebook",
        "name": "Learning Frappe 101",  # "Set by User" naming rule requires this
        "cover_image": cover_file.file_url,
        "asset_file": asset_file.file_url,
        "format": "PDF",
        "price": 25.00,
        "author": "7tl61ke254",  # This must be the exact 'name' of an existing Author document
        "description": "## Introduction\nThis is a **markdown** description.",
        "table_of_contents": "- Chapter 1: Getting Started\n- Chapter 2: DocTypes",
        "route": "store/learning-frappe-101",
        "is_published": 1
    })

    # 4. Insert into Database
    doc.insert()
    
    # 5. Commit the transaction (if running from console or external script)
    frappe.db.commit()

    print(f"Successfully created ebook: {doc.name}")

# Run the function
create_ebook()