# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': """
        School Data Create
        """,

    'description': """
      School
    """,

    'author': "Saidul Islam",
    'version': '15.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #securtiy
        "security/ir.model.access.csv",

        #views
        "views/student.xml",
        'views/teacher.xml',
        'views/course.xml',
        'views/section.xml',
        'views/registration.xml',
        
        #menus
        "views/menu.xml",


    ],
    # only loaded in demonstration mode

}
