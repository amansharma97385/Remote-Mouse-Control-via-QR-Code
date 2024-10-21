import qrcode
from flask import Flask, request, render_template
import pyautogui
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Replace with your computer's IP address
computer_ip = '192.168.1.5'  # Update this with your actual IP address
port = 5000

# Function to generate QR code
def generate_qr_code():
    url = f'http://192.168.1.3:5000/'  # Update to the correct IP
    qr = qrcode.make(url)
    qr.save('mouse_control_qr.png')
    print(f"QR code generated for {url} and saved as 'mouse_control_qr.png'")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/left_click', methods=['POST'])
def left_click():
    logging.debug("Left click triggered")
    pyautogui.click()  # Simulate left mouse click
    return "Left Click", 200

@app.route('/right_click', methods=['POST'])
def right_click():
    logging.debug("Right click triggered")
    pyautogui.click(button='right')  # Simulate right mouse click
    return "Right Click", 200

@app.route('/move_mouse', methods=['POST'])
def move_mouse():
    data = request.json
    logging.debug(f"Received data: {data}")  # Log the received data
    x = data.get('x')
    y = data.get('y')
    logging.debug(f"Moving mouse to ({x}, {y})")  # Log mouse movement
    try:
        pyautogui.moveTo(x, y)  # Move the mouse cursor
        return "Mouse moved", 200
    except Exception as e:
        logging.error(f"Error moving mouse: {e}")  # Log any error
        return "Internal Server Error", 500

if __name__ == '__main__':
    generate_qr_code()  # Generate the QR code when the script runs
    app.run(host='0.0.0.0', port=port, debug=True)
