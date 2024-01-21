import frappe
import json
from frappe import _
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice

class CustomSalesInvoice(SalesInvoice):
  def validate(self):
    default_company = frappe.db.get_single_value('Global Defaults', 'default_company')
    company = frappe.get_doc("Company", default_company)
    self.custom_bank_name = company.custom_bank_name
    self.custom_iban_no = company.custom_iban_no
    self.custom_swift_code = company.custom_swift_code
    self.custom_account_no = company.custom_account_no
    super(CustomSalesInvoice, self).validate()
    