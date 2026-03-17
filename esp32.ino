#include <WiFi.h>

const char* ssid = "Glad's";
const char* password = "gdx1234.";
const char* host = "10.226.146.186";   // Python server IP
const int port = 5000;

#define FAN_A 5
#define FAN_B 2
#define FAN_C 0
#define LED_A 15
#define LED_B 16
#define CLASS_LIGHT 14
#define LDR_PIN 34

// PWM settings
const int freq = 5000;
const int res = 8;

WiFiClient client;

// LDR smoothing
int smoothLDR = 0;

void setup() {

  Serial.begin(115200);

  // PWM setup
  ledcAttach(FAN_A, freq, res);
  ledcAttach(FAN_B, freq, res);
  ledcAttach(FAN_C, freq, res);

  ledcAttach(LED_A, freq, res);
  ledcAttach(LED_B, freq, res);

  ledcAttach(CLASS_LIGHT, freq, res);

  // Connect WiFi
  WiFi.begin(ssid, password);

  Serial.print("Connecting WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected!");
}

void loop() {

  if (!client.connected()) {

    Serial.println("Connecting to Python Server...");

    if (client.connect(host, port)) {
      Serial.println("Connected to Python Server!");
    } 
    else {
      delay(2000);
      return;
    }
  }

  if (client.available()) {

    String data = client.readStringUntil('\n');
    data.trim();

    int c1 = data.indexOf(',');
    int c2 = data.indexOf(',', c1 + 1);
    int c3 = data.indexOf(',', c2 + 1);
    int c4 = data.indexOf(',', c3 + 1);

    if (c1 != -1 && c4 != -1) {

      int fanA = data.substring(0, c1).toInt();
      int fanB = data.substring(c1 + 1, c2).toInt();
      int fanC = data.substring(c2 + 1, c3).toInt();
      int ledA = data.substring(c3 + 1, c4).toInt();
      int ledB = data.substring(c4 + 1).toInt();

      // Fan speed
      ledcWrite(FAN_A, fanA);
      ledcWrite(FAN_B, fanB);
      ledcWrite(FAN_C, fanC);

      // LED ON / OFF
      ledcWrite(LED_A, ledA ? 255 : 0);
      ledcWrite(LED_B, ledB ? 255 : 0);

      Serial.printf("FanA:%d FanB:%d FanC:%d LEDA:%d LEDB:%d\n",
                    fanA, fanB, fanC, ledA, ledB);
    }
  }


  int ldrValue = analogRead(LDR_PIN);

  // smoothing filter
  smoothLDR = (smoothLDR * 4 + ldrValue) / 5;

  Serial.print("LDR Value: ");
  Serial.println(smoothLDR);

  // better brightness mapping
  int brightness = map(smoothLDR, 300, 3000, 255, 0);
  brightness = constrain(brightness, 0, 255);

  ledcWrite(CLASS_LIGHT, brightness);

  delay(20);
}