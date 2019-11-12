##############################################################################
#
#    Account Cut-off Accrual Picking module for OpenERP
#    Copyright (C) 2013 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Account Accrual Picking',
    'version': '12.0.0.1.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Accrued Expense & Accrued Revenue from Pickings',
    'author': "Akretion,Odoo Community Association (OCA)",
    'website': 'http://www.akretion.com',
    'depends': ['account_cutoff_accrual_base', 'purchase', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_cutoff_view.xml',
        'data/ir_cron.xml',
    ],
    'images': [
        'images/accrued_expense_draft.jpg',
        'images/accrued_expense_journal_entry.jpg',
        'images/accrued_expense_done.jpg',
        ],
    'installable': True,
    'application': True,
}
