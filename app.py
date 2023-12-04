import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('login_response')
def on_login_response(data):
    print(f'Login Response: {data["data"]}')

@sio.on('midi_signal')
def on_midi_signal(data):
    signal_type = data['type']
    midi_data = data['data']
    print(f'Received MIDI Signal - Type: {signal_type}, Data: {midi_data}')

# Replace 'http://0.0.0.0:25465' with the actual URL where your server is running
sio.connect('http://localhost:25550')

# Add your additional client logic here

# This blocks the script from exiting immediately, keeping the connection alive
try:
    sio.wait()
except KeyboardInterrupt:
    print("Closing connection.")
    sio.disconnect()