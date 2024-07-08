# -*- coding: utf-8 -*-
# © 2024 Jaime Millán <jmillan@stemdo.io>

{
    'name': 'Blue Theme',
    'description': 'A custom blue theme for Odoo',
    'version': '1.0',
    'author': 'Jaime Millán',
    'category': 'Themes/Backend',
    'depends': ['web', 'mail'],
    'data': [
        'views/base_menus.xml',
        'views/layout_templates.xml',
    ],
    'assets': {
        "web.assets_frontend": [
            "blue_theme/static/src/scss/login.scss",
        ],
        "web.assets_backend": [
            "blue_theme/static/src/xml/settings_templates.xml",
            "blue_theme/static/src/xml/top_bar_templates.xml",
            "blue_theme/static/src/scss/theme_accent.scss",
            "blue_theme/static/src/scss/navigation_bar.scss",
            "blue_theme/static/src/scss/datetimepicker.scss",
            "blue_theme/static/src/scss/theme.scss",
            "blue_theme/static/src/scss/sidebar.scss",
            "blue_theme/static/src/js/chrome/sidebar_menu.js",
            "blue_theme/static/src/js/fields/colors.js",
        ],
    },
    "installable": True,
    "auto_install": False,
    "application": False,
    "pre_init_hook": "test_pre_init_hook",
    "post_init_hook": "test_post_init_hook",
}
