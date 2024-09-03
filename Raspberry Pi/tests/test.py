import serial
import time
import logging

# Setup logging
logging.basicConfig(filename='test.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def initialize_serial(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        logging.info(f"Serial port {port} opened successfully.")
        return ser
    except serial.SerialException as e:
        logging.error(f"Failed to open serial port: {e}")
        raise

def test_temperature(ser):
    ser.write(b"READ_TEMP\n")
    response = ser.readline().decode('utf-8').strip()
    if response:
        try:
            temperature = float(response)
            logging.info(f"Temperature data received: {temperature}")
            print(f"Temperature: {temperature} °C")
        except ValueError:
            logging.warning(f"Invalid temperature data received: {response}")
    else:
        logging.warning("No temperature data received.")

def test_humidity(ser):
    ser.write(b"READ_HUMI\n")
    response = ser.readline().decode('utf-8').strip()
    if response:
        try:
            humidity = float(response)
            logging.info(f"Humidity data received: {humidity}")
            print(f"Humidity: {humidity} %")
        except ValueError:
            logging.warning(f"Invalid humidity data received: {response}")
    else:
        logging.warning("No humidity data received.")

def main():
    # Hardcoded values
    port = 'COM3'  # Change to your serial port
    baudrate = 115200      # Baud rate for serial communication
    test_type = 'humidity'  # Change to 'humidity' if you want to test humidity

    ser = initialize_serial(port, baudrate)

    if test_type == "temperature":
        test_temperature(ser)
    elif test_type == "humidity":
        test_humidity(ser)
    else:
        logging.error(f"Invalid test type: {test_type}")

    ser.close()

if __name__ == "__main__":
    main()
