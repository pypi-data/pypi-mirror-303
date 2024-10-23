# Copyright 2024 Coopdevs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import api, fields, models
_logger = logging.getLogger(__name__)

class ProjectTaskType(models.Model):
    _name = 'project.task.type'
    _inherit = ["project.task.type"]

    forecast_line_active = fields.Boolean(
        "Include this stage in forecast?",
        default= True,
        help="If tasks in that stage should be considered by forecast calculations.",
    )

