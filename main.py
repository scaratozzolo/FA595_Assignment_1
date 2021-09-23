import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Main function. Graphs one period of sine and cosine on the same axis.
    """
    # Create our array of x values
    x = np.linspace(-np.pi, np.pi)

    # plot x and sin(x)
    plt.plot(x, np.sin(x))

    # plot x and cos(x)
    plt.plot(x, np.cos(x))

    #Add title and labels
    plt.title("Graph of Sine and Cosine")
    plt.xlabel("Radians")

    # Show graph in matplotlib gui
    plt.show()


if __name__ == '__main__':

    main()