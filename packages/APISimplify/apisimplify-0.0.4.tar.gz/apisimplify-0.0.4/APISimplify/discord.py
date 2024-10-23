import requests
import time
import json
from discord import DISCORD_PERMISSION_VALUES

class Discord:
    def __init__(self, user_token):
        self.user_token = user_token
        self.base_url = "https://discord.com/api/v10"
        
    DISCORD_PERMISSION_VALUES = {
        "CREATE_INSTANT_INVITE": 0x1,
        "KICK_MEMBERS": 0x2,
        "BAN_MEMBERS": 0x4,
        "ADMINISTRATOR": 0x8,
        "MANAGE_CHANNELS": 0x10,
        "MANAGE_GUILD": 0x20,
        "ADD_REACTIONS": 0x40,
        "VIEW_AUDIT_LOG": 0x80,
        "PRIORITY_SPEAKER": 0x100,
        "STREAM": 0x200,
        "VIEW_CHANNEL": 0x400,
        "SEND_MESSAGES": 0x800,
        "SEND_TTS_MESSAGES": 0x1000,
        "MANAGE_MESSAGES": 0x2000,
        "EMBED_LINKS": 0x4000,
        "ATTACH_FILES": 0x8000,
        "READ_MESSAGE_HISTORY": 0x10000,
        "MENTION_EVERYONE": 0x20000,
        "USE_EXTERNAL_EMOJIS": 0x40000,
        "VIEW_GUILD_INSIGHTS": 0x80000,
        "CONNECT": 0x100000,
        "SPEAK": 0x200000,
        "MUTE_MEMBERS": 0x400000,
        "DEAFEN_MEMBERS": 0x800000,
        "MOVE_MEMBERS": 0x1000000,
        "USE_VAD": 0x2000000,
        "CHANGE_NICKNAME": 0x4000000,
        "MANAGE_NICKNAMES": 0x8000000,
        "MANAGE_ROLES": 0x10000000,
        "MANAGE_WEBHOOKS": 0x20000000,
        "MANAGE_EMOJIS_AND_STICKERS": 0x40000000,
        "USE_APPLICATION_COMMANDS": 0x80000000,
        "REQUEST_TO_SPEAK": 0x100000000,
        "MANAGE_EVENTS": 0x200000000,
        "MANAGE_THREADS": 0x400000000,
        "CREATE_PUBLIC_THREADS": 0x800000000,
        "CREATE_PRIVATE_THREADS": 0x1000000000,
        "USE_EXTERNAL_STICKERS": 0x2000000000,
        "SEND_MESSAGES_IN_THREADS": 0x4000000000,
        "START_EMBEDDED_ACTIVITIES": 0x8000000000,
        "MODERATE_MEMBERS": 0x10000000000
    }
    
    def get_user(self):
        url = f"{self.base_url}/users/@me"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)
        user_profile = response.json()

        if 'id' in user_profile:
            print("User Profile:")
            print(f"User ID: {user_profile['id']}")
            print(f"Username: {user_profile['username']}")
            print(f"Avatar URL: https://cdn.discordapp.com/avatars/{user_profile['id']}/{user_profile['avatar']}.png")

            if 'email' in user_profile:
                print(f"Email: {user_profile['email']}")

            if 'bio' in user_profile:
                print(f"Bio: {user_profile['bio']}")

            if 'locale' in user_profile:
                print(f"Locale: {user_profile['locale']}")

            if 'verified' in user_profile:
                print(f"Verified: {user_profile['verified']}")

            if 'premium_type' in user_profile:
                premium_type = user_profile['premium_type']
                if premium_type == 1:
                    print("Nitro Status: Nitro Classic")
                elif premium_type == 2:
                    print("Nitro Status: Nitro")
                else:
                    print("Nitro Status: None")

            if 'public_flags' in user_profile:
                public_flags = user_profile['public_flags']
                print(f"Public Flags: {public_flags}")

            if 'banner' in user_profile:
                banner_url = f"https://cdn.discordapp.com/banners/{user_profile['id']}/{user_profile['banner']}.png"
                print(f"Banner URL: {banner_url}")
        else:
            print("Failed to fetch user profile. Response:", user_profile)

        return user_profile

    def get_guilds(self):
        url = f"{self.base_url}/users/@me/guilds"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_channels(self, guild_id):
        url = f"{self.base_url}/guilds/{guild_id}/channels"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_messages(self, channel_id, limit=50):
        url = f"{self.base_url}/channels/{channel_id}/messages"
        headers = {'Authorization': self.user_token}
        params = {'limit': limit}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def send_message(self, channel_id, content):
        url = f"{self.base_url}/channels/{channel_id}/messages"
        headers = {'Authorization': self.user_token}
        data = {'content': content}
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    
    def create_channel(self, guild_id, name, channel_type=0):
        url = f"{self.base_url}/guilds/{guild_id}/channels"
        headers = {'Authorization': self.user_token}
        data = {
            'name': name,
            'type': channel_type 
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    
    def delete_channel(self, channel_id):
        url = f"{self.base_url}/channels/{channel_id}"
        headers = {'Authorization': self.user_token}
        response = requests.delete(url, headers=headers)
        return response.status_code == 204

    def kick_member(self, guild_id, member_id):
        url = f"{self.base_url}/guilds/{guild_id}/members/{member_id}"
        headers = {'Authorization': self.user_token}
        response = requests.delete(url, headers=headers)
        return response.status_code == 204

    def ban_member(self, guild_id, member_id, reason=None):
        url = f"{self.base_url}/guilds/{guild_id}/bans/{member_id}"
        headers = {'Authorization': self.user_token}
        data = {'reason': reason} if reason else {}
        response = requests.put(url, headers=headers, json=data)
        return response.status_code == 204

    def unban_member(self, guild_id, member_id):
        url = f"{self.base_url}/guilds/{guild_id}/bans/{member_id}"
        headers = {'Authorization': self.user_token}
        response = requests.delete(url, headers=headers)
        return response.status_code == 204

    def get_member(self, guild_id, member_id):
        url = f"{self.base_url}/guilds/{guild_id}/members/{member_id}"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)
        return response.json()

    def edit_message(self, channel_id, message_id, content):
        url = f"{self.base_url}/channels/{channel_id}/messages/{message_id}"
        headers = {'Authorization': self.user_token}
        data = {'content': content}
        response = requests.patch(url, headers=headers, json=data)
        return response.json()

    def delete_message(self, channel_id, message_id):
        url = f"{self.base_url}/channels/{channel_id}/messages/{message_id}"
        headers = {'Authorization': self.user_token}
        response = requests.delete(url, headers=headers)
        return response.status_code == 204  

    def get_friends(self, save_to_file=False):
        url = f"{self.base_url}/users/@me/relationships"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)
        
        friends = response.json()

        if isinstance(friends, list):
            if save_to_file:
                with open("friends.json", "w") as file:
                    json.dump(friends, file, indent=4)
                print("Friends list saved to friends.json.")
            else:
                print(f"You have {len(friends)} friends.")
                for friend in friends:
                    print(f"ID: {friend['id']}")
                    print(f"Username: {friend['user']['username']}")
                    print("-" * 20)
        else:
            print("Failed to fetch the list of friends. Response:", friends)

        return friends

    def get_activities(self):
        url = f"{self.base_url}/users/@me/activities"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)
        return response.json()
    
    def update_status(self, status="online", activity=None):
        url = f"{self.base_url}/users/@me/settings"
        headers = {'Authorization': self.user_token}
        data = {
            'status': status,
            'activity': activity or {}
        }
        response = requests.patch(url, headers=headers, json=data)
        return response.json()
    
    def update_nickname(self, guild_id, nickname):
        url = f"{self.base_url}/guilds/{guild_id}/members/@me"
        headers = {'Authorization': self.user_token}
        data = {'nick': nickname}
        response = requests.patch(url, headers=headers, json=data)
        return response.json()
    
    def get_voice_regions(self, guild_id):
        url = f"{self.base_url}/guilds/{guild_id}/regions"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)
        return response.json()
        
    def get_audit_logs(self, guild_id, limit=20):
        url = f"{self.base_url}/guilds/{guild_id}/audit-logs"
        headers = {'Authorization': self.user_token}
        params = {'limit': limit}

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch audit logs. Status code: {response.status_code}")
            return None
            
    def leave_guild(self, guild_id):
        guild_info = self.get_guilds()  
        guild_name = None

        for guild in guild_info:
            if guild['id'] == guild_id:
                guild_name = guild['name']
                break

        url = f"{self.base_url}/users/@me/guilds/{guild_id}"
        headers = {'Authorization': self.user_token}

        for attempt in range(3):  
            response = requests.delete(url, headers=headers)
            
            if response.status_code == 204:
                print(f"Successfully left the guild: {guild_name}")
                return True
            elif response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 1))  
                print(f"Rate limited. Retrying after {retry_after} seconds...")
                time.sleep(retry_after)  
            else:
                print("Failed to leave the guild. Status Code:", response.status_code)
                return False

        print("Exceeded maximum retry attempts.")
        return False

    def get_user_profile(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)
        user_profile = response.json()

        if 'id' in user_profile:
            print("User Profile:")
            print(f"User ID: {user_profile['id']}")
            print(f"Username: {user_profile['username']}")
            print(f"Avatar URL: https://cdn.discordapp.com/avatars/{user_profile['id']}/{user_profile['avatar']}.png")

            if 'bio' in user_profile:
                print(f"Bio: {user_profile['bio']}")

        else:
            print("Failed to fetch user profile. Response:", user_profile)

        return user_profile


    def send_embed(self, channel_id, title, description, color=0x00ff00):
        url = f"{self.base_url}/channels/{channel_id}/messages"
        headers = {'Authorization': self.user_token}
        embed = {
            'embeds': [{
                'title': title,
                'description': description,
                'color': color
            }]
        }
        response = requests.post(url, headers=headers, json=embed)
        return response.json()
    
    def spam_messages(self, channel_id, content, count, delay):
        for i in range(count):
            response = self.send_message(channel_id, content)
            if response.get('id'):
                print(f"Message {i + 1}/{count} sent.")
            else:
                print(f"Failed to send message {i + 1}/{count}. Response: {response}")
            time.sleep(delay)
            
    def add_role(self, guild_id, name, permissions_list=None, color=None, hoist=False, mentionable=False):
        url = f"{self.base_url}/guilds/{guild_id}/roles"
        headers = {
            'Authorization': self.user_token,
            'Content-Type': 'application/json'
        }

        permissions = 0

        if permissions_list:
            for perm in permissions_list:
                if perm in DISCORD_PERMISSION_VALUES:
                    permissions |= DISCORD_PERMISSION_VALUES[perm]
                else:
                    print(f"Permission '{perm}' not found.")

        data = {
            'name': name,
            'hoist': hoist,
            'mentionable': mentionable,
            'permissions': permissions
        }

        if color is not None:
            data['color'] = color

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 201:
            return response.json()
        else:
            print(f"Failed to create role. Status code: {response.status_code}")
            return None

    def add_reaction(self, channel_id, message_id, emoji):
        url = f"{self.base_url}/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
        headers = {'Authorization': self.user_token}
        response = requests.put(url, headers=headers)
        return response.status_code == 204
    
    def get_guild_insights(self, guild_id):
        url = f"{self.base_url}/guilds/{guild_id}/preview"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_guild_info(self, guild_id):
        url = f"{self.base_url}/guilds/{guild_id}"
        headers = {'Authorization': self.user_token}
        response = requests.get(url, headers=headers)

        guild_info = response.json()

        if 'id' in guild_info:
            print("Guild Info:")
            print(f"Guild ID: {guild_info['id']}")
            print(f"Guild Name: {guild_info['name']}")
            print(f"Guild Description: {guild_info.get('description', 'No description available')}")
            print(f"Guild Member Count: {guild_info.get('approximate_member_count', 'Not available')}")
            print(f"Guild Owner ID: {guild_info.get('owner_id', 'Not available')}")
            print(f"Guild Creation Date: {guild_info.get('created_at', 'Not available')}")
            print(f"Guild Icon: https://cdn.discordapp.com/icons/{guild_info['id']}/{guild_info.get('icon', 'No icon')}.png")
            
            channel_count = len(guild_info.get('channels', []))
            print(f"Number of Channels: {channel_count}")

            role_count = len(guild_info.get('roles', []))
            print(f"Number of Roles: {role_count}")

        else:
            print("Failed to fetch guild information. Response:", guild_info)

        return guild_info
        
    def fetch_friend_names(self, friend_ids):
        names = []
        url = f"{self.base_url}/users/@me/relationships"
        headers = {
            'Authorization': self.user_token,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            friends = response.json()
            for friend in friends:
                if str(friend['id']) in friend_ids:  
                    names.append(friend['user']['username']) 
        else:
            print(f"Failed to fetch friend names. Status code: {response.status_code}")
        return names
        
    def create_group(self, friend_ids):
        url = f"{self.base_url}/users/@me/channels"
        headers = {
            'Authorization': self.user_token,
            'Content-Type': 'application/json'
        }
        data = {
            "recipients": friend_ids  
        }
            
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            print("Group created successfully.")
            return response.json()
        elif response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 1))
            print(f"Rate limited. Retrying after {retry_after} seconds.")
            time.sleep(retry_after)
            return self.create_group(friend_ids)
        else:
            print(f"Failed to create group. Status code: {response.status_code}")
            return None
            
    def mass_create_groups(self, friend_ids_list):
        for friend_ids in friend_ids_list:
            friend_names = self.fetch_friend_names(friend_ids)
            if friend_names:
                print(f"Creating group with friends: {', '.join(friend_names)}")
            else:
                print("No friend names found.")
            self.create_group(friend_ids)
            time.sleep(1)
            
    def get_friend_count(self):
        url = f"{self.base_url}/users/@me/relationships"
        headers = {
            'Authorization': self.user_token,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            friends = response.json()
            return len([friend for friend in friends if friend['type'] == 1])
        else:
            print(f"Failed to fetch friend count. Status code: {response.status_code}")
            return None
