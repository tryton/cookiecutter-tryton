{% if not cookiecutter.prefix -%}
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

{% endif -%}
try:
    from trytond.modules.{{ cookiecutter.module_name }}.tests.test_{{ cookiecutter.module_name }} import suite  # noqa: E501
except ImportError:
    from .test_{{ cookiecutter.module_name }} import suite

__all__ = ['suite']
