.. _question-presets:

Question Presets
================

e2xauthoring comes with several question presets and the ability to add own presets.

Built-in Question Presets
-------------------------

There are 7 questions presets available with e2xauthoring.

Code (Autograded)
~~~~~~~~~~~~~~~~~

This is the preset for autograded code questions. It adds three cells:

* A read-only cell for the question
* A solution code cell for the student answer
* A test code cell for testing the student answer

Both the solution cell and test cell are already filled with nbgrader's special syntax for solution and hidden test regions.
Everything in the solution region will be removed in the student version of the question.
Everything in the hidden test region will be removed in the student version of the question.

.. figure:: img/autograded_code_question.png
    :alt: The autograded code question

    The autograded code question preset.

Code (Manual)
~~~~~~~~~~~~~

This is the preset for manually graded code questions. It adds two cells:

* A read-only cell for the question
* A solution code cell for the student answer

The solution cell is already filled with nbgrader's special syntax for solution regions.
Everything in the solution region will be removed in the student version of the question.

.. figure:: img/manual_code_question.png
    :alt: The manually graded code question

    The manually graded code question preset.

Diagram
~~~~~~~

This is the preset for diagram questions. It uses the diagram editor from `draw io <http://drawio.com>`_.
It adds two cells:

* A read-only cell for the question
* A diagram cell for the student answer


.. figure:: img/diagram_question.png
    :alt: The diagram question

    The diagram question preset (unrendered).

Render the diagram cell to see and edit the diagram.

.. figure:: img/diagram_question_rendered.png
    :alt: The rendered diagram question

    The diagram question preset (rendered).

To edit the diagram, click the *Edit Diagram* button.
You can choose if the diagram should be replaced with an empty diagram in the student version or if the pre-created diagram should be given to students.

Freetext
~~~~~~~~

This is the preset for manually graded text questions. It adds two cells:

* A read-only cell for the question
* A solution markdown cell for the student answer

.. figure:: img/freetext_question.png
    :alt: The freetext question

    The freetext question preset.

*Hint: You can use the solution regions in markdown solution cells, too.*

Multiple Choice
~~~~~~~~~~~~~~~

This is the preset for multiple choice questions. It adds a single cell:

* A markdown cell for the question and solution

.. figure:: img/multiple_choice_question.png
    :alt: The multiple choice question

    The multiple choice question preset (unrendered).

To create answers, simply write a markdown list and then render the cell. Then select the correct answers.
Students will not be able to unrender the cell.

.. figure:: img/multiple_choice_question_rendered.png
    :alt: The rendered multiple choice question 

    The multiple choice question preset (rendered).



Single Choice
~~~~~~~~~~~~~

This is the preset for single choice questions. It adds a single cell:

* A markdown cell for the question and solution

.. figure:: img/single_choice_question.png
    :alt: The single choice question

    The single choice question preset (unrendered).

To create answers, simply write a markdown list and then render the cell. Then select the correct answer.
Students will not be able to unrender the cell.

.. figure:: img/single_choice_question_rendered.png
    :alt: The rendered single choice question 

    The multiple choice question preset (rendered).

Upload Files
~~~~~~~~~~~~

This is the preset for upload questions. It stores uploaded files and images from the webcam in the notebook.
It adds two cells:

* A read-only cell for the question 
* A solution cell for the answer.

.. figure:: img/upload_question_rendered.png
    :alt: The rendered upload files question 

    The upload files question preset (rendered).

Students can upload files and take images via the webcam by clicking on the *Add Files / Images* button.
This opens the attachment editor.

.. figure:: img/attachment_editor.png
    :alt: The attachment editor

    The attachment editor. Here three images have been uploaded.

*Note: The webcam upload has not been tested across all browsers and devices and will likely not work on mobile.*

Adding Your Own Presets
-----------------------

You can add your own question presets via the nbgrader config.

A question preset is a single Jupyter notebook containing nbgrader cells.
There can only be a single solution cell in a question preset.
The name of the question preset is the name of the Jupyter notebook that contains the preset.

Assume you have a directory called ``/home/e2x/my_presets/``, containing one or more Jupyter notebooks.
To add this as new presets, add the following in your ``nbgrader_config.py``.
Make sure to add the absolute path.

.. code-block:: python
    :caption: Adding custom question presets to e2xauthoring

    # nbgrader_config.py

    # ...

    c = get_config()

    # Add a path to the preset manager
    c.PresetManager.extra_task_preset_path = "/home/e2x/my_presets/"



