# -*- coding: utf-8 -*-
{
    'name': 'Auguria demo',
    'installed_version': '13.0.1.1',
    'author': 'Auguria SAS',
    'licence': 'LGPL Version 3',
    'summary': 'Initialize projet',
    'sequence': 15,
    'description': """
Initialize project
    """,
    'category': 'Base',
    'website': 'https://www.auguria.fr',
    'images': [],
    'depends': [
                'base',
                'crm'
        ],
    'data': [#'security/ir.model.access.csv',
#              'views/res_config_settings_view.xml',
#              'data/ir_config_parameter.xml'
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
}
