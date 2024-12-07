import numpy as np
 
def numpy_operations():
    input_array = []
    
    length_of_array = int(input("Enter your array length: "))
    
    for _ in range(length_of_array):
        element = input("Enter an element: ")

        try:
            input_array.append(int(element))  # Convert to integer and append
        except ValueError:
            print("Please enter a valid number.")

    array = np.array(input_array)
    #operations
    array_plus_5 = array + 5
    array_squared = array ** 2
    mean_array = np.mean(array)
    sum_array = np.sum(array)
    sorted_array = np.sort(array)

    # Print results
    print("\nArray + 5:", array_plus_5)
    print("Array squared:", array_squared)
    print("Mean of array:", mean_array)
    print("Sum of array:", sum_array)
    print("Sorted array: ", sorted_array)
    print("\n")

if __name__ == "__main__":
    numpy_operations()