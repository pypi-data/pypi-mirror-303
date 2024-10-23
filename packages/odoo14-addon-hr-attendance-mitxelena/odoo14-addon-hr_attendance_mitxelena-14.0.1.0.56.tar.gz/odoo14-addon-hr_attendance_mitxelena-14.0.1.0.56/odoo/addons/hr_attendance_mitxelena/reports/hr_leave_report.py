# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, exceptions, _
from odoo.osv import expression


class LeaveReport(models.Model):
    _inherit = "hr.leave.report"
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        result = super(LeaveReport, self).read_group(domain, fields, groupby, offset, limit, orderby, lazy)
        for record in result:
            record["number_of_hours_display"] = sum([r.number_of_hours_display for r in self.search(record["__domain"])])
        return result

    number_of_hours_display = fields.Float("Number of Hours", compute="_compute_number_of_hours_display")

    @api.depends("number_of_days", "employee_id.resource_id.calendar_id.hours_per_day")
    def _compute_number_of_hours_display(self):
        for record in self:
            record.number_of_hours_display = record.number_of_days * record.employee_id.resource_id.calendar_id.hours_per_day
