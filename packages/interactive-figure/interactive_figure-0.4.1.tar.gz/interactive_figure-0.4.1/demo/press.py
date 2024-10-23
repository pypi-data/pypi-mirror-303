# This demo shows all the button press registering possibilities.

from interactive_figure import interactive_figure
import matplotlib.pyplot as plt


def main():
    interactive_figure.create()
    run_demo()
    interactive_figure.close()


def run_demo():
    plt.title("Feedback will appear here.")
    interactive_figure.draw()

    while True:
        interactive_figure.wait_for_interaction()

        key = interactive_figure.get_last_key_press()
        mouse = interactive_figure.get_last_mouse_press()
        x, y = interactive_figure.get_last_mouse_pos()

        interactive_figure.clear()

        # Exit if q is pressed outside rectangle.
        if x is None or y is None:
            if key == "q":
                print("Closing...")
                return
        # Plot keys if pressed inside rectangle.
        else:
            x = round(x, 3)
            y = round(y, 3)

            if not key is None:
                plt.text(x, y, key, ha="center", va="center", fontsize="large")
            elif mouse == 1:
                plt.plot(x, y, "r.", ms=13)
            elif mouse == 2:
                plt.plot(x, y, "g.", ms=13)
            elif mouse == 3:
                plt.plot(x, y, "b.", ms=13)
            else:
                # Any other mouse button.
                plt.plot(x, y, "k.", ms=13)

        plt.title(f"key: {key}, x: {x}, y: {y}")

        interactive_figure.draw()


if __name__ == "__main__":
    main()
