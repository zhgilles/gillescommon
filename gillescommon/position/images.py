#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time       : 2021/4/13 15:10
@Author     : gillesshi
@Email      : gillesshi@leyinetwork.com
@File       : images.py
@Software   : PyCharm
@Description: 
"""


from airtest.core.api import Template, using
import os
using(os.path.join(os.getcwd(), '..', '..', 'gillescommon', 'gillescommon', 'image'))


# wg
open_10_gifts = Template("open_10_gifts.png", record_pos=(0.306, -0.074), resolution=(1440, 810), rgb=True)
al_help = Template("al_help.png", record_pos=(0.328, 0.151), resolution=(1440, 810))
help_all = Template("help_all.png", record_pos=(0.28, 0.223), resolution=(1440, 811))
collect = Template("collect.png", record_pos=(0.303, -0.122), resolution=(1440, 810))
auto_complete = Template("auto_complete.png", record_pos=(-0.215, 0.011), resolution=(1440, 810))
collect_2 = Template("collect.png", record_pos=(-0.213, 0.008), resolution=(1440, 810))
start = Template("start.png", record_pos=(-0.212, 0.009), resolution=(1440, 811))
account = Template(r"account.png", record_pos=(-0.226, -0.126), resolution=(1440, 811))
switch_account = Template(r"switch_account.png", record_pos=(-0.001, 0.112), resolution=(1440, 811))
yes = Template(r"yes.png", record_pos=(-0.11, 0.107), resolution=(1440, 811))
login = Template(r"login.png", record_pos=(-0.002, 0.122), resolution=(1440, 811), rgb=True)
town_tag = Template("town_tag.png", record_pos=(-0.035, -0.122), resolution=(1440, 810))
cross = Template(r"cross.png", record_pos=(0.469, -0.257), resolution=(1440, 811))
cross_2 = Template(r"cross_2.png", record_pos=(0.392, -0.227), resolution=(1440, 811))
login_window = Template(r"login_window.png", record_pos=(0.204, -0.211), resolution=(1440, 811))
ok = Template(r"ok.png", record_pos=(-0.129, 0.157), resolution=(1440, 811), rgb=True, threshold=0.1)
ok_2 = Template(r"ok.png", record_pos=(0.001, 0.18), resolution=(1440, 811), rgb=True)
bull_gang_challenge = Template(r"bull_gang_challenge.png", record_pos=(-0.002, -0.113), resolution=(1440, 811), rgb=True)
event_calendar = Template(r"event_calendar.png", record_pos=(0.001, -0.227), resolution=(1440, 811))
exit_window_2 = Template(r"exit_window_2.png", record_pos=(0.462, -0.26), resolution=(1440, 811))
use = Template(r"use.png", record_pos=(0.332, -0.111), resolution=(1440, 811), rgb=True)
use_2 = Template(r"use_2.png", record_pos=(0.332, -0.111), resolution=(1440, 811), rgb=True, threshold=0.3)
select = Template(r"select.png", record_pos=(-0.212, -0.106), resolution=(1440, 811))
collect = Template(r"collect.png", record_pos=(-0.002, 0.208), resolution=(1440, 811))


# me
search_2_me = Template(r"search_2_me.png", record_pos=(0.317, 0.229), resolution=(1440, 811))
plus_me = Template(r"plus_me.png", record_pos=(0.056, 0.232), resolution=(1440, 811))
touch_me = Template(r"touch_me.png", record_pos=(-0.081, 0.03), resolution=(1440, 811), threshold=0.5)
touch_2_me = Template(r"touch_2_me.png", record_pos=(-0.138, 0.025), resolution=(1440, 811), threshold=0.5)
attack_me = Template(r"attack_me.png", record_pos=(0.176, 0.209), resolution=(1440, 811))
setup_me = Template(r"setup_me.png", record_pos=(0.306, -0.164), resolution=(1440, 811))
select_commander_me = Template(r"select_commander_me.png", record_pos=(0.295, -0.154), resolution=(1440, 811))
select_troops_me = Template(r"select_troops_me.png", record_pos=(0.025, 0.208), resolution=(1440, 811))
march_me = Template(r"march_me.png", record_pos=(0.231, 0.208), resolution=(1440, 811))
queue_add_me = Template(r"queue_add_me.png", record_pos=(0.445, -0.207), resolution=(1440, 811))
minus_me = Template(r"minus_me.png", record_pos=(-0.366, 0.233), resolution=(1440, 811))
ok_me = Template(r"ok_me.png", record_pos=(0.001, 0.086), resolution=(1440, 811))
cross_me = Template(r"cross_me.png", record_pos=(0.473, -0.262), resolution=(1440, 811))
map_switch_me = Template(r"map_switch_me.png", record_pos=(0.45, 0.239), resolution=(1440, 811))
explore_2_me = Template(r"explore_2_me.png", record_pos=(0.287, -0.062), resolution=(1440, 811))
explore_3_me = Template(r"explore_3_me.png", record_pos=(0.133, 0.124), resolution=(1440, 811))
dispatch_me = Template(r"dispatch_me.png", record_pos=(0.313, -0.169), resolution=(1440, 811))
dispatch_2_me = Template(r"dispatch_me.png", record_pos=(0.309, -0.101), resolution=(1440, 811))
dispatch_2_me = Template(r"dispatch_me.png", record_pos=(0.309, -0.101), resolution=(1440, 811))
dispatch_3_me = Template(r"dispatch_me.png", record_pos=(0.324, -0.019), resolution=(1440, 811))
cross_2_me = Template(r"cross_2_me.png", record_pos=(0.356, -0.227), resolution=(1440, 811))
gather_me = Template(r"gather_me.png", record_pos=(0.207, 0.109), resolution=(1440, 811))



