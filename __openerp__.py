# -*- coding: utf-8 -*-

{
    "name": "Real Estate Management",
    "description": """
Real Estate Management.
========================================================

This application allows you to work with real estates.
                    """,
    "version": "0.1",
    "depends": ["base", "product"],
    "category": "Product",
    "author": "Emad Shaaban",

    'data' : [
        'real_estate_view.xml', 
        'real_estate_workflow.xml', 
        'security/real_estate_security.xml',
        'security/ir.model.access.csv'
        ],

    "installable": True,
    "auto_install": False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
