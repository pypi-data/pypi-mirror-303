class Update:
    def __init__(self, update_dict):
        self.update_id = update_dict["update_id"]
        self.message = Message(update_dict["message"]) if "message" in update_dict else None
        self.callback_query = CallbackQuery(update_dict["callback_query"]) if "callback_query" in update_dict else None

    def to_dict(self):
        return {
            "update_id": self.update_id,
            "message": self.message.to_dict() if self.message else None,
            "callback_query": self.callback_query.to_dict() if self.callback_query else None
        }

class CallbackQuery:
    def __init__(self, callback_query_dict):
        self.id = callback_query_dict["id"]
        self.from_user = User(callback_query_dict["from"])
        self.message = Message(callback_query_dict["message"]) if "message" in callback_query_dict else None
        self.inline_message_id = callback_query_dict.get("inline_message_id")
        self.chat_instance = callback_query_dict["chat_instance"]
        self.data = callback_query_dict.get("data")

    def to_dict(self):
        return {
            "id": self.id,
            "from_user": self.from_user.to_dict(),
            "message": self.message.to_dict() if self.message else None,
            "inline_message_id": self.inline_message_id,
            "chat_instance": self.chat_instance,
            "data": self.data
        }

class Message:
    def __init__(self, message_dict):
        self.message_id = message_dict["message_id"]
        self.from_user = User(message_dict["from"])
        self.date = message_dict["date"]
        self.chat = Chat(message_dict["chat"])
        self.text = message_dict.get("text")
        self.sticker = Sticker(message_dict["sticker"]) if "sticker" in message_dict else None
        self.photo = message_dict.get("photo")
        self.video = message_dict.get("video")
        self.document = message_dict.get("document")
        self.venue = Venue(message_dict["venue"]) if "venue" in message_dict else None
        self.location = Venue(message_dict["location"]) if "location" in message_dict else None


    def to_dict(self):
        return {
            "message_id": self.message_id,
            "from_user": self.from_user.to_dict(),
            "date": self.date,
            "chat": self.chat.to_dict(),
            "text": self.text,
            "sticker": self.sticker.to_dict() if self.sticker else None,
            "photo": self.photo,
            "video": self.video,
            "document": self.document,
            "venue": self.venue.to_dict() if self.venue else None,
            "location": self.location.to_dict() if self.location else None
        }

class User:
    def __init__(self, user_dict):
        self.id = user_dict["id"]
        self.is_bot = user_dict["is_bot"]
        self.first_name = user_dict["first_name"]
        self.username = user_dict.get("username")
        self.language_code = user_dict.get("language_code")

    def to_dict(self):
        return {
            "id": self.id,
            "is_bot": self.is_bot,
            "first_name": self.first_name,
            "username": self.username,
            "language_code": self.language_code
        }

class Venue:
    def __init__(self, venue_dict):
        self.location = venue_dict.get("location", {})
        self.latitude = self.location.get("latitude") or venue_dict.get("latitude")
        self.longitude = self.location.get("longitude") or venue_dict.get("longitude")
        self.address = venue_dict.get('address')
        self.title = venue_dict.get("title")
        self.foursquare_id = venue_dict.get("foursquare_id")
        self.foursquare_type = venue_dict.get("foursquare_type")

    def to_dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "address": self.address,
            "title": self.title,
            "foursquare_id": self.foursquare_id,
            "foursquare_type": self.foursquare_type
        }

class Chat:
    def __init__(self, chat_dict):
        self.id = chat_dict["id"]
        self.type = chat_dict["type"]
        self.first_name = chat_dict.get("first_name")
        self.username = chat_dict.get("username")

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "first_name": self.first_name,
            "username": self.username
        }

class Sticker:
    def __init__(self, sticker_dict):
        self.file_id = sticker_dict["file_id"]
        self.file_unique_id = sticker_dict["file_unique_id"]
        self.width = sticker_dict["width"]
        self.height = sticker_dict["height"]
        self.is_animated = sticker_dict["is_animated"]
        self.is_video = sticker_dict.get("is_video", False)
        self.thumb = sticker_dict.get("thumb")
        self.emoji = sticker_dict.get("emoji")
        self.set_name = sticker_dict.get("set_name")

    def to_dict(self):
        return {
            "file_id": self.file_id,
            "file_unique_id": self.file_unique_id,
            "width": self.width,
            "height": self.height,
            "is_animated": self.is_animated,
            "is_video": self.is_video,
            "thumb": self.thumb,
            "emoji": self.emoji,
            "set_name": self.set_name
        }
