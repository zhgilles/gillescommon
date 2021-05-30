X_SIZE = 1440  # G.DEVICE.display_info['width']
Y_SIZE = 810  # G.DEVICE.display_info['height']


def cal_pos_abs(x_rel, y_rel, x_size=X_SIZE, y_size=Y_SIZE):
    x_abs = x_rel * x_size + 0.5 * x_size
    y_abs = y_rel * x_size + 0.5 * y_size
    return x_abs, y_abs


# wg
quest = cal_pos_abs(0.114, 0.231)
town_quest = cal_pos_abs(-0.398, -0.167)
daily_quest = cal_pos_abs(-0.399, -0.097)
alliance_quest = cal_pos_abs(-0.399, -0.028)
vip_quest = cal_pos_abs(-0.398, 0.041)
alliance = (1050, 750)
gift = (1070, 720)
ok = cal_pos_abs(-0.001, 0.191)
clear_expired_gift = cal_pos_abs(0.031, 0.222)
exit_window = cal_pos_abs(0.458, -0.26)
magnifier = cal_pos_abs(0.358, -0.259)
x_pos = cal_pos_abs(-0.008, -0.013)
y_pos = cal_pos_abs(0.14, -0.01)
confirm = cal_pos_abs(0.435, 0.241)
transport = cal_pos_abs(0.101, 0.015)
basic_rss = cal_pos_abs(-0.417, -0.172)
growth_rss = cal_pos_abs(-0.417, -0.1)
grain = cal_pos_abs(-0.25, -0.061)
logs = cal_pos_abs(-0.25, 0.012)
rubble = cal_pos_abs(-0.25, 0.09)
iron = cal_pos_abs(-0.25, 0.166)
silver = cal_pos_abs(-0.25, 0.233)
transport_2 = cal_pos_abs(0.294, 0.212)
go = cal_pos_abs(0.001, 0.099)
more = cal_pos_abs(-0.062, 0.229)
leyi_account_email = cal_pos_abs(0.003, -0.03)
password = cal_pos_abs(0.002, 0.039)
mail = cal_pos_abs(0.29, 0.233)
mail_2 = cal_pos_abs(-0.314, -0.155)
instant_check = cal_pos_abs(-0.193, 0.217)
o3 = cal_pos_abs(-0.002, 0.206)
o4 = cal_pos_abs(-0.002, 0.102)
o5 = cal_pos_abs(-0.456, -0.26)
event_mail = cal_pos_abs(-0.312, -0.04)
o6 = cal_pos_abs(-0.002, 0.207)
center = (720,405)
world_map = cal_pos_abs(-0.485, 0.185)
cross_3 = cal_pos_abs(0.244, -0.205)
items = cal_pos_abs(0.026, 0.227)
my_items = cal_pos_abs(0.138, -0.207)
chest = cal_pos_abs(-0.4, 0.07)
swipe_point = cal_pos_abs(-0.162, -0.006)

# me
search_me = cal_pos_abs(-0.453, 0.238)
whisperers_me = cal_pos_abs(-0.377, 0.123)
level_swipe_start_me = cal_pos_abs(-0.332, 0.232)
plan_1_me = cal_pos_abs(0.374, -0.021)
plan_2_me = cal_pos_abs(0.373, 0.023)
plan_3_me = cal_pos_abs(0.374, 0.067)
center_me = cal_pos_abs(0, 0)
whisperers_max_level_me = cal_pos_abs(0.021, 0.234)