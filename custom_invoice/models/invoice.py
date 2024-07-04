# -*- coding: utf-8 -*-
# © 2024 Jaime Millán <jmillan@stemdo.io>

from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    additional_info = fields.Text(string='Additional Information')
    custom_date = fields.Date(string='Custom Date')
    project_url = fields.Char(string='Project URL')
    project_manager = fields.Many2one('res.users', string='Project Manager')
    project_status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ], string='Project Status')
    detailed_description = fields.Text(string='Detailed Description')
    internal_notes = fields.Text(string='Internal Notes')
    delivery_date = fields.Date(string='Delivery Date')

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    line_comment = fields.Text(string='Line Comment')
