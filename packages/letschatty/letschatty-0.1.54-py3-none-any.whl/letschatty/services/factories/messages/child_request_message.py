
from typing import Type
from datetime import datetime
from zoneinfo import ZoneInfo
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
        content = ChattyContentText(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=TextMessage, sent_by=sent_by)

    @staticmethod
    def instance_image_message(message: MessageRequest, sent_by: str) -> ImageMessage:
        content = ChattyContentImage(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=ImageMessage, sent_by=sent_by)

    @staticmethod
    def instance_video_message(message: MessageRequest, sent_by: str) -> VideoMessage:
        content = ChattyContentVideo(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=VideoMessage, sent_by=sent_by)

    @staticmethod
    def instance_document_message(message: MessageRequest, sent_by: str) -> DocumentMessage:
        content = ChattyContentDocument(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=DocumentMessage, sent_by=sent_by)

    @staticmethod
    def instance_audio_message(message: MessageRequest, sent_by: str) -> AudioMessage:
        content = ChattyContentAudio(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=AudioMessage, sent_by=sent_by)

    @staticmethod
    def instance_sticker_message(message: MessageRequest, sent_by: str) -> StickerMessage:
        content = ChattyContentSticker(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=StickerMessage, sent_by=sent_by)

    @staticmethod
    def instance_contact_message(message: MessageRequest, sent_by: str) -> ContactMessage:
        content = ChattyContentContacts(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=ContactMessage, sent_by=sent_by)

    @staticmethod
    def instance_location_message(message: MessageRequest, sent_by: str) -> LocationMessage:
        content = ChattyContentLocation(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=LocationMessage, sent_by=sent_by)

    @staticmethod
    def instance_central_notification(message: MessageRequest, sent_by: str) -> CentralNotification:
        content = ChattyContentCentral(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=CentralNotification, sent_by=sent_by)

    @staticmethod
    def instance_reaction_message(message: MessageRequest, sent_by: str) -> ReactionMessage:
        content = ChattyContentReaction(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=ReactionMessage, sent_by=sent_by)
        
    @staticmethod
    def instantiate_message(message: MessageRequest, content: ChattyContent, message_type: Type[ChattyMessage], sent_by: str) -> ChattyMessage:
        return message_type(
            id=None,
            created_at=datetime.now(tz=ZoneInfo("UTC")),
            updated_at=datetime.now(tz=ZoneInfo("UTC")),
            content=content,
            status=Status.WAITING,
            is_incoming_message=False,
            context=ChattyContext(message.context),
            sent_by=sent_by,
            subtype=message.subtype
        )
