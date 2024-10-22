# Copyright 2024 Coopdevs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = ["project.task", "forecast.line.mixin"]
    
    def _should_have_forecast(self):
        self.ensure_one()
        if not self.stage_id:
            _logger.info("skip task %s: no task state defined", self)
            return super()._should_have_forecast()
        forecast_type = self.stage_id.forecast_line_type
        if not forecast_type:
            _logger.info("skip task %s: no forecast for task state", self)
            return super()._should_have_forecast()
        else:
            return forecast_type

        
