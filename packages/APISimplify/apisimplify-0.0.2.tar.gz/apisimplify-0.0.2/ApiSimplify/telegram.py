import requests

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.commands = {}
        self.processed_messages = set()  
        self.user_points = {}  

    def send_message(self, chat_id, text):
        """Send a message to a chat."""
        url = f"{self.base_url}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': text
        }
        response = requests.post(url, json=payload)
        return response.json()

    def set_webhook(self, webhook_url):
        """Set a webhook for the bot."""
        url = f"{self.base_url}/setWebhook"
        payload = {
            'url': webhook_url
        }
        response = requests.post(url, json=payload)
        return response.json()

    def get_updates(self):
        """Get the latest updates from the bot."""
        url = f"{self.base_url}/getUpdates"
        response = requests.get(url)
        return response.json()

    def add_command(self, command_name, response):
        """Add a new command and its response to the bot."""
        self.commands[command_name] = response  

    def handle_command(self, command, chat_id):
        """Handle a command and return a response."""
        if command in self.commands:
            return self.commands[command](chat_id)  
        return "I don't understand that command."

    def add_user_points(self, chat_id, points):
        """Add points to a user's balance."""
        if chat_id in self.user_points:
            self.user_points[chat_id] += points  
        else:
            self.user_points[chat_id] = points  

    def process_updates(self):
        """Process updates from Telegram and respond to commands."""
        updates = self.get_updates()
        for update in updates.get('result', []):
            if 'message' in update and 'text' in update['message']:
                chat_id = update['message']['chat']['id']
                command = update['message']['text']

                if command not in self.processed_messages:
                    response_text = self.handle_command(command, chat_id)
                    self.send_message(chat_id, response_text)
                    self.processed_messages.add(command)