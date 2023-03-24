from collections import defaultdict
import statistics

# Define dictionaries to store sensor readings
temperatures = defaultdict(list)
humidities = defaultdict(list)

# Open log file and read lines
with open('sample.log') as f:
    lines = f.readlines()

# Extract reference temperature and humidity values
ref_line = lines[0].strip().split()
ref_temperature = float(ref_line[1])
ref_humidity = float(ref_line[2])

# Define classification thresholds
TEMP_PRECISION = 5
TEMP_ULTRA_PRECISE_STDDEV = 0.5
TEMP_VERY_PRECISE_STDDEV = 3
HUMIDITY_THRESHOLD = 1

# Loop over lines and classify devices
for i, line in enumerate(lines):
    if line.startswith('thermometer'):
        # Get temperature readings
        while i+1 < len(lines) and not lines[i+1].startswith(('thermometer', 'humidity')):
            timestamp, temperature = lines[i+1].strip().split()
            temperatures[line.strip()].append(float(temperature))
            i += 1

        # Classify temperature device
        mean = statistics.mean(temperatures[line.strip()])
        stddev = statistics.stdev(temperatures[line.strip()])
        if abs(mean - ref_temperature) <= TEMP_PRECISION and stddev < TEMP_ULTRA_PRECISE_STDDEV:
            print(line.strip(), 'is ultra precise')
        elif abs(mean - ref_temperature) <= TEMP_PRECISION and stddev < TEMP_VERY_PRECISE_STDDEV:
            print(line.strip(), 'is very precise')
        else:
            print(line.strip(), 'is precise')

    elif line.startswith('humidity'):
        # Get humidity readings
        while i+1 < len(lines) and not lines[i+1].startswith(('thermometer', 'humidity')):
            timestamp, humidity = lines[i+1].strip().split()
            humidities[line.strip()].append(float(humidity))
            i += 1

        # Classify humidity device
        if all(abs(humidity - ref_humidity) <= HUMIDITY_THRESHOLD for humidity in humidities[line.strip()]):
            print(line.strip(), 'is valid')
        else:
            print(line.strip(), 'is invalid')