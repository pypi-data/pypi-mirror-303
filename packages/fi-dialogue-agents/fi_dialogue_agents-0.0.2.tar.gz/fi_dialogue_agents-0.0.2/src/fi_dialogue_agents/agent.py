from flask import Flask
from flask_socketio import SocketIO, emit

class Agent:
    def __init__(self, host="0.0.0.0", port=5001, cors_allowed_origins="*"):
        """Initialize the Flask app and SocketIO"""
        self.app = Flask(__name__)
        self.socketio = SocketIO(self.app, cors_allowed_origins=cors_allowed_origins)
        self.host = host
        self.port = port

        # User-provided functions for message handling and typing events
        self.on_message_handler = None
        self.on_typing_start_handler = None
        self.on_typing_stop_handler = None

        # Register event handler for user messages
        self.socketio.on_event('user_message', self._handle_user_message)

    def on_message(self, handler):
        """Set the function that handles user messages"""
        self.on_message_handler = handler

    def on_typing_start(self, handler):
        """Set the function to be called when typing starts"""
        self.on_typing_start_handler = handler

    def on_typing_stop(self, handler):
        """Set the function to be called when typing stops"""
        self.on_typing_stop_handler = handler

    def send_message(self, message):
        """Send a message to the client"""
        emit('bot_response', message)

    def start_typing(self):
        """Emit typing start event to the client"""
        emit('agent_typing')

    def stop_typing(self):
        """Emit typing stop event to the client"""
        emit('agent_stop_typing')

    def _handle_user_message(self, message):
        """Internal method to handle incoming messages"""
        print(f"Received message: {message}")
        
        if self.on_typing_start_handler:
            self.on_typing_start_handler()  # Call user's typing start handler
        
        if self.on_message_handler:
            # Process the message using the user-defined handler
            response = self.on_message_handler(message)
            self.send_message(response)
        
        if self.on_typing_stop_handler:
            self.on_typing_stop_handler()  # Call user's typing stop handler

    def run(self):
        """Start the SocketIO server"""
        self.socketio.run(self.app, host=self.host, port=self.port)
