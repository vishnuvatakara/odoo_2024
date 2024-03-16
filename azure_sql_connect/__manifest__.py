# -*- coding: utf-8 -*-
#############################################################################
#
#    e-Sustavi d.o.o.
#
#    Copyright (C) 2023-TODAY e-Sustavi d.o.o.(<http://www.e-sustavi.hr>).
#    Author: e-Sustavi d.o.o.(<http://www.e-sustavi.hr>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'MS SQL Connect',
    'version': '17.0.1.0.0',
    'summary': """MS SQL Connect""",
    'description': """MS SQL Connect""",
    'category': 'Technical',
    'author': 'e-Sustavi d.o.o.',
    'company': 'e-Sustavi d.o.o.',
    'maintainer': 'e-Sustavi d.o.o.',
    'depends': [],
    'website': 'https://www.e-sustavi.hr/',
    'data': ["security/ir.model.access.csv",
             'views/sql_server.xml',
             ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}
