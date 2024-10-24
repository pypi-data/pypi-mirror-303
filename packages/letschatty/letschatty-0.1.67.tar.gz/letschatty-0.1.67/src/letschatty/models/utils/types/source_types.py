from enum import StrEnum

class SourceType(StrEnum):
    OTHER_SOURCE = "other_source"
    PURE_AD = "pure_ad"
    DEFAULT_SOURCE = "default_source"
    WHATSAPP_DEFAULT_SOURCE = "whatsapp_default_source"
    TOPIC_DEFAULT_SOURCE = "topic_default_source"
    UTM_SOURCE = "utm_source"