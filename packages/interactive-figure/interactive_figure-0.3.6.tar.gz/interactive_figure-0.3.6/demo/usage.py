# This demo is the script in the usage section.

from interactive_figure import interactive_figure

interactive_figure.create()
# Stall until user input is received.
interactive_figure.wait_for_interaction()
key = interactive_figure.get_last_key_press()
print(f"Pressed key: {key}")
interactive_figure.close()
