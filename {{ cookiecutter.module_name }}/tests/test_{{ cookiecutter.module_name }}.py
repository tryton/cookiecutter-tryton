{% if not cookiecutter.prefix -%}
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

{% endif -%}
import unittest
{% if cookiecutter.test_with_scenario %}
import doctest
{%- endif %}

from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite
{%- if cookiecutter.test_with_scenario %}
from trytond.tests.test_tryton import doctest_setup, doctest_teardown
{%- endif %}


class {{ cookiecutter.module_name.replace('_', ' ').title().replace(' ', '') }}TestCase(ModuleTestCase):
    'Test {{ cookiecutter.module_name.replace('_', ' ').title() }} module'
    module = '{{ cookiecutter.module_name }}'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            {{ cookiecutter.module_name.replace('_', ' ').title().replace(' ', '') }}TestCase))
    {%- if cookiecutter.test_with_scenario %}
    suite.addTests(doctest.DocFileSuite(
            'scenario_{{ cookiecutter.module_name }}.rst',
            setUp=doctest_setup, tearDown=doctest_teardown, encoding='utf-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    {%- endif %}
    return suite
