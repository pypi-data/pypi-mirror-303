# Copyright 2022 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Project Forecast Task Stage",
    "summary": "Project Forecast Filter by Task Stages (project.task.type)",
    "version": "16.0.1.0.2",
    "author": "Coopdevs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Project",
    "website": "https://github.com/OCA/project",
    "depends": ["project_forecast_line"],
    "data": [
        "views/project_task_type.xml",
    ],
    "demo": [],
    "installable": True,
    "development_status": "Alpha",
    "application": True,
}
