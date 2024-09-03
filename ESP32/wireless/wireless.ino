#include <WiFi.h>
#include <HardwareSerial.h>
#include <ArduinoJson.h>

const char* ssid = "BELL310";        // Replace with your WiFi SSID
const char* password = "3D7D7C4A9417"; // Replace with your WiFi password

const char* serverIP = "192.168.2.42";   // Replace with the IP address of your PC
const uint16_t serverPort = 81;     // The same port as in the Python server script

WiFiClient client;

// Define UART1 as an example
HardwareSerial MySerial(2); 

unsigned long previousSendMillis = 0;
const long sendInterval = 1000;  // Interval at which to send data (milliseconds)
unsigned long previousReconnectMillis = 0;
const long reconnectInterval = 10000;  // Interval at which to attempt reconnection (milliseconds)

void setup() {
    Serial.begin(115200);

    // Connect to Wi-Fi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");

    // Connect to the server
    if (client.connect(serverIP, serverPort)) {
        Serial.println("Connected to the server");
    } else {
        Serial.println("Connection to server failed");
    }

    MySerial.begin(115200, SERIAL_8N1, 16, 17); // Baud rate should match the receiver's settings
    delay(1000);
}

void loop() {
    unsigned long currentMillis = millis();

    // Handle sending data to the server
    if (client.connected()) {
        if (currentMillis - previousSendMillis >= sendInterval) {
            previousSendMillis = currentMillis;

            // Check if there's new data to send
            if (MySerial.available()) {
                String Buffer = MySerial.readString();
                Serial.println(Buffer);
                
                String sensorData = Buffer;
                
                // Send data to the server
                client.println(sensorData);
                Serial.println("Data sent: " + sensorData);
            }
        }

        // Handle receiving data from the server
        if (client.available()) {
            String receivedData = client.readStringUntil('\n');
            Serial.println("Received data: " + receivedData);

            // Parse the JSON data
            StaticJsonDocument<200> doc;
            DeserializationError error = deserializeJson(doc, receivedData);

            if (error) {
                Serial.print(F("deserializeJson() failed: "));
                Serial.println(error.f_str());
                return;
            }

            // Accessing values from the JSON
            int error_code = doc["error_code"];
            const char* time = doc["time"];
            const char* temperature = doc["temperature"];
            const char* humidity = doc["humidity"];
            const char* uv_index = doc["uv_index"];
            const char* moisture = doc["moisture"];
            const char* general = doc["general"];

            // Print the values
            Serial.printf("Error Code: %d\n", error_code);
            Serial.printf("Time: %s\n", time);
            Serial.printf("Temperature: %s\n", temperature);
            Serial.printf("Humidity: %s\n", humidity);
            Serial.printf("UV Index: %s\n", uv_index);
            Serial.printf("Moisture: %s\n", moisture);
            Serial.printf("General: %s\n", general);

            // Format the data as a comma-separated string
            String dataToSend = String(error_code) + "," + time + "," + temperature + "," +
                                humidity + "," + uv_index + "," + moisture + "," + general;
            
            // Ensure the string is exactly 100 characters long by padding with spaces
            while (dataToSend.length() < 500) {
              dataToSend += "/";
            }
            
            // Send the formatted string to the STM32 over UART
            MySerial.println(dataToSend);

        }
    } else {
        // Attempt reconnection only if enough time has passed
        if (currentMillis - previousReconnectMillis >= reconnectInterval) {
            previousReconnectMillis = currentMillis;
            
            // Reconnect to the server
            if (client.connect(serverIP, serverPort)) {
                Serial.println("Reconnected to server");
            } else {
                Serial.println("Reconnection failed");
            }
        }
    }
}

/*

#include <HardwareSerial.h>

// Define UART1 as an example
HardwareSerial MySerial(2); 

void setup() {
  
  // Initialize MySerial for UART1 communication
  MySerial.begin(115200, SERIAL_8N1, 16, 17); // Baud rate should match the receiver's settings

  // Initialize Serial for USB communication
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  // Send data through MySerial
  if (MySerial.available()) {
    String Buffer = MySerial.readString();
    Serial.println(Buffer);
  }
  MySerial.print("HELLO\n");
  delay(3000);
} */
