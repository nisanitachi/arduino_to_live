import random
import matplotlib
import matplotlib.pyplot as plt
import io
import time
from flask import Flask, render_template, Response, stream_with_context

# Use the 'Agg' backend to avoid Tkinter issues
matplotlib.use('Agg')

app = Flask(__name__)

# Simulated data storage
x_vals = []
ecg_data = []
ppg_data = []

# Function to simulate data generation
def simulate_data():
    # Simulate PPG and ECG data as random values between 0 and 500
    ppg_value = random.uniform(0, 500)
    ecg_value = random.uniform(0, 500)
    
    # Update data lists
    x_vals.append(len(x_vals) + 1)
    ppg_data.append(ppg_value)
    ecg_data.append(ecg_value)

# Function to generate and update the plot
def update_plot():
    simulate_data()

    fig, (ax1, ax2) = plt.subplot(2, 1,figsize=(12,8))  # Create two subplots

    # Plot PPG data
    ax1.plot(x_vals, ppg_data, label='PPG', color='blue')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('PPG Values')
    ax1.legend(loc='upper right')
    ax1.set_title('PPG Data')

    # Plot ECG data
    ax2.plot(x_vals, ecg_data, label='ECG', color='red')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('ECG Values')
    ax2.legend(loc='upper right')
    ax2.set_title('ECG Data')
    

    # Save plot to a BytesIO object
    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot.png')
def plot_png():
    # Update plot and serve as an image
    output = update_plot()
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/data_stream')
def data_stream():
    def generate():
        while True:
            simulate_data()
            yield f"data: {ppg_data[-1]},{ecg_data[-1]}\n\n"
            time.sleep(1)  # Adjust the sleep time to control the update rate
    return Response(stream_with_context(generate()), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run()
