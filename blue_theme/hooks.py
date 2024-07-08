# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: ADVAITH BG (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import base64
from odoo.modules import get_module_resource

def set_menu_icons(cr):
    """Set custom icons for menu items"""
    menu_icon_mapping = {
        'Contacts': 'Contacts.png',
        'Link Tracker': 'Link Tracker.png',
        'Dashboards': 'Dashboards.png',
        'Sales': 'Sales.png',
        'Invoicing': 'Invoicing.png',
        'Accounting': 'Invoicing.png',
        'Inventory': 'Inventory.png',
        'Purchase': 'Purchase.png',
        'Calendar': 'Calendar.png',
        'CRM': 'CRM.png',
        'To-do': 'Note.png',
        'Website': 'Website.png',
        'Point of Sale': 'Point of Sale.png',
        'Manufacturing': 'Manufacturing.png',
        'Repairs': 'Repairs.png',
        'Email Marketing': 'Email Marketing.png',
        'SMS Marketing': 'SMS Marketing.png',
        'Project': 'Project.png',
        'Surveys': 'Surveys.png',
        'Employees': 'Employees.png',
        'Recruitment': 'Recruitment.png',
        'Attendances': 'Attendances.png',
        'Time Off': 'Time Off.png',
        'Expenses': 'Expenses.png',
        'Maintenance': 'Maintenance.png',
        'Live Chat': 'Live Chat.png',
        'Lunch': 'Lunch.png',
        'Fleet': 'Fleet.png',
        'Timesheets': 'Timesheets.png',
        'Events': 'Events.png',
        'eLearning': 'eLearning.png',
        'Members': 'Members.png',
    }

    menu_items = cr['ir.ui.menu'].search([('parent_id', '=', False)])
    for menu in menu_items:
        icon_filename = menu_icon_mapping.get(menu.name)
        if icon_filename:
            img_path = get_module_resource(
                'blue_theme', 'static', 'src', 'img', 'icons', icon_filename)
            with open(img_path, "rb") as img_file:
                menu.write({'web_icon_data': base64.b64encode(img_file.read())})

def test_pre_init_hook(cr):
    """Pre-init hook to set menu icons"""
    set_menu_icons(cr)

def test_post_init_hook(cr):
    """Post-init hook to set menu icons"""
    set_menu_icons(cr)
