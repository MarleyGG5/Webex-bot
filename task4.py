from ctypes import util
from flask import Flask, request 
from dotenv import load_dotenv   
import os
from datetime import datetime

from common.utils import create_webhook 
from webexpythonsdk import WebexAPI, Webhook

# Load environment variables from .env file for configuration
load_dotenv()

# Get the Webex Teams bot token from environment variables
WEBEX_TEAMS_ACCESS_TOKEN = os.getenv('WEBEX_TEAMS_ACCESS_TOKEN')

# Validate the access token exists
if not WEBEX_TEAMS_ACCESS_TOKEN:
    raise ValueError("WEBEX_TEAMS_ACCESS_TOKEN is not set correctly in the environment variables")

teams_api = None 
notes = {}   # Dictionary to store user notes in memory

# Initialize Flask web application
app = Flask(__name__)

# Define webhook endpoint to receive messages from Webex
@app.route('/messages_webhook', methods=['POST'])
def messages_webhook():
    if request.method == 'POST':
        webhook_obj = Webhook(request.json)  
        return process_message(webhook_obj.data)

# Main message processing function
def process_message(data):
    # Ignore messages sent by the bot itself
    if data.personId == teams_api.people.me().id:
        return '200'
    else:
        # Get the message text from Webex
        message = teams_api.messages.get(data.id).text.strip()
        
        # Add a new note
        if message.lower().startswith('/add'):
            note = message[4:].strip()  # Remove command prefix and whitespace
            # Initialize user's notes list if it doesn't exist
            if data.personEmail not in notes:
                notes[data.personEmail] = []
            # Add new note with timestamp
            notes[data.personEmail].append({
                'timestamp': datetime.now(),
                'content': note
            })
            send_direct_message(data.personEmail, f"Note saved successfully!")
        
        # Show all notes    
        elif message.lower() == '/show':
            if data.personEmail not in notes or not notes[data.personEmail]:
                send_direct_message(data.personEmail, "You don't have any saved notes.")
            else:
                # Format and display all notes with timestamps
                response = "Your saved notes:\n\n"
                for i, note in enumerate(notes[data.personEmail], 1):
                    response += f"{i}. [{note['timestamp'].strftime('%Y-%m-%d %H:%M')}] {note['content']}\n"
                send_direct_message(data.personEmail, response)
        
        # Clear all notes        
        elif message.lower() == '/clear':
            if data.personEmail in notes:
                notes[data.personEmail] = []
            send_direct_message(data.personEmail, "All notes cleared!")
        
        # Show help menu    
        elif message.lower() == '/help':
            help_text = """
Available commands:
- /add <your note> - Save a new note
- /show - Display all your saved notes
- /clear - Delete all your notes
- /help - Show this help message
"""
            send_direct_message(data.personEmail, help_text)
        
        # Handle unknown commands    
        else:
            send_direct_message(data.personEmail, "I didn't understand that command. Type '/help' to see available commands.")
            
        return '200'

def send_direct_message(person_email, message):
    teams_api.messages.create(toPersonEmail=person_email, text=message)

def send_message_in_room(room_id, message):
    teams_api.messages.create(roomId=room_id, text=message)

if __name__ == '__main__':
    teams_api = WebexAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN)
    create_webhook(teams_api, 'messages_webhook', '/messages_webhook', 'messages')
    app.run(host='0.0.0.0', port=12000)
