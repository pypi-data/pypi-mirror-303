"""
This module provides functions to create and interact with a Matplotlib figure. The figure registers mouse presses, keyboard input and the location of the mouse
after any input.

Source: https://github.com/teuncm/interactive-figure
"""

import matplotlib.pyplot as plt
from types import SimpleNamespace
import sys


def create(hide_labels=False, hide_toolbar=False, **kwargs):
    """Create the interactive figure.

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
    """
    if _state.fig is None:
        if hide_toolbar:
            plt.rcParams["toolbar"] = "None"

        if hide_labels:
            _state.hide_labels = True

        # Disable interactive mode for explicit control over drawing. See:
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.isinteractive.html#matplotlib.pyplot.isinteractive
        plt.ioff()

        _state.fig = fig = plt.figure(**kwargs)
        fig.canvas.manager.set_window_title("Interactive Figure")
        # Create drawable axis.
        _state.ax = ax = plt.gca()

        # Show figure but allow the main thread to continue.
        plt.show(block=False)

        # Reset plot state and draw to obtain focus.
        clear()
        draw()

        # Add our custom event handlers. For handlers, see:
        # https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect
        # For general interaction handling, see:
        # https://matplotlib.org/stable/users/explain/figure/interactive_guide.html
        # For mouse buttons, see:
        # https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton
        fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)
        fig.canvas.mpl_disconnect(fig.canvas.manager.button_press_handler_id)
        fig.canvas.mpl_connect("key_press_event", _key_press_handler)
        fig.canvas.mpl_connect("button_press_event", _button_press_handler)
        fig.canvas.mpl_connect("close_event", _close_handler)

        print("Interactive figure: created")
    else:
        raise RuntimeError("Interactive figure: ERROR - you cannot create multiple figures")


def draw():
    """Draw contents of the figure."""
    _check_exists()

    canvas = _state.fig.canvas
    # Mark canvas for a draw.
    canvas.draw_idle()
    # Force update the GUI. This is when the drawing actually happens
    # in the backend.
    canvas.flush_events()


def clear():
    """Reset contents and layout of the figure."""
    _check_exists()

    ax = _state.ax
    ax.clear()

    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])

    if _state.hide_labels:
        ax.set_xticks([])
        ax.set_yticks([])


def toggle_fullscreen():
    """Toggle fullscreen."""
    _check_exists()

    _state.fig.canvas.manager.full_screen_toggle()


def close():
    """Close the figure."""
    _check_exists()

    _state.closed_using_ui = False
    plt.close(_state.fig)

    # Handle proper closure so that the figure can be reused.
    _state_reset_fig()
    _state_reset_press()


def wait_for_interaction(timeout=-1):
    """Wait for interaction. 
    
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
    """
    _check_exists()

    # Reimplementation of:
    # figure.Figure.waitforbuttonpress()
    # _blocking_input.blocking_input_loop()
    #     but without show() to prevent redrawing the figure.

    # Contains the event that was registered.
    event = None

    # Handler to stop blocking event loop.
    def simple_handler(ev):
        nonlocal event
        event = ev
        _state.fig.canvas.stop_event_loop()

    # Connect event handlers and save callback ids.
    callback_ids = [
        _state.fig.canvas.mpl_connect(name, simple_handler) for name in ["button_press_event", "key_press_event"]
    ]
    try:
        # Start a blocking event loop.
        _state.fig.canvas.start_event_loop(timeout=timeout)
    finally:
        # Disconnect handlers.
        for callback_id in callback_ids:
            _state.fig.canvas.mpl_disconnect(callback_id)

    interaction_type = None if event is None else event.name == "key_press_event"

    if interaction_type is None:
        # No button was pressed, so reset the press state.
        _state_reset_press()

    return interaction_type


def get_last_key_press():
    """Get the last key press in lowercase.

    Returns
    -------
    str | None
        The last key that was pressed.
    """
    _check_exists()

    key_string = _state.last_keypress

    if key_string is None:
        return None
    else:
        return key_string.lower()


def get_last_mouse_press():
    """Get the ID of the last mouse press.

    Returns
    -------
    int | None
        The identifier of the last mouse button that was pressed.
    """
    _check_exists()

    mouse_button = _state.last_mousepress

    if mouse_button is None:
        return None
    else:
        return mouse_button.value


def get_last_mouse_pos():
    """Get the last mouse position.

    Returns
    -------
    (x: float, y: float) | (None, None)
        The last registered mouse position after any interaction.
    """
    _check_exists()

    return (_state.last_mouse_x, _state.last_mouse_y)


def wait(timeout):
    """Freeze for the given number of seconds. 
    
    During this period it is not possible to interact 
    with the figure. For sub-second timeouts use time.wait() instead.

    Parameters
    ----------
    timeout : float
        Number of seconds to wait for.
    """
    _check_exists()

    _state.fig.canvas.start_event_loop(timeout=timeout)
    # Reset the press state.
    _state_reset_press()


# HIDDEN METHODS


def _get_state():
    """Get all state information of the interactive figure.

    Returns
    -------
    SimpleNamespace
        Namespace with figure state information
    """
    return _state


def _check_exists():
    """Check if the interactive figure exists.

    Raises
    ------
    RuntimeError
        If the figure is not available
    """
    if _state.fig is None:
        raise RuntimeError("Interactive figure: ERROR - figure is not available")


def _state_reset_fig():
    """Reset figure information."""
    _state.fig = None
    _state.ax = None
    _state.hide_labels = False
    _state.closed_using_ui = True


def _state_reset_press():
    """Reset last registered press information."""
    _state.last_keypress = None
    _state.last_mousepress = None
    _state.last_mouse_x = None
    _state.last_mouse_y = None


def _key_press_handler(event):
    """Register key and mouse coordinates on press.

    Parameters
    ----------
    event
        The event object that was generated internally
    """
    _state.last_keypress = event.key
    _state.last_mousepress = None
    _state.last_mouse_x = event.xdata
    _state.last_mouse_y = event.ydata


def _button_press_handler(event):
    """Register key, mouse button and mouse coordinates on press.

    Parameters
    ----------
    event
        The event object that was generated internally
    """
    _state.last_keypress = event.key
    _state.last_mousepress = event.button
    _state.last_mouse_x = event.xdata
    _state.last_mouse_y = event.ydata


def _close_handler(event):
    """Exit when the user presses the red x to close the figure
    to prevent an infinite event loop.
    
    Parameters
    ----------
    event
        The event object that was generated internally
    """
    print("Interactive figure: closed")

    # Triggered if the UI ('the red x') is used to close the figure.
    if _state.closed_using_ui:
        print("Interactive figure: exited script")       
        sys.exit(0)


# Namespace to track the internal state of the interactive figure.
_state = SimpleNamespace(
    fig=None,
    ax=None,
    hide_labels=False,
    closed_using_ui=True,
    last_keypress=None,
    last_mousepress=None,
    last_mouse_x=None,
    last_mouse_y=None,
)
