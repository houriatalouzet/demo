# -*- coding: utf-8 -*-

from odoo import fields, models


class ResClass(models.Model):
    _name = "res.class"

    name = fields.Float(string="Class name")
    tutor_id = fields.Char(string="Tutor")
    Coefficient = fields.Float(string="Coefficient")
    