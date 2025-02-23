import sys
import statistics

def detect_outliers(data):
    """Identifies outliers using the 1.5*IQR rule and returns the cleaned dataset."""
    if len(data) < 2:
        return data  # If only one element, no outliers possible
    
    sorted_data = sorted(data)
    mid = len(sorted_data) // 2

    Q1 = statistics.median(sorted_data[:mid])  # First quartile
    Q3 = statistics.median(sorted_data[(mid + (len(sorted_data) % 2)):])  # Third quartile
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    cleaned_data = [x for x in data if lower_bound <= x <= upper_bound]
    return cleaned_data

def process_data(input_str):
    """Processes input data, computes statistical metrics, and identifies outliers."""
    lines = input_str.strip().split("\n")
    
    if len(lines) < 2 or not lines[0].isdigit():  # Check if input is valid
        print("Invalid input")
        return

    N = int(lines[0])  # Number of elements
    
    try:
        dataset = list(map(int, lines[1].split()))
        if len(dataset) != N:
            print("Invalid input")
            return
    except ValueError:
        print("Invalid input")
        return

    mean_value = round(statistics.mean(dataset), 2)
    median_value = round(statistics.median(dataset), 2)
    mode_value = statistics.mode(dataset)
    std_dev_value = round(statistics.stdev(dataset), 2) if len(dataset) > 1 else 0.00

    cleaned_data = detect_outliers(dataset)

    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Mode: {mode_value}")
    print(f"Standard Deviation: {std_dev_value}")

    if cleaned_data:
        print("Cleaned Dataset:", " ".join(map(str, cleaned_data)))
    else:
        print("No outliers found")

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if input_data:
        process_data(input_data)
    else:
        print("Invalid input")
