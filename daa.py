import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Bubble Sort as a generator for visualization
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

# Quick Sort helper - recursive, but to visualize, we use a generator
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        yield from quick_sort(arr, low, pivot_index - 1)
        yield from quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        yield arr
    arr[i], arr[high] = arr[high], arr[i]
    yield arr
    return i

# Visualizer function
def visualize_sorting(algorithm, data):
    title = "Bubble Sort" if algorithm == "bubble" else "Quick Sort"
    generator = bubble_sort(data) if algorithm == "bubble" else quick_sort(data, 0, len(data)-1)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(data)), data, align="edge")
    ax.set_title(title)
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, int(1.1 * max(data)))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    def update_plot(arr):
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Iterations: {iteration[0]}")

    ani = animation.FuncAnimation(fig, func=update_plot, frames=generator, repeat=False, blit=False, interval=100)
    plt.show()

# Sample Data
data = [random.randint(1, 100) for _ in range(30)]

# Call the visualizer
visualize_sorting("bubble", data.copy())   # Visualize Bubble Sort
visualize_sorting("quick", data.copy())    # Visualize Quick Sort
