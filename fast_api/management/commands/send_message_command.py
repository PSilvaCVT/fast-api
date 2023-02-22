import json

from django.core.management.base import BaseCommand
from django_redis import get_redis_connection


class Command(BaseCommand):
    help = "Send message to websocket through Redis"

    def handle(self, *args, **options):
        redis_conn = get_redis_connection("default")
        redis_conn.publish(
            "message_event",
            json.dumps(
                dict(
                    chat_id="123",
                    data="Test send message to websocket through API.",
                )
            ),

        )
