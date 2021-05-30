# -*- encoding=utf8 -*-

from airtest.core.api import touch, exists, sleep, text, swipe, keyevent
from gillescommon.position.images import cross, ok


def my_touch(v, wait_time=0.5):
    touch(v)
    sleep(wait_time)


def my_exist(v):
    res = exists(v)
    return res


def my_text(*args, wait_time=0, **kwargs):
    text(*args, **kwargs)
    sleep(wait_time)


def my_swipe(*args, wait_time=0.5, **kwargs):
    swipe(*args, **kwargs)
    sleep(wait_time)


def my_keyevent(*args, **kwargs):
    keyevent(*args, **kwargs)


def my_exist_and_touch(v, wait_time=0.5):
    if my_exist(v):
        my_touch(v, wait_time)
        return True
    return False
