import requests

class WhatsApp:
    def __init__(self, access_token, phone_number_id):
        self.access_token = access_token
        self.phone_number_id = phone_number_id
        self.base_url = f'https://graph.facebook.com/v12.0/{phone_number_id}/messages'

    def send_message(self, to_number, message):
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "text",
            "text": {
                "body": message
            }
        }
        response = requests.post(self.base_url, headers=headers, json=data)
        return self.handle_response(response)

    def send_image(self, to_number, image_url, caption=None):
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "image",
            "image": {
                "link": image_url
            }
        }
        if caption:
            data['image']['caption'] = caption
        
        response = requests.post(self.base_url, headers=headers, json=data)
        return self.handle_response(response)

    def send_document(self, to_number, document_url, caption=None):
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "document",
            "document": {
                "link": document_url
            }
        }
        if caption:
            data['document']['caption'] = caption
        
        response = requests.post(self.base_url, headers=headers, json=data)
        return self.handle_response(response)

    def send_location(self, to_number, latitude, longitude, name=None, address=None):
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "location",
            "location": {
                "latitude": latitude,
                "longitude": longitude
            }
        }
        if name:
            data['location']['name'] = name
        if address:
            data['location']['address'] = address
        
        response = requests.post(self.base_url, headers=headers, json=data)
        return self.handle_response(response)

    def send_template_message(self, to_number, template_name, language_code, components=None):
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        }
        if components:
            data['template']['components'] = components

        response = requests.post(self.base_url, headers=headers, json=data)
        return self.handle_response(response)

    def handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")