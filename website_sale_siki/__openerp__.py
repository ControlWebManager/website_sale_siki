{
    'name': 'Cumstom Module eCommerce',
    'summary': 'Child Module - Parent website_sale',
    'author' : 'SIKI SAS, Developer Ing Henry Vivas',
	'website' : 'www.sikisoftware.com',
    "support": "controlwebmanager@gmail.com",
    'category': 'Website',
    'description': """
Extend Cumstom OpenERP E-Commerce
==================

List of modifications:
-------------------
    * V.-1.0 Field description and features in website ( Req. 1062 )
    * ...:
        * ...
        * ...
        """,
    'depends': [
        'website_sale',
        'website',
        'product',
    ],
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'data/demo.xml',
    ],
    'installable': True,
    'application': False,
}