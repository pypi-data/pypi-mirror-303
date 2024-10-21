
from typing import Type
from ...models.utils import MessageType, Status
from ...models.messages import ChattyMessage, TextMessage, ImageMessage, VideoMessage, DocumentMessage, StickerMessage, AudioMessage, ContactMessage, LocationMessage, CentralNotification, ReactionMessage
from ...models.messages.chatty_messages.schema import ChattyContentText, ChattyContentImage, ChattyContentVideo, ChattyContentDocument, ChattyContentSticker, ChattyContentAudio, ChattyContentContacts, ChattyContentLocation, ChattyContentCentral, ChattyContentReaction, ChattyContent, ChattyContext
from ...models.messages.messages_request.message_request import MessageRequest

class MessagefromMessageRequestFactory:
    """This factory takes a message request and instantiates the corresponding ChattyMessage"""
    @staticmethod
    def from_frontend(message: MessageRequest, sent_by: str) -> ChattyMessage | None:
        message.sent_by = sent_by
        match message.type:
            case MessageType.TEXT.value:
                return MessagefromMessageRequestFactory.instance_text_message(message)
            case MessageType.IMAGE.value:
                return MessagefromMessageRequestFactory.instance_image_message(message)
            case MessageType.VIDEO.value:
                return MessagefromMessageRequestFactory.instance_video_message(message)
            case MessageType.DOCUMENT.value:
                return MessagefromMessageRequestFactory.instance_document_message(message)
            case MessageType.AUDIO.value:
                return MessagefromMessageRequestFactory.instance_audio_message(message)
            case MessageType.STICKER.value:
                return MessagefromMessageRequestFactory.instance_sticker_message(message)
            case MessageType.CONTACT.value:
                return MessagefromMessageRequestFactory.instance_contact_message(message)
            case MessageType.LOCATION.value:
                return MessagefromMessageRequestFactory.instance_location_message(message)
            case MessageType.CENTRAL.value:
                return MessagefromMessageRequestFactory.instance_central_notification(message)
            case MessageType.REACTION.value:
                return MessagefromMessageRequestFactory.instance_reaction_message(message)
            case _:
                return None

    @staticmethod
    def instance_text_message(message: MessageRequest) -> TextMessage:
        content = ChattyContentText(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=TextMessage)

    @staticmethod
    def instance_image_message(message: MessageRequest) -> ImageMessage:
        content = ChattyContentImage(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=ImageMessage)

    @staticmethod
    def instance_video_message(message: MessageRequest) -> VideoMessage:
        content = ChattyContentVideo(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=VideoMessage)

    @staticmethod
    def instance_document_message(message: MessageRequest) -> DocumentMessage:
        content = ChattyContentDocument(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=DocumentMessage)

    @staticmethod
    def instance_audio_message(message: MessageRequest) -> AudioMessage:
        content = ChattyContentAudio(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=AudioMessage)

    @staticmethod
    def instance_sticker_message(message: MessageRequest) -> StickerMessage:
        content = ChattyContentSticker(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=StickerMessage)

    @staticmethod
    def instance_contact_message(message: MessageRequest) -> ContactMessage:
        content = ChattyContentContacts(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=ContactMessage)

    @staticmethod
    def instance_location_message(message: MessageRequest) -> LocationMessage:
        content = ChattyContentLocation(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=LocationMessage)

    @staticmethod
    def instance_central_notification(message: MessageRequest) -> CentralNotification:
        content = ChattyContentCentral(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=CentralNotification)

    @staticmethod
    def instance_reaction_message(message: MessageRequest) -> ReactionMessage:
        content = ChattyContentReaction(**message.content)
        return MessagefromMessageRequestFactory.instantiate_message(message=message, content=content, message_type=ReactionMessage)
        
    @staticmethod
    def instantiate_message(message: MessageRequest, content: ChattyContent, message_type: Type[ChattyMessage]) -> ChattyMessage:
        return message_type(
            id=None,
            created_at=message.date,
            content=content,
            status=Status.WAITING,
            is_incoming_message=False,
            context=ChattyContext(message.context),
            sent_by=message.sent_by
        )
