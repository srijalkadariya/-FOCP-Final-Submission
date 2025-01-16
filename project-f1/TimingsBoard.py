import statistics  # For calculating statistical data like mean
from tabulate import tabulate  # For displaying data in a table format

def parse_lap_files(lap_files):
    """Parses multiple lap time files and returns location and lap data."""
    combined_lap_data = {}  # Dictionary to store lap data for each driver
    location = None  # Initialize location as None

    # Iterate through each lap time file
    for file_path in lap_files:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()  # Read all lines from the file
        except FileNotFoundError:  # Handle missing file
            print(f"Error: File '{file_path}' not found.")
            return None, None

        # First line of the file contains the location
        if location is None:
            location = lines[0].strip()  # Set the location from the first file

        # Process the remaining lines for lap data
        for line in lines[1:]:
            try:
                # Extract driver code (first 3 characters) and lap time (remaining part)
                code = line[:3]  # Driver code (e.g., "HAM")
                lap_time = float(line[3:])  # Lap time as a floating-point number
                # Add lap time to the dictionary for the respective driver
                combined_lap_data.setdefault(code, []).append(lap_time)
            except ValueError:  # Handle malformed lines
                print(f"Warning: Skipping malformed line in file '{file_path}': {line.strip()}")

    return location, combined_lap_data  # Return the location and the parsed lap data

def load_driver_details(file_path):
    """Loads driver details from a file."""
    driver_details = {}  # Dictionary to store driver details
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    # Parse each line for driver information
                    car_number, code, name, team = line.strip().split(',')
                    # Store the details in a dictionary with the driver code as the key
                    driver_details[code.strip()] = {
                        "team": team.strip(),
                        "car_number": car_number.strip(),
                        "name": name.strip()
                    }
                except ValueError:  # Handle malformed lines
                    print(f"Warning: Skipping malformed line in driver details file: {line.strip()}")
    except FileNotFoundError:  # Handle missing file
        print(f"Error: Driver details file '{file_path}' not found.")
        return None
    
    return driver_details  # Return the driver details dictionary

def calculate_statistics(lap_data):
    """Calculates statistics based on the lap data."""
    # Find the fastest lap for each driver
    fastest_laps = {code: min(times) for code, times in lap_data.items()}
    # Find the average lap time for each driver
    average_laps = {code: statistics.mean(times) for code, times in lap_data.items()}
    # Find the overall average lap time across all drivers
    overall_average = statistics.mean([time for times in lap_data.values() for time in times])
    
    return fastest_laps, average_laps, overall_average  # Return calculated statistics

def display_results(location, lap_data, fastest_laps, average_laps, overall_average, driver_details):
    """Displays the processed results."""
    print(f"Grand Prix Location: {location}\n")  # Display the location of the race
    
    # Prepare data for tabulation
    table_data = []
    # Sort drivers by their fastest lap in descending order
    sorted_drivers = sorted(fastest_laps.items(), key=lambda x: x[1], reverse=True)

    # Populate the table data with driver information and lap statistics
    for code, fastest in sorted_drivers:
        name = driver_details.get(code, {}).get('name', 'Unknown')  # Get driver name
        team = driver_details.get(code, {}).get('team', 'Unknown')  # Get driver team
        car_number = driver_details.get(code, {}).get('car_number', 'N/A')  # Get car number
        avg_time = average_laps[code]  # Get average lap time
        total_laps = len(lap_data[code])  # Get total laps recorded
        # Add a row to the table data
        table_data.append([code, name, team, car_number, f"{fastest:.3f}", f"{avg_time:.3f}", total_laps])
    
    # Display the driver performance table
    headers = ["Code", "Name", "Team", "Car #", "Fastest Lap", "Avg Lap Time", "Total Laps"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))  # Print table with headers and data
    
    # Identify the driver with the fastest lap time
    fastest_driver_code, fastest_lap_time = min(fastest_laps.items(), key=lambda x: x[1])
    fastest_driver = driver_details.get(fastest_driver_code, {})  # Get details of the fastest driver
    fastest_driver_name = fastest_driver.get('name', 'Unknown')  # Get driver name
    fastest_driver_team = fastest_driver.get('team', 'Unknown')  # Get driver team

    # Display the driver with the fastest lap
    print("\nDriver with the Fastest Lap time:")
    fastest_lap_table = [
        [fastest_driver_code, fastest_driver_name, fastest_driver_team, f"{fastest_lap_time:.3f}"]
    ]
    fastest_lap_headers = ["Code", "Name", "Team", "Fastest Lap"]
    print(tabulate(fastest_lap_table, headers=fastest_lap_headers, tablefmt="grid"))  # Print table
    
    # Display the overall average lap time
    print("\nOverall Average Lap Time:", f"{overall_average:.3f}")

def main():
    # File paths
    drivers_file = "drivers.txt"  # File containing driver details
    lap_files = [  # List of files containing lap times
        "lap_times_1.txt",
        "lap_times_2.txt",
        "lap_times_3.txt",
    ]
    
    driver_details = load_driver_details(drivers_file)  # Load driver details
    if not driver_details:  # If driver details are not loaded, exit
        return

    location, lap_data = parse_lap_files(lap_files)  # Parse lap time files
    if not location or not lap_data:  # If lap data or location is missing, exit
        return

    # Calculate statistics from the lap data
    fastest_laps, average_laps, overall_average = calculate_statistics(lap_data)
    # Display the results
    display_results(location, lap_data, fastest_laps, average_laps, overall_average, driver_details)

# Entry point of the program
if __name__ == "__main__":
    main()
