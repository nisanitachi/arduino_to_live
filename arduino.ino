const int numReadings  = 5;
  
float ppg_avg;
float ecg_avg;
float ecg[numReadings] = {0, 0, 0, 0, 0};
float ppg[numReadings] = {0, 0, 0, 0, 0};
int count, i;

void setup() {
    Serial.begin(115200);  // Set comm speed for serial plotter window
    Serial.println("ppg,ecg");
}

void loop() {
    // Shift old values and read new values
    for (i = 0; i < numReadings - 1; i++) {
        ppg[i] = ppg[i + 1];
        ecg[i] = ecg[i + 1];
    }

    ppg[numReadings - 1] = analogRead(A1);
    ecg[numReadings - 1] = analogRead(A0);

    // Calculate the average
    ppg_avg = 0;
    ecg_avg = 0;

    for (i = 0; i < numReadings; i++) {
        ppg_avg += ppg[i];
        ecg_avg += ecg[i];
    }

    ppg_avg /= numReadings;
    ecg_avg /= numReadings;

    // Print data in CSV format
    Serial.print(ppg_avg);
    Serial.print(", ");
    Serial.println(ecg_avg);

    delay(1000 / 125);  // Delay to match sampling frequency of 125 Hz
