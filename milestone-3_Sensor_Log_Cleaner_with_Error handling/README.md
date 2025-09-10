# Sensor Log Reader with Error Handling

A Python mini-project that reads and processes a sensor log file, handles malformed entries gracefully, and exports clean data — built after completing the `try/except` section of a Python Bootcamp.

---

**Situation:**  
In real-world validation and QA engineering, raw sensor logs often contain corrupted or malformed entries. Engineers must parse and clean this data efficiently to analyze system behavior.

**Task:**  
Develop a Python script to:
- Read sensor logs (`.txt`)
- Handle errors (`IndexError`, `ValueError`, `FileNotFoundError`)
- Filter clean records and export them to a new file

**Action:**  
- Used Python’s `try-except-else-finally` blocks for robust exception handling  
- Validated each line and extracted timestamp, temperature, and pressure  
- Logged warnings for corrupted lines and continued processing without crashing  
- Wrote clean sensor data to `Clean_Sensor_Log.txt`

**Result:**  
✔️ Clean, structured log file ready for further analysis  
✔️ Summary of malformed entries  
✔️ Modular, readable, and recruiter-facing Python code

---

## Skills Demonstrated

- File Handling in Python (`with open`)
- Exception Management (`try`, `except`, `else`, `finally`)
- Data Cleaning & Validation
- Modular & Readable Code Writing

---

## Sample Output
2025-09-09 13:10:02 ---> Temperature: 22.5 ---> Pressure: 101.2
[WARNING] Invalid Number: 2025-09-09 13:11:03,NA,100.9
[WARNING] Incomplete line: 2025-09-09 13:12:00
...
Malformed lines (IndexError): 1
Invalid Numbers (ValueError): 2


---

## Files Included

| File                    | Description                           |
|-------------------------|---------------------------------------|
| `sensor_log_reader.py`  | Main Python script                    |
| `sensor_log.txt`        | Input log file with sample data       |
| `Clean_Sensor_Log.txt`  | Output file containing clean records  |

---

## How to Run

```bash
python sensor_log_reader.py

