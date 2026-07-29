from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    previous_reading = fields.Float(
        string="Previous",
        compute="_compute_previous_reading",
        store=True,
    )

    new_reading = fields.Float(
        string="New",
    )

    actual_reading = fields.Float(
        string="Actual",
        compute="_compute_actual_reading",
        store=True,
    )

    @api.depends("new_reading", "previous_reading")
    def _compute_actual_reading(self):
        for line in self:
            # Consumption is the difference between the current and prior readings.
            line.actual_reading = line.new_reading - line.previous_reading
            # Odoo invoices from quantity, so the line quantity follows consumption.
            line.quantity = line.actual_reading

    @api.depends("product_id", "move_id.partner_id")
    def _compute_previous_reading(self):
        for line in self:
            line.previous_reading = 0.0

            if not line.product_id or not line.move_id.partner_id:
                continue

            # Use the latest posted customer invoice for the same customer,
            # product, and company as the source of the prior meter reading.
            previous = self.search(
                [
                    ("product_id", "=", line.product_id.id),
                    ("move_id.partner_id", "=", line.move_id.partner_id.id),
                    ("move_id.company_id", "=", line.move_id.company_id.id),
                    ("move_id.state", "=", "posted"),
                    ("move_id.move_type", "=", "out_invoice"),
                    ("display_type", "=", "product"),
                    ("id", "!=", line.id),
                ],
                order="id desc",
                limit=1,
            )

            if previous:
                line.previous_reading = previous.new_reading
