# MIDI Signal Receiver

## Overview

This is the MidiFlex script that uses the `socketio` library to connect to the MidiFlex Server and receive MIDI signals. The script listens for events such as connection, login response, and MIDI signals, and prints the relevant information to the console. ***(In the Future, receive and send Midi Singals from/to the Server)***

## Setup

### 1. Clone the Repository:

```bash
git clone https://github.com/Technik-AG-STG/MidiFlex-Client.git
cd MidiFlex-Client
```

### 2. Install Dependencies:

- Ensure you have Python 3.8.10 installed. Then, install the required dependencies using:
- ***In some cases it may be the case that Python modules have to have exactly the same version.***

```bash
pip install -r requirements.txt
```

### 3. Run the Script:

Replace 'http://localhost:25550' with the actual URL where your MidiFlex Server is running. Then, run the script:

```bash
python app.py
```

The script will connect to the specified server and start printing information to the console.

### Closing the Connection

To gracefully close the connection, press Ctrl+C in the terminal where the script is running. The script will print "Closing connection" before disconnecting from the server.

## Client Logic

In the future, the midiflex client will be able to receive midi signals and output them virtually, but also send signals back to the server.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
