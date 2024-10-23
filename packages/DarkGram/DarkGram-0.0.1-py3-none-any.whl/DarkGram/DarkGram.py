import io
import json
import os
from pprint import pprint
import time
import requests

from .D_items import Update
import logging

logging.basicConfig(level=logging.INFO)

class DarkGram:
    """
    The main class for working with the telegram api
    """
    def __init__(self, token):
        self.token = token
        self.url = f"https://api.telegram.org/bot{self.token}/"
        self.file_url = f"https://api.telegram.org/file/bot{self.token}/"
        self.save_folder = "darksave"

    def send_message(self, chat_id, text):
        """
        Function for sending messages

        chat_id: The id of the chat
        text: The text of the message
        """
        url = f"{self.url}sendMessage"
        data = {"chat_id": chat_id, "text": text}
        response = requests.post(url, json=data)
        return response.json()

    def send_keyboard_message(self, chat_id, text, keyboard):
        """
        Function for sending messages with keyboard
        chat_id: The id of the chat
        text: The text of the message
        keyboard: The keyboard of the message as a JSON string
        """
        url = f"{self.url}sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text,
            "reply_markup": keyboard
        }
        response = requests.post(url, json=data)
        return response.json()

    def send_sticker(self, chat_id, sticker):
        """
        Function for sending stickers
        chat_id: The id of the chat
        sticker: The id of the sticker
        """
        url = f"{self.url}sendSticker"
        data = {"chat_id": chat_id, "sticker": sticker}
        response = requests.post(url, json=data)
        return response.json()

    def get_updates(self, offset=None):
        """
        Function for getting updates
        offset: The offset of the updates
        """
        params = {
            "offset": offset,
            "limit": 100,
            "timeout": 0
        }
        response = requests.get(f"{self.url}getUpdates", params=params)
        data = response.json()
        # pprint(data)
        return [Update(update) for update in data["result"]], data

    def get_file(self, file_id):
        """
        Function for getting file by id
        file_id: The id of the file
        """
        url = f"{self.url}getFile"
        data = {"file_id": file_id}
        response = requests.get(url, params=data)
        return response.json()["result"]["file_path"]

    def send_document(self, chat_id, document):
        """
        Function for sending documents
        chat_id: The id of the chat
        document: The document file object
        """
        url = f"{self.url}sendDocument"
        files = {"document": document}
        data = {"chat_id": chat_id}
        response = requests.post(url, data=data, files=files)
        return response.json()

    def download_file(self, file_path, local_filename):
        """
        Function for downloading files
        file_path: The path of the file
        local_filename: The local filename to save the file
        """
        url = f"{self.file_url}{file_path}"
        response = requests.get(url)
        os.makedirs(os.path.dirname(local_filename), exist_ok=True)

        with open(local_filename, 'wb') as f:
            f.write(response.content)

    def set_save_folder(self, folder):
        """
        Function for setting save folder
        folder: The folder to save files
        """
        self.save_folder = folder
        os.makedirs(self.save_folder, exist_ok=True)

    def send_inline_keyboard_message(self, chat_id, text, inline_keyboard):
        """
        Function for sending messages with inline keyboard
        chat_id: The id of the chat
        text: The text of the message
        inline_keyboard: The inline keyboard of the message
        """
        url = f"{self.url}sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text,
            "reply_markup": json.dumps({"inline_keyboard": inline_keyboard})
        }
        response = requests.post(url, json=data)
        return response.json()

    def answer_callback_query(self, callback_query_id, text=None, show_alert=False):
        """
        Function for answering callback queries
        callback_query_id: The id of the callback query
        text: The text of the answer
        show_alert: Whether to show an alert or not (default is False)
        """
        url = f"{self.url}answerCallbackQuery"
        data = {
            "callback_query_id": callback_query_id,
            "text": text,
            "show_alert": show_alert
        }
        response = requests.post(url, json=data)
        return response.json()

    def send_media_group(self, chat_id, media):
        """
        Function for sending media group
        chat_id: The id of the chat
        media: The media of the group
        """
        url = f"{self.url}sendMediaGroup"
        files = {}
        media_json = []

        for i, item in enumerate(media):
            if isinstance(item['media'], (str, bytes)) and os.path.isfile(item['media']):
                files[f'file{i}'] = open(item['media'], 'rb')
                media_json.append({
                    'type': item['type'],
                    'media': f'attach://file{i}'
                })
            elif isinstance(item['media'], io.BufferedReader):
                files[f'file{i}'] = item['media']
                media_json.append({
                    'type': item['type'],
                    'media': f'attach://file{i}'
                })
            else:
                media_json.append(item)

        data = {
            "chat_id": chat_id,
            "media": json.dumps(media_json)
        }

        response = requests.post(url, data=data, files=files)

        # Close opened files
        for file in files.values():
            if not isinstance(file, io.BufferedReader):
                file.close()

        return response.json()

    def send_photo(self, chat_id, photo, caption=None):
        """
        Function for sending photos
        chat_id: The id of the chat
        photo: The photo file path or file object
        caption: The caption of the photo
        """
        url = f"{self.url}sendPhoto"
        try:
            if os.path.isfile(photo):
                with open(photo, "rb") as photo_file:
                    files = {"photo": photo_file}
                    data = {"chat_id": chat_id, "caption": caption}
                    response = requests.post(url, data=data, files=files)
            else:
                data = {"chat_id": chat_id, "photo": photo, "caption": caption}
                response = requests.post(url, data=data)

            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Error sending photo: {e}")
            return None

    def send_video(self, chat_id, video, caption=None):
        """
        Function for sending videos
        chat_id: The id of the chat
        video: The video file path or file object
        caption: The caption of the video
        """
        url = f"https://api.telegram.org/bot{self.token}/sendVideo"
        try:
            if os.path.isfile(video):
                with open(video, 'rb') as video_file:
                    files = {'video': video_file}
                    data = {'chat_id': chat_id, 'caption': caption}
                    response = requests.post(url, data=data, files=files)

                return response.json()
            return f'Not Found video: {video}'
        except Exception as e:
            logging.error(f"Error sending video: {e}")
            return None

    def send_audio(self, chat_id, audio, caption=None):
        """
        Function for sending audios
        chat_id: The id of the chat
        audio: The audio file path or file object
        caption: The caption of the audio
        """
        url = f"{self.url}sendAudio"
        try:
            if os.path.isfile(audio):
                with open(audio, "rb") as audio_file:
                    files = {"audio": audio_file}
                    data = {"chat_id": chat_id, "caption": caption}
                    response = requests.post(url, data=data, files=files)
            else:
                data = {"chat_id": chat_id, "audio": audio, "caption": caption}
                response = requests.post(url, data=data)

            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Error sending audio: {e}")
            return None

    def create_reply_keyboard(self, buttons):
        """
        Create a reply keyboard with the given buttons
        buttons: List of lists, where each inner list represents a row of buttons
        """
        keyboard = {"keyboard": buttons, "resize_keyboard": True}
        return json.dumps(keyboard)

    def delete_message(self, chat_id, message_id):
        """
        Function for deleting a message
        chat_id: The id of the chat
        message_id: The id of the message to delete
        """
        url = f"{self.url}deleteMessage"
        data = {
            "chat_id": chat_id,
            "message_id": message_id
        }
        response = requests.post(url, json=data)
        return response.json()
