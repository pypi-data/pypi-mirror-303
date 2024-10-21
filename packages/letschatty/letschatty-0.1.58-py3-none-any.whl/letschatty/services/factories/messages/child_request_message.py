
from typing import Type
from datetime import datetime
from zoneinfo import ZoneInfo

from bson import ObjectId

from ....models.utils import MessageType, Status
from ....models.messages import ChattyMessage, TextMessage, ImageMessage, VideoMessage, DocumentMessage, StickerMessage, AudioMessage, ContactMessage, LocationMessage, CentralNotification, ReactionMessage
from ....models.messages.chatty_messages.schema import ChattyContentText, ChattyContentImage, ChattyContentVideo, ChattyContentDocument, ChattyContentSticker, ChattyContentAudio, ChattyContentContacts, ChattyContentLocation, ChattyContentCentral, ChattyContentReaction, ChattyContent, ChattyContext
from ....models.messages.chatty_messages.base.message_request import MessageRequest

class MessagefromMessageRequestFactory:
    """This factory takes a message request and instantiates the corresponding ChattyMessage"""
    @staticmethod
    def from_request(message: MessageRequest, sent_by: str) -> ChattyMessage | None:
        match message.type:
            case MessageType.TEXT.value:
                return MessagefromMessageRequestFactory.instance_text_message(message, sent_by)
            case MessageType.IMAGE.value:
                return MessagefromMessageRequestFactory.instance_image_message(message, sent_by)
            case MessageType.VIDEO.value:
                return MessagefromMessageRequestFactory.instance_video_message(message, sent_by)
            case MessageType.DOCUMENT.value:
                return MessagefromMessageRequestFactory.instance_document_message(message, sent_by)
            case MessageType.AUDIO.value:
                return MessagefromMessageRequestFactory.instance_audio_message(message, sent_by)
            case MessageType.STICKER.value:
                return MessagefromMessageRequestFactory.instance_sticker_message(message, sent_by)
            case MessageType.CONTACT.value:
                return MessagefromMessageRequestFactory.instance_contact_message(message, sent_by)
            case MessageType.LOCATION.value:
                return MessagefromMessageRequestFactory.instance_location_message(message, sent_by)
            case MessageType.CENTRAL.value:
                return MessagefromMessageRequestFactory.instance_central_notification(message, sent_by)
            case MessageType.REACTION.value:
                return MessagefromMessageRequestFactory.instance_reaction_message(message, sent_by)
            case _:
                raise ValueError(f"Invalid message type: {message.type} - valid types: {MessageType.values()}")

    @staticmethod
    def instance_text_message(message: MessageRequest, sent_by: str) -> TextMessage:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=TextMessage, sent_by=sent_by)

    @staticmethod
    def instance_image_message(message: MessageRequest, sent_by: str) -> ImageMessage:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=ImageMessage, sent_by=sent_by)

    @staticmethod
    def instance_video_message(message: MessageRequest, sent_by: str) -> VideoMessage:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=VideoMessage, sent_by=sent_by)

    @staticmethod
    def instance_document_message(message: MessageRequest, sent_by: str) -> DocumentMessage:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=DocumentMessage, sent_by=sent_by)

    @staticmethod
    def instance_audio_message(message: MessageRequest, sent_by: str) -> AudioMessage:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=AudioMessage, sent_by=sent_by)

    @staticmethod
    def instance_sticker_message(message: MessageRequest, sent_by: str) -> StickerMessage:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=StickerMessage, sent_by=sent_by)

    @staticmethod
    def instance_contact_message(message: MessageRequest, sent_by: str) -> ContactMessage:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=ContactMessage, sent_by=sent_by)

    @staticmethod
    def instance_location_message(message: MessageRequest, sent_by: str) -> LocationMessage:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=LocationMessage, sent_by=sent_by)

    @staticmethod
    def instance_central_notification(message: MessageRequest, sent_by: str) -> CentralNotification:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=CentralNotification, sent_by=sent_by)

    @staticmethod
    def instance_reaction_message(message: MessageRequest, sent_by: str) -> ReactionMessage:
        return MessagefromMessageRequestFactory.instantiate_message(message=message, message_type=ReactionMessage, sent_by=sent_by)
        
    @staticmethod
    def instantiate_message(message: MessageRequest, message_type: Type[ChattyMessage], sent_by: str) -> ChattyMessage:
        return message_type(
            id=str(ObjectId()),
            created_at=datetime.now(tz=ZoneInfo("UTC")),
            updated_at=datetime.now(tz=ZoneInfo("UTC")),
            content=message.content,
            status=Status.WAITING,
            is_incoming_message=False,
            context=message.context,
            sent_by=sent_by,
            subtype=message.subtype
        )
