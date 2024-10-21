# This demo shows a simple reaction time measurement experiment.

from interactive_figure import interactive_figure
import matplotlib.pyplot as plt
import random
import time

TIME_LIMIT = 2
NUM_DISTRACTORS = 39


def main():
    interactive_figure.create()
    run_demo()
    interactive_figure.close()


def plot_stimulus():
    """Plot a stimulus with some distractors and a target."""
    x = [random.random()*100 for _ in range(NUM_DISTRACTORS)]
    y = [random.random()*100 for _ in range(NUM_DISTRACTORS)]

    # Plot distractors.
    plt.plot(x, y, "k.", markersize=12, markerfacecolor="none", linestyle='none')

    x = random.random()*100
    y = random.random()*100

    # Plot target.
    plt.plot(x, y, "b^", markersize=12, markerfacecolor="none", linestyle='none')


def run_demo():
    plt.title("Feedback will appear here.")
    interactive_figure.draw()

    limit_counter = 0

    while True:
        plot_stimulus()
        interactive_figure.draw()
        time_before = time.time()
        interaction_type = interactive_figure.wait_for_interaction(TIME_LIMIT)
        time_after = time.time()

        key = interactive_figure.get_last_key_press()
        x, y = interactive_figure.get_last_mouse_pos()
        dt = round(time_after - time_before, 3)

        # Exit if q is pressed outside rectangle.
        if (x is None or y is None) and key == "q":
            print("Closing...")
            return

        interactive_figure.clear()

        if interaction_type is None:
            limit_counter += 1
            if limit_counter == 1:
                plt.title(f"No input was registered within {TIME_LIMIT}s", color="red")
            else:
                plt.title(f"No input was registered within {TIME_LIMIT}s ({limit_counter})", color="red")
        else:
            limit_counter = 0
            plt.title(f"key: {key}, dt: {dt}")

        interactive_figure.draw()


if __name__ == "__main__":
    main()
