# functions for the project
def rolling_avg(array, step_size):
    averaged_values = []
    i = 0
    while i < len(array):
        if (i + step_size) >= len(array):
            arr = array[i:]
            out = 0
            for val in arr:
                out += val
            averaged_values.append(out / len(arr))
        else:
            arr = array[i:i + step_size]
            out = 0
            for val in arr:
                out += val
            averaged_values.append(out / len(arr))
        i += step_size
    return averaged_values
