{{ '#' * (cookiecutter.module_name|replace('_', ' ')|title|length + 7) }}
{{ cookiecutter.module_name.replace('_', ' ').title() }} Module
{{ '#' * (cookiecutter.module_name|replace('_', ' ')|title|length + 7) }}

.. toctree::
   :maxdepth: 2

   usage
   design
   releases
