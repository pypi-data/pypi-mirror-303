# Copyright 2024 Coopdevs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import api, fields, models
_logger = logging.getLogger(__name__)

class ProjectTaskType(models.Model):
    _name = 'project.task.type'
    _inherit = ["project.task.type"]

    forecast_line_type = fields.Selection(
        [("forecast", "Forecast"), ("confirmed", "Confirmed")],
        help="type of forecast lines created by the tasks in that stage",
    )

