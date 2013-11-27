#! -*- coding:utf-8 -*-
from django.dispatch import Signal
from django.db.models.signals import post_save
from django.core.signals import request_finished
from groups.models import Group, Topic, Reply, Applicant
from sys_notification.models import Notification

# 群组操作的signal
group_notify = Signal(providing_args=["instance", "args", "kwargs"])

# 话题操作的signal
topic_notify = Signal(providing_args=["instance", "args", "kwargs"])

# 好友操作的signal
friend_notify = Signal(providing_args=["instance", "args", "kwargs"])

# 将通知置为已点击
set_notity_clicked = Signal(providing_args=["request", "no_type", "args", "kwargs"])


def group_action(sender, instance, *args, **kwargs):
    obj = instance
    if obj.status != 'processing':
        notify = Notification(no_type='group', group_action=obj.status, to_user=obj.applicant, group=obj.group,
                              applicant=obj)
        notify.save()

group_notify.connect(group_action, dispatch_uid='create_group_notify')


def topic_action(sender, instance, *args, **kwargs):
    obj = instance
    if obj.reply:   # 是否是对回复的回复
        notify = Notification(no_type='topic', topic_action='re_reply', to_user=obj.reply.creator, reply=obj.reply,
                              topic=obj.topic, )
        notify.save()
    else:
        notify = Notification(no_type='topic', topic_action='re_topic', to_user=obj.topic.creator, topic=obj.topic)
        notify.save()

topic_notify.connect(topic_action, dispatch_uid='create_topic_notify')


def friend_action(sender, instance, *args, **kwargs):
    obj = instance
    # 关注操作
    notify = Notification(no_type='friend', friend_action='follow', to_user=obj.to_user, follower=obj.from_user)
    notify.save()
friend_notify.connect(friend_action, dispatch_uid='follow_notify')


def set_notification_clicked(sender, request, no_type, **kwargs):
    """
    点击相应页面后将通知置为已经点击clicked
    @fanlintao
    """
    notify_qs = Notification.objects.filter(to_user=request.user, no_type=no_type, click='unclick')
    notify_qs.update(click='clicked')

set_notity_clicked.connect(set_notification_clicked, dispatch_uid='set_notification_clicked')



