import time  # Import the time module to measure execution time
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy as np  # Import numpy for numerical operations (not used in this code)

# Function to measure the execution time of a given function with various input sizes
def time_complexity(func, inputs):
    execution_times = []  # List to store execution times
    input_sizes = []  # List to store the sizes of the inputs
    # Loop through each input size
    for input_ in inputs:
        start_time = time.time()  # Record the start time
        func(input_)  # Call the function with the current input size
        end_time = time.time()  # Record the end time
        execution_times.append(end_time - start_time)  # Calculate execution time and add it to the list
        input_sizes.append(input_)  # Add the input size to the list
    return execution_times, input_sizes  # Return the lists of execution times and input sizes

# Function to plot the execution times against input sizes
def plot_time_complexity(execution_times, input_sizes):
    plt.plot(input_sizes, execution_times)  # Plot the execution times
    plt.xlabel('Input Size')  # Label for the x-axis
    plt.ylabel('Execution Time (seconds)')  # Label for the y-axis
    plt.title('Time Complexity')  # Title of the plot
    plt.show()  # Display the plot

# Sample function to measure; it performs a simple loop up to n
def my_function(n):
    for i in range(n):  # Loop from 0 to n-1
        pass  # Do nothing (just a placeholder)

# Define input sizes to test
inputs = [10, 100, 1000, 10000]

# Measure the execution times and input sizes
execution_times, input_sizes = time_complexity(my_function, inputs)

# Plot the execution times against input sizes
plot_time_complexity(execution_times, input_sizes)
