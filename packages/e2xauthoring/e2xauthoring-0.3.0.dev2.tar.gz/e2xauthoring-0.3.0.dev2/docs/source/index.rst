.. e2xauthoring documentation master file, created by
   sphinx-quickstart on Tue Aug 22 15:54:37 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

e2xauthoring Documentation
==========================

Welcome to the **e2xauthoring** documentation site. e2xauthoring streamlines assignment creation for nbgrader by utilizing reusable components known as *tasks* and *templates*.

* **Seamless Integration with e2xgrader:** e2xauthoring integrates with e2xgrader, enhancing the process of creating nbgrader assignments.
* **Efficient Worksheet Creation:** Generate assignments by crafting Jupyter notebook-based worksheets, which serve as individual assignment units.
* **Flexible Templates:** Utilize customizable templates for worksheets, defining headers and footers. Templates can incorporate variables, which are populated during worksheet creation.
* **Task-Centric Approach:** Design assignments with reusable tasks, where each task is a small Jupyter notebook containing related questions (e.g., Task 1, Task 1.1).
* **Question Presets:** Use a dedicated toolbar to insert question presets into tasks. You can extend functionality by adding your own question presets.
* **Task Pools:** Group tasks logically into task pools, providing a structured overview of assignment components.
* **Version Control Ready:** Convert task pools into Git repositories, facilitating version control for collaboration and iteration.
* **Worksheet Customization:** Assemble worksheets by selecting templates, filling variables, and picking tasks to include, tailoring assignments to specific needs.

Screenshots
-----------

To get a better idea of how e2xauthoring looks like, here are some screenshots.

.. figure:: user_docs/img/assignments.png
    :alt: Assignments Page
    :scale: 50%

    Assignments

.. figure:: user_docs/img/tasks.png
    :alt: Tasks Page
    :scale: 50%

    Tasks

.. figure:: user_docs/img/templates.png
    :alt: Templates Page
    :scale: 50%

    Templates

.. figure:: user_docs/img/add_question.png
    :alt: Creating a Task
    :scale: 50%

    Creating a Task

.. toctree::
   :maxdepth: 2
   :caption: User Documentation:

   user_docs/index

.. toctree::
   :maxdepth: 2
   :caption: Setup:

   setup/index





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
