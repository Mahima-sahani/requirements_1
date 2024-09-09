{
    'name': 'Product KSC',
    'version': '16.1.1',
    'summary': 'Manage Products',
    'description': 'Module to manage products with additional fields and features.',
    'category': 'Sales',
    'author': 'Inno-age',
    'depends': ['base','sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_ksc_views.xml',
        'data/product_ksc_demo.xml',
    ],
    'installable': True,
    'application': True,
}
