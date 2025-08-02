from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket with AI support'

    name = fields.Char(string="Subject", required=True)
    description = fields.Text(string="Description")
    category = fields.Selection([
        ('general', 'General'),
        ('technical', 'Technical'),
        ('billing', 'Billing'),
    ], string="Category", default='general')
    ai_suggested_reply = fields.Text(string="AI Suggested Reply", readonly=True)

    @api.model
    def generate_ai_reply(self, ticket_description):
        # Placeholder logic for AI (we’ll add OpenAI later)
        return "Thank you for your ticket. We're looking into it!"
