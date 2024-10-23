interactive_figure.interactive_figure
=====================================

.. py:module:: interactive_figure.interactive_figure

.. autoapi-nested-parse::

   This module provides functions to create and interact with a Matplotlib figure. The figure registers mouse presses, keyboard input and the location of the mouse
   after any input.

   Source: https://github.com/teuncm/interactive-figure



Functions
---------

.. autoapisummary::

   interactive_figure.interactive_figure.create
   interactive_figure.interactive_figure.draw
   interactive_figure.interactive_figure.clear
   interactive_figure.interactive_figure.toggle_fullscreen
   interactive_figure.interactive_figure.close
   interactive_figure.interactive_figure.wait_for_interaction
   interactive_figure.interactive_figure.get_last_key_press
   interactive_figure.interactive_figure.get_last_mouse_press
   interactive_figure.interactive_figure.get_last_mouse_pos
   interactive_figure.interactive_figure.wait


Module Contents
---------------

.. py:function:: create(hide_labels=False, hide_toolbar=False, **kwargs)

   Create the interactive figure.

   Parameters
   ----------
   hide_labels : bool, optional
       remove all labels from the figure (makes rendering *much* faster).
   hide_toolbar : bool, optional
       whether to hide the toolbar, default False.

   Remaining keyword arguments will be sent to the figure upon creation.

   Raises
   ----------
   RuntimeError
       if multiple interactive figures are created.


.. py:function:: draw()

   Draw contents of the figure.


.. py:function:: clear()

   Reset contents and layout of the figure.


.. py:function:: toggle_fullscreen()

   Toggle fullscreen.


.. py:function:: close()

   Close the figure.


.. py:function:: wait_for_interaction(timeout=-1)

   Wait for interaction. 

   Optionally use a timeout in seconds.

   Parameters
   ----------
   timeout : int, optional
       Timeout in seconds when waiting for input.

   Returns
   -------
   bool | None
       - True if a key was pressed.
       - False if a mouse button was pressed.
       - None if no input was given within the timeout.


.. py:function:: get_last_key_press()

   Get the last key press in lowercase.

   Returns
   -------
   str | None
       The last key that was pressed.


.. py:function:: get_last_mouse_press()

   Get the ID of the last mouse press.

   Returns
   -------
   int | None
       The identifier of the last mouse button that was pressed.


.. py:function:: get_last_mouse_pos()

   Get the last mouse position.

   Returns
   -------
   (x: float, y: float) | (None, None)
       The last registered mouse position after any interaction.


.. py:function:: wait(timeout)

   Freeze for the given number of seconds. 

   During this period it is not possible to interact 
   with the figure. For sub-second timeouts use time.wait() instead.

   Parameters
   ----------
   timeout : float
       Number of seconds to wait for.


