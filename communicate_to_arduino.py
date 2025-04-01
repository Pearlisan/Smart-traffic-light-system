import serial
import time
import identify_cars

# Set up serial communication with the Arduino
try:
    arduino = serial.Serial('COM1', 9600, timeout=1)  # Ensure timeout is set
    arduino.bytesize = 8              # Number of data bits = 8
    arduino.parity = 'N'              # No parity
    arduino.stopbits = 1              # Number of Stop bits = 1
    time.sleep(2)  # Wait for the connection to establish
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

try:
    start_time = time.time()  # Track when we start

    while time.time() - start_time < 25:  # Run for 25 seconds
        # Get car count from the identify_cars.py script 
        car_count = str(identify_cars.car_count).encode()
        print(car_count)

        # Send the car count to the Arduino
        arduino.write(car_count)

        # Add a delay before the next iteration
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    print("Closing serial port...")
    
    arduino.flush()  # Ensure all data is written to the arduino
    arduino.close()  # Close the serial port
    
    if arduino.is_open:  # Check if it's still open
        print("Force closing serial port...")
        del arduino  # Delete the serial object to release the port




