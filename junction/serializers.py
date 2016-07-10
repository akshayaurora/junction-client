# -*- coding: utf-8 -*-

from schematics.types.compound import ModelType, ListType
from schematics.types import IntType, StringType, BooleanType, DateTimeType
from schematics.models import Model

__all__ = ['FeedbackQuestionSerializer', 'ScheduleItemSerializer']


class IdSerializer(Model):
    id = IntType()


class TitleSerializer(Model):
    title = StringType()


class NameSerializer(Model):
    name = StringType()


class IdTitleSerializer(IdSerializer, TitleSerializer):
    pass


class IdNameSerializer(IdSerializer, NameSerializer):
    pass


class RoomSerializer(IdNameSerializer):
    venue = StringType()
    note = StringType()


class SessionSerializer(IdTitleSerializer):
    author = StringType()
    section = StringType()
    prerequisites = StringType()
    description = StringType()
    target_audience = IntType()
    speaker_info = StringType()
    speaker_links = StringType()
    content_urls = StringType()


class ScheduleItemSerializer(IdNameSerializer):
    room_id = IntType()
    type = StringType()
    event_date = DateTimeType('%Y-%m-%d')
    start_time = DateTimeType('%H:%M:%S')
    end_time = DateTimeType('%H:%M:%S')
    session = ModelType(SessionSerializer)


class BaseQuestionSerializer(IdSerializer, TitleSerializer):
    schedule_item_type = StringType()
    is_required = BooleanType()
    type = StringType()


class TextFeedbackQuestionSerializer(BaseQuestionSerializer):
    pass


class AllowedChoiceValidator(IdTitleSerializer):
    value = IntType()


class ChoiceFeedbackQuestionSerializer(BaseQuestionSerializer):
    allowed_choices = ListType(ModelType(AllowedChoiceValidator))


class FeedbackQuestionSerializer(Model):
    text = ListType(ModelType(TextFeedbackQuestionSerializer))
    choice = ListType(ModelType(ChoiceFeedbackQuestionSerializer))
