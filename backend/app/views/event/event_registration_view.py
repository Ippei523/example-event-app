from app.models import Event
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)


class EventRegistrationView(APIView):
    def post(self, request, response, **kwargs):
        try:
            title = request.data.get("title")
            description = request.data.get("description")
            location = request.data.get("location")
            start_time = request.data.get("start_time")
            end_time = request.data.get("end_time")
            tag_id = request.data.get("tag_id")
            user_id = request.data.get("user_id")
            event = Event.objects.create(
                title=title,
                description=description,
                location=location,
                start_time=start_time,
                end_time=end_time,
                tag_id=tag_id,
                user_id=user_id,
            )
            event.save()
            return Response(
                {"message": "イベントを作成しました"},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            logger.exception(e)
            return Response(
                {"message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
