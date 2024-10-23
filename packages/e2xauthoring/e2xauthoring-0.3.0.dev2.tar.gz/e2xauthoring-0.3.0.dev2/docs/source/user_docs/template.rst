Templates
=========

A template is a Jupyter notebook containing special cells that define the overall structure of the worksheet.
Templates have header and footer cells, as well as student and group info cells.



Template Variables
------------------

All template cells can be customized by using template variables. To define a template variable, enclose it in double curly braces.

.. figure:: img/sample_template.png
    :alt: A template with variables

    A template with the variables ``assignment_number`` and ``due_date``.

When creating a worksheet, you can assign values to these variables.

.. figure:: img/sample_template_variables.png
    :alt: A template with variables during worksheet creation

    Creating a worksheet from the template with the variables ``assignment_number`` and ``due_date``.

Template Cells
--------------

Header Cells
~~~~~~~~~~~~

Header cells will always appear at the top of the generated worksheet.

Student / Group Info Cells
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a cell where students can put their student id or the team members when working on a group assignment.

Footer Cells
~~~~~~~~~~~~

Footer cells will always appear at the bottom of the generated worksheet.


Adding Your Own Cell Presets
----------------------------

You can add your own template cell presets via the nbgrader config.

A template preset is a single Jupyter notebook containing.
The name of the cell preset is the name of the Jupyter notebook that contains the preset.

Assume you have a directory called ``/home/e2x/my_template_presets/``, containing one or more Jupyter notebooks.
To add this as new template presets, add the following in your ``nbgrader_config.py``.
Make sure to add the absolute path.

.. code-block:: python
    :caption: Adding custom template presets to e2xauthoring

    # nbgrader_config.py

    # ...

    c = get_config()

    # Add a path to the preset manager
    c.PresetManager.extra_template_preset_path = "/home/e2x/my_template_presets/"
