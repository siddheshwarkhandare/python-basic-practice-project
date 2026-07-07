
#binary search algo just revisting it 
def binary_search(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Prevents potential integer overflow in large datasets
        mid = left + (right - left) // 2  
        
        # Target found, return its index
        if arr[mid] == target:
            return mid
        # Target is larger, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # Target is smaller, ignore the right half
        else:
            right = mid - 1
            
    return -1  # Target is not present in the list

# --- Example Usage ---
sorted_data =[int(x) for x in input("enter array seprated by coma: ").split(",")]
target_value = int(input("enter target value"))

result = binary_search(sorted_data, target_value)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")
