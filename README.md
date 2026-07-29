# Meter Reading Invoice

## Purpose

Meter Reading Invoice is a custom Odoo module that extends customer invoice lines with utility meter readings. It adds Previous, New, and Actual reading columns so invoice quantities can be calculated from consumption.

## Features

- Adds Previous, New, and Actual reading fields to invoice lines.
- Retrieves the Previous reading from the latest posted customer invoice for the same customer, product, and company.
- Computes Actual as New minus Previous.
- Sets the invoice line Quantity from the computed Actual reading.
- Shows the meter reading columns on the invoice form and printed invoice report.

## Dependencies

- Odoo 18
- `account`

No additional Python packages or external services are required beyond a working Odoo Accounting installation.

## Installation

1. Copy the `meter_reading_invoice` folder into an Odoo addons path, for example:

   ```bash
   /home/me/odoo18/custom_addons/meter_reading_invoice
   ```

2. Ensure the custom addons path is configured:

   ```text
   addons_path = /home/me/odoo18/addons,/home/me/odoo18/custom_addons
   ```

3. Update the apps list or upgrade the module from the command line:

   ```bash
   ./odoo-bin -c /etc/odoo18.conf -d odoo18_db -u meter_reading_invoice
   ```

   If using the project virtual environment:

   ```bash
   venv/bin/python ./odoo-bin -c /etc/odoo18.conf -d odoo18_db -u meter_reading_invoice
   ```

## Testing

1. Open Odoo and go to customer invoices.
2. Create and post an invoice for a customer and product with a New meter reading.
3. Create another invoice for the same customer and product.
4. Confirm that Previous is filled from the earlier posted invoice's New reading.
5. Enter the current New reading and confirm that Actual equals New minus Previous.
6. Confirm that Quantity matches Actual.
7. Print or preview the invoice report and verify that Previous, New, and Actual appear before Quantity.

## Repository

Public GitHub repository:

```text
Add the submitted repository URL here.
```
