from enum import StrEnum

class Status(StrEnum):
    READ = "read"
    DELIVERED = "delivered"
    SENT = "sent"
    WAITING = "waiting"
    FAILED = "failed"