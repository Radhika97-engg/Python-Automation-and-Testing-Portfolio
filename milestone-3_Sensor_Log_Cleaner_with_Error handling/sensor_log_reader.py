# sensor_log_reader.py
# Goal: Read a sensor log file, handle malformed data, and save valid records.
import os

def sensor_logger():
    # Print the current working directory 
    print("Current Working Directory:", os.getcwd())

    try:
        # Open both the input sensor log and the output clean log files
        with open('sensor_log.txt', 'r') as file, open('Clean_Sensor_Log.txt', 'w') as clean_file:

            # Initialize counters for error tracking
            malformed_count = 0
            invalid_number_count = 0

            # Loop through each line in the log file
            for line in file:
                clean_line = line.strip() 
                print(clean_line)

                try:
                    # Split line into parts and extract values
                    parts = clean_line.split(',')
                    time_stamp = parts[0].strip()
                    temperature = float(parts[1].strip())
                    pressure = float(parts[2].strip())

                # Catch lines with missing parts
                except IndexError:
                    malformed_count += 1
                    print(f"[WARNING] Incomplete line: {clean_line}")

                # Catch lines with invalid float conversions
                except ValueError:
                    invalid_number_count += 1
                    print(f"[WARNING] Invalid number in line: {clean_line}")

                else:
                    # Valid line: print and save to clean file
                    print(f"{time_stamp} ---> Temperature: {temperature} ---> Pressure: {pressure}")
                    clean_file.write(f"{time_stamp},{temperature},{pressure}\n")

            # Print final summary
            print("\nSummary Report")
            print(f"Malformed lines (IndexError): {malformed_count}")
            print(f"Invalid numbers (ValueError): {invalid_number_count}")

    # File not found error handling
    except FileNotFoundError:
        print("sensor_log.txt doesn't exist at the specified path.")

    #Confirm process end
    finally:
        print("Log processing completed.")

#Run the function
output = sensor_logger()
print(output)  # None is expected since function doesn't return a value