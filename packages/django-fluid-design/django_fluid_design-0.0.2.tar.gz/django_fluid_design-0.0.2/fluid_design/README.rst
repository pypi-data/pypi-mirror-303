django-fluid-design
===================

Summary
-------

Implements ENGIE's Fluid Design System as Django templatetags.


Quick Start
-----------

1. Add :code:`fluid_design` to your :code:`INSTALLED_APPS` settings.

2. Load template tag like this :code:`{% load fluid_design %}`.

3. Add built-in assets (js/css) :code:`{% fluid_design_assets %}`.

4. Use the components :code:`{% Pagination pager=page_obj %}`.
