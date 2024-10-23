
:html_theme.sidebar_secondary.remove: true

{{ name | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}

   {% block methods %}
   {% if methods %}
   .. rubric:: {{ _('Methods') }}

   .. autosummary::
      :toctree:
      :template: custom-base-template.rst
   {% for item in methods %}
      {%- if not item.startswith('_') or item in ['__call__'] %}
         {{ name }}.{{ item }}
      {%- endif -%}
   {%- endfor %}
   {% endif %}
   {% endblock %}
