# Copyright 2024 Coopdevs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = ["project.task"]
    
    def _should_have_forecast(self):
        self.ensure_one()
        if (not self.stage_id) or (not self.stage_id.forecast_line_active):
            _logger.info("skip task %s: no forecast for task state", self)
            return False
        else:
            return super(ProjectTask,self)._should_have_forecast()
        
