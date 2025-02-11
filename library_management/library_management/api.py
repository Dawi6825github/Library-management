
import frappe
from frappe import _ 

@frappe.whitelist(allow_guest=True)
def get_books():
    return frappe.get_all('Book', fields=['title', 'author', 'publish_date', 'isbn'])

@frappe.whitelist(allow_guest=True)
def add_book(title, author, publish_date, isbn):
    book = frappe.get_doc({
        'doctype': 'Book',
        'title': title,
        'author': author,
        'publish_date': publish_date,
        'isbn': isbn
    })
    book.insert()
    return book

@frappe.whitelist(allow_guest=True)
def update_book(book_id, title=None, author=None, publish_date=None, isbn=None):
    book = frappe.get_doc('Book', book_id)
    if title:
        book.title = title
    if author:
        book.author = author
    if publish_date:
        book.publish_date = publish_date
    if isbn:
        book.isbn = isbn
    book.save()
    return book

@frappe.whitelist(allow_guest=True)
def delete_book(book_id):
    frappe.delete_doc('Book', book_id)
    return {'status': 'success'}

@frappe.whitelist(allow_guest=True)
def get_loans():
    return frappe.get_all('Loan', fields=['member', 'book', 'loan_date', 'return_date'])

@frappe.whitelist(allow_guest=True)
def add_loan(member_id, book_id, loan_date, return_date):
    loan = frappe.get_doc({
        'doctype': 'Loan',
        'member': member_id,
        'book': book_id,
        'loan_date': loan_date,
        'return_date': return_date
    })
    loan.insert()
    return loan

@frappe.whitelist(allow_guest=True)
def update_loan(loan_id, return_date):
    loan = frappe.get_doc('Loan', loan_id)
    loan.return_date = return_date
    loan.save()
    return loan

@frappe.whitelist(allow_guest=True)
def delete_loan(loan_id):
    frappe.delete_doc('Loan', loan_id)
    return {'status': 'success'}

@frappe.whitelist(allow_guest=True)
def check_book_availability(book_id):
    loans = frappe.get_all('Loan', filters={'book': book_id, 'return_date': None})
    return {'available': len(loans) == 0}

@frappe.whitelist(allow_guest=True)
def add_member(first_name, last_name, email, phone):
    member = frappe.get_doc({
        'doctype': 'Member',
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone
    })
    member.insert()
    return member

@frappe.whitelist(allow_guest=True)
def update_member(member_id, first_name=None, last_name=None, email=None, phone=None):
    member = frappe.get_doc('Member', member_id)
    if first_name:
        member.first_name = first_name
    if last_name:
        member.last_name = last_name
    if email:
        member.email = email
    if phone:
        member.phone = phone
    member.save()
    return member

@frappe.whitelist(allow_guest=True)
def delete_member(member_id):
    frappe.delete_doc('Member', member_id)
    return {'status': 'success'}
