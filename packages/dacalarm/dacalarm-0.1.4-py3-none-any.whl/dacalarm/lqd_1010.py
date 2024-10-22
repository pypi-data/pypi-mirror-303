# 2024.10.18 修改参数

import datetime
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from typing import List, Optional

from dacalarm.utils.control_delta import centered_ewm
from dacalarm.utils.dac_facade import get_data, default_cache, mysql_conn
from dacalarm.utils.ycl_abandon_abnormal import get_time, get_time_str, abandon_abnormal_ycl

KEY_C1 = "C1_CONTROL"
KEY_C2 = "C2_CONTROL"
KEY_C3 = "C3_CONTROL"
KEY_C4 = "C4_CONTROL"
KEY_C5 = "C5_CONTROL"
KEY_C6 = "C6_CONTROL"
KEY_C7 = "C7_CONTROL"
KEY_C8 = "C8_CONTROL"
KEY_C9 = "C9_CONTROL"
KEYS = [KEY_C1, KEY_C2, KEY_C3, KEY_C4, KEY_C5, KEY_C6, KEY_C7, KEY_C8, KEY_C9]
ALARM_RULE_ID = 2039
TTL = 6 * 3600

# 不能小于0.5
ACTION_SLOPE_THRESHOLD1 = 0.06
ACTION_SLOPE_THRESHOLD2 = 0.12
ACTION_SLOPE_THRESHOLD3 = 0.16
YCL_INIT_ACTION_DELTA_THRESHOLD = 0.6
ACTION_YCL_CHANGE_THRESHOLD = 0.5
BW1R_ACTION_NUMBER = 3.5
BW2R_ACTION_NUMBER = 1.5

ACTION_CORRECTION_SLOPE_THRESHOLD = 0.1
PV_SP_DELTA_THRESHOLD = 0.1

ACTION_CORRECTION_YCL_DELTA = 0.7
YCL_HIGH_THRESHOLD = 1043.5
YCL_LOW_THRESHOLD = 1037
YCL_LOCATION_ACTION_INTERVAL = 25
YCL_LOCATION_ACTION_TURN = 1

BD4R_ACTION_DELTA = 0.6
BD4R_DELTA_ACTION_TURN = 1
BD4R_DELTA_ACTION_INTERVAL = 25

ACTION_POINT_MOVE_DELTA_THRESHOLD = 0.15
TEMPERATURE_ACTION_DELTA_THRESHOLD = 0.02
TEN_MIN_DELTA_ABNORMAL_THRESHOLD = 3.5

BW1R_CENTER_LINE = 1249.6
BW1R_EXTRA_ACTION_TURN = 0


def get_config(alarm_rule_id):
    global ACTION_SLOPE_THRESHOLD1, ACTION_SLOPE_THRESHOLD2, ACTION_SLOPE_THRESHOLD3
    global ACTION_YCL_CHANGE_THRESHOLD, YCL_INIT_ACTION_DELTA_THRESHOLD, BW1R_ACTION_NUMBER, BW2R_ACTION_NUMBER
    global ACTION_CORRECTION_SLOPE_THRESHOLD, PV_SP_DELTA_THRESHOLD, ACTION_CORRECTION_YCL_DELTA
    global YCL_HIGH_THRESHOLD, YCL_LOW_THRESHOLD, YCL_LOCATION_ACTION_INTERVAL, YCL_LOCATION_ACTION_TURN
    global BW1R_CENTER_LINE, BW1R_EXTRA_ACTION_TURN
    global BD4R_ACTION_DELTA, BD4R_DELTA_ACTION_TURN, BD4R_DELTA_ACTION_INTERVAL

    config_result = mysql_conn.query_config_by_alarm_rule_id(alarm_rule_id)
    config = config_result.get('冷却段', {})

    ACTION_SLOPE_THRESHOLD1 = config.get('MB1_YCL变化斜率阈值1', ACTION_SLOPE_THRESHOLD1)
    ACTION_SLOPE_THRESHOLD2 = config.get('MB1_YCL变化斜率阈值2', ACTION_SLOPE_THRESHOLD2)
    ACTION_SLOPE_THRESHOLD3 = config.get('MB1_YCL变化斜率阈值3', ACTION_SLOPE_THRESHOLD3)
    YCL_INIT_ACTION_DELTA_THRESHOLD = config.get('MB1_YCL拐头后初次调控变化量', YCL_INIT_ACTION_DELTA_THRESHOLD)
    ACTION_YCL_CHANGE_THRESHOLD = config.get('MB1_YCL每变化多少调一组', ACTION_YCL_CHANGE_THRESHOLD)
    BW1R_ACTION_NUMBER = config.get('MB1_BW1R每变化0.05度调的组数', BW1R_ACTION_NUMBER)
    BW2R_ACTION_NUMBER = config.get('MB1_BW2R每变化0.05度调的组数', BW2R_ACTION_NUMBER)
    ACTION_CORRECTION_SLOPE_THRESHOLD = config.get('MB1_YCL变化斜率不大阈值', ACTION_CORRECTION_SLOPE_THRESHOLD)
    PV_SP_DELTA_THRESHOLD = config.get('MB1_YCL变化斜率不大时，PV、SP差值大于阈值不调', PV_SP_DELTA_THRESHOLD)
    ACTION_CORRECTION_YCL_DELTA = config.get('MB1_YCL10min变缓变化阈值', ACTION_CORRECTION_YCL_DELTA)
    YCL_HIGH_THRESHOLD = config.get('MB2_YCL高位阈值', YCL_HIGH_THRESHOLD)
    YCL_LOW_THRESHOLD = config.get('MB2_YCL低位阈值', YCL_LOW_THRESHOLD)
    YCL_LOCATION_ACTION_INTERVAL = config.get('MB2_YCL位置调控间隔单位min', YCL_LOCATION_ACTION_INTERVAL)
    YCL_LOCATION_ACTION_TURN = config.get('MB2_YCL位置每次调控组数', YCL_LOCATION_ACTION_TURN)
    BW1R_CENTER_LINE = config.get('BW1R中心线', BW1R_CENTER_LINE)
    BW1R_EXTRA_ACTION_TURN = config.get('BW1R远离中心线额外力度组数', BW1R_EXTRA_ACTION_TURN)

    BD4R_ACTION_DELTA = config.get('MB4_BD4R长时间单趋势变化量', BD4R_ACTION_DELTA)
    BD4R_DELTA_ACTION_TURN = config.get('MB4_BD4R长时间单趋势调整组数', BD4R_DELTA_ACTION_TURN)
    BD4R_DELTA_ACTION_INTERVAL = config.get('MB4_BD4R长时间单趋势调整间隔', BD4R_DELTA_ACTION_INTERVAL)

    return config


def centered_guaidian(data: List[dict], time_diff: Optional[float] = 15):
    df = pd.DataFrame(data)
    if df.empty:
        return None, None
    peaks, _ = find_peaks(df['value'], width=10)
    troughs, _ = find_peaks(-df['value'], width=10)
    turning_points = np.sort(np.concatenate((peaks, troughs)))

    filtered_turning_points = []
    last_turning_point = None

    for point in turning_points:
        if last_turning_point is None or (
                get_time(df['time'][point]) - get_time(
            df['time'][last_turning_point])).total_seconds() / 60 > time_diff:
            filtered_turning_points.append(point)
            last_turning_point = point

    slopes = []
    for point in filtered_turning_points:
        if 2 <= point <= len(df) - 2:  # ensure enough data points on both sides
            slopes.append((df['time'][point], df['value'][point]))

    if slopes:
        return slopes[-1]
    return None, None


def ycl_pre(data):
    # 去重
    unique_data = []
    for row in data:
        time = row["time"]
        value = float(row["value"])
        if not unique_data or abs(value - float(unique_data[-1]["value"])) > 0.00001:
            unique_data.append({"time": get_time_str(get_time(time)), "value": value})
    return unique_data


def find_last_peak(data, window=None, min_distance=None, min_height=None, prominence=None):
    # 使用find_peaks函数查找峰值
    peaks, _ = find_peaks(data,
                          distance=min_distance,
                          height=min_height,
                          prominence=prominence,
                          width=window)
    if len(peaks) > 0:
        return peaks[-1]
    else:
        return None


def find_ycl_turning_point(ycl_filtered_values):
    window = 8
    min_distance = 40
    try:
        peak_ = find_last_peak(ycl_filtered_values, window=window, min_distance=min_distance)
        valley_ = find_last_peak(-ycl_filtered_values, window=window, min_distance=min_distance)
    except Exception as e:
        print(e)
        return None
    if peak_ and valley_:
        return max(peak_, valley_)
    elif peak_:
        return peak_
    elif valley_:
        return valley_
    else:
        return None


def do(ycl_data, global_result):
    config = get_config(ALARM_RULE_ID)
    global_result['CONTROL'] = 0
    alpha = 0.142857
    # TODO 去毛刺函数优化修改
    ycl_data = abandon_abnormal_ycl(ycl_pre(ycl_data))
    ycl_data = centered_ewm(data=ycl_data, alpha=alpha)
    ycl_df = pd.DataFrame(data=ycl_data)
    ycl_values = ycl_df.iloc[:, 1]
    ycl_turning_index = find_ycl_turning_point(ycl_values)
    if not ycl_turning_index:
        ycl_turning_index = -21
    # guaidian_time, guaidian_value = centered_guaidian(ycl_data, time_diff=10)
    guaidian_time, guaidian_value = ycl_data[ycl_turning_index]['time'], ycl_data[ycl_turning_index]['value']
    guaidian_value = float(guaidian_value)

    current_time = get_time(ycl_data[-1]['time'])
    current_value = float(ycl_data[-1]['value'])

    bw2r_data = get_data("9", "BW2R.UNIQUE", get_time_str(get_time(guaidian_time) - datetime.timedelta(minutes=60)),
                         get_time_str(current_time))
    bw2r_df = pd.DataFrame(data=bw2r_data)
    bw2r_values = bw2r_df["value"].ewm(span=21, adjust=False).mean().iloc[::-1].ewm(span=21, adjust=False).mean().iloc[
                  ::-1].rolling(window=11).mean()
    # 不再函数找拐点，函数找拐点容易误判，直接认为YCL拐点30min前为BW2R拐点
    guaidian_bw2r = round(bw2r_values[len(bw2r_values) - 61], 2)
    current_bw2r = round(bw2r_values[len(bw2r_values) - 1], 2)

    bw1r_data = get_data("9", "BW1R.UNIQUE", get_time_str(get_time(guaidian_time) - datetime.timedelta(minutes=90)),
                         get_time_str(current_time))
    bw1r_df = pd.DataFrame(data=bw1r_data)
    bw1r_values = bw1r_df["value"].ewm(span=21, adjust=False).mean().iloc[::-1].ewm(span=21, adjust=False).mean().iloc[
                  ::-1].rolling(window=11).mean()
    current_bw1r = round(bw1r_values[len(bw1r_values) - 1], 2)
    pre_guaidian20min_bw1r = round(
        bw1r_values[len(bw1r_values) - 41 - int((current_time - get_time(guaidian_time)).seconds / 30)], 2)

    # BW1R拐点直接为YCL开始拐头处的点，因为BW1R相当于YCL存在滞后性
    guaidian_bw1r = current_bw1r
    bw1r20min_delta = round(current_bw1r - bw1r_values[len(bw1r_values) - 41], 2)

    last_guaidian_time = default_cache.get('LQD_TURN_GUAI_DIAN_TIME')
    last_action_direction = default_cache.get(f'LQD_TURN_ACTION_DIRECTION', 0)
    turn_init = default_cache.get(f'LQD_TURN_INIT', 1)

    # 查看是否刷新拐点
    turn_init = turn_action(last_guaidian_time, guaidian_time, guaidian_value, current_value,
                            last_action_direction, global_result, turn_init, current_time, guaidian_bw1r,
                            guaidian_bw2r, pre_guaidian20min_bw1r)

    this_guaidian_time = default_cache.get('LQD_TURN_GUAI_DIAN_TIME')
    if not this_guaidian_time:
        this_guaidian_time = get_time_str(current_time)
    this_guaidian_value = default_cache.get('LQD_TURN_GUAI_DIAN_VALUE')
    if not this_guaidian_value:
        this_guaidian_value = current_value

    global_result['上次调控的拐点时间'] = last_guaidian_time
    global_result['识别的新拐点时间'] = guaidian_time
    global_result['识别的新拐点值'] = guaidian_value
    global_result['本次调控的拐点时间'] = this_guaidian_time
    global_result['本次调控的拐点值'] = this_guaidian_value

    last_action_value = default_cache.get(f'LQD_TURN_YCL_ACTION_VALUE', guaidian_value)
    last_action_time = get_time(default_cache.get(f'LQD_TURN_YCL_ACTION_TIME', guaidian_time))

    slope, delta_value, minutes = calc_ycl_change_slope(current_time, current_value, last_action_time,
                                                        last_action_value)
    global_result['上次锚点时间'] = get_time_str(last_action_time)
    global_result['上次锚点值'] = last_action_value
    global_result['斜率'] = slope
    global_result['差值'] = delta_value
    global_result['分钟数'] = minutes
    global_result['当前YCL值'] = current_value
    global_result['当前YCL值时间'] = get_time_str(current_time)

    point_delta = choose_action_point_follow_pv(current_time)
    this_action_direction = default_cache.get(f'LQD_TURN_ACTION_DIRECTION', 0)

    ycl10min_delta = current_value - ycl_data[-21]['value']
    ycl20min_delta = current_value - ycl_data[-41]['value']

    bw1r10min_delta = current_bw1r - bw1r_values[len(bw2r_values) - 21]
    bw1r20min_delta = current_bw1r - bw1r_values[len(bw2r_values) - 41]
    bw2r10min_delta = current_bw2r - bw2r_values[len(bw2r_values) - 21]
    bw2r20min_delta = current_bw2r - bw2r_values[len(bw2r_values) - 41]
    turns, this_action_ycl, this_action_time = calc_action_amount(slope, delta_value, current_value, current_time,
                                                                  turn_init, last_action_time, last_action_value,
                                                                  global_result, this_guaidian_value, current_value,
                                                                  point_delta, this_action_direction, ycl10min_delta,
                                                                  ycl20min_delta, current_bw2r, current_bw1r,
                                                                  bw1r10min_delta, bw2r10min_delta)

    global_result['本次计算后的锚点时间'] = get_time_str(this_action_time)
    global_result['本次计算后的锚点值'] = this_action_ycl
    if turns > 0:
        turns = extra_action_strength(this_action_direction, turns, current_time, current_value, current_bw1r,
                                      bw1r20min_delta, global_result)
    global_result['本次调整组数'] = turns
    global_result['是否拐点初次调整'] = turn_init
    if turns > 0:
        if this_guaidian_time == last_guaidian_time or turn_init == 1:
            times = default_cache.get(f'LQD_TURN_ACTION_TIMES', 0)
            default_cache.set(f'LQD_TURN_ACTION_TIMES', times + 1, TTL)
            global_result['共调整次数'] = times + 1
        default_cache.set(f'LQD_TURN_INIT', 0, TTL)
        default_cache.set(f'LQD_TURN_YCL_ACTION_VALUE', this_action_ycl, TTL)
        default_cache.set(f'LQD_TURN_YCL_ACTION_TIME', get_time_str(this_action_time), TTL)
        had_action_turns = default_cache.get(f'LQD_TURN_ACTION_AMOUNT', 0)
        default_cache.set(f'LQD_TURN_ACTION_AMOUNT', had_action_turns + turns, TTL)
        global_result['拐点共调整组数'] = had_action_turns + turns
        default_cache.set('LQD_LAST_ACTION_TIME', get_time_str(current_time), TTL)

        action(turns, global_result, this_action_direction, point_delta)
    else:

        turns, action_direction = ycl_return_central_value(current_time, current_value, ycl20min_delta, bw1r20min_delta,
                                                           bw2r20min_delta, global_result)

        if turns == 0:
            turns, action_direction = bd4r_delta_action(global_result, current_time, ycl10min_delta,
                                                        this_action_direction)

        if turns > 0:
            new_turns = extra_action_strength(action_direction, turns, current_time, current_value, current_bw1r,
                                              bw1r20min_delta, global_result)
            if new_turns > 0:
                default_cache.set('LQD_LAST_ACTION_TIME', get_time_str(current_time), TTL)
                action(new_turns, global_result, action_direction, point_delta)
        move_action_point(this_action_time, this_action_ycl, current_time, current_value, delta_value, global_result)


def check_auto_lqd(current_time):
    auto_flag = get_data("8", "AUTO_LQ", get_time_str(current_time - datetime.timedelta(minutes=8)),
                         get_time_str(current_time))
    if auto_flag[0]['value'] == 1 and auto_flag[-1]['value'] == 0:
        for i in range(9):
            default_cache.set(f'LQD_TURN_ACTION_C{i + 1}', 0, TTL)
        return 1
    return 0


# 到拐点刷新轮次
def turn_action(last_guaidian_time, guaidian_time, guaidian_value, current_value, last_action_direction, global_result,
                init, current_time, guaidian_bw1r, guaidian_bw2r, pre_guaidian20min_bw1r):
    this_action_direction = 1 if current_value > guaidian_value else -1

    if last_guaidian_time and last_guaidian_time <= guaidian_time:
        if get_time(last_guaidian_time) + datetime.timedelta(minutes=6) > get_time(guaidian_time):
            global_result['YCL拐点连续，本次拐点不算'] = f"上次拐点{last_guaidian_time}, 本次拐点{guaidian_time}"
            init = 0
        elif last_action_direction == this_action_direction:
            global_result['YCL连续同向变化，不刷新拐点'] = True
            init = 0
        elif abs(current_value - guaidian_value) < YCL_INIT_ACTION_DELTA_THRESHOLD:
            global_result['YCL变化还未到调控值，不刷新拐点'] = True
            init = 0
        else:
            init = 1
    if not init:
        init = check_auto_lqd(current_time)
    if init:
        default_cache.set(f'LQD_TURN_GUAI_DIAN_TIME', guaidian_time, TTL)
        default_cache.set(f'LQD_TURN_GUAI_DIAN_VALUE', guaidian_value, TTL)
        default_cache.set(f'LQD_TURN_ACTION_DIRECTION', this_action_direction, TTL)
        default_cache.set(f'LQD_TURN_YCL_ACTION_VALUE', guaidian_value, TTL)
        default_cache.set(f'LQD_TURN_YCL_ACTION_TIME', guaidian_time, TTL)
        default_cache.set(f'LQD_TURN_ACTION_POS', 0, TTL)
        default_cache.set(f'LQD_TURN_INIT', 1, TTL)
        default_cache.set(f'LQD_TURN_ACTION_AMOUNT', 0, TTL)
        default_cache.set(f'LQD_TURN_ACTION_TIMES', 0, TTL)
        default_cache.set('LQD_LAST_ACTION_POINT', '', TTL)
        if this_action_direction == 1:
            guaidian_bw1r = min(guaidian_bw1r, pre_guaidian20min_bw1r)
        elif this_action_direction == -1:
            guaidian_bw1r = max(guaidian_bw1r, pre_guaidian20min_bw1r)
        default_cache.set('LQD_TURN_BW1R_VALUE', guaidian_bw1r, TTL)
        default_cache.set('LQD_TURN_BW2R_VALUE', guaidian_bw2r, TTL)
        default_cache.set('LQD_TURN_ACTION_BW1R_VALUE', guaidian_bw1r, TTL)
        default_cache.set('LQD_TURN_ACTION_BW2R_VALUE', guaidian_bw2r, TTL)
    return init


def retention_ci_change(global_result):
    for i in range(9):
        old_action = default_cache.get(f'LQD_TURN_ACTION_C{i + 1}', 0)
        this_action = global_result.get(KEYS[i], 0)
        default_cache.set(f'LQD_TURN_ACTION_C{i + 1}', round(old_action + this_action, 2), TTL)


# 算出距离上次调整需要调整几轮
def calc_action_amount(slope, delta_value, ycl_current_value, current_time, turn_init, last_action_time,
                       last_action_value, global_result, guaidian_value, current_value, point_delta,
                       this_action_direction, ycl10min_delta, ycl20min_delta, current_bw2r, current_bw1r,
                       bw1r10min_delta, bw2r10min_delta):
    if abs(ycl10min_delta) >= TEN_MIN_DELTA_ABNORMAL_THRESHOLD:
        global_result["YCL异常值过滤"] = f'10min变化为{ycl10min_delta},超过阈值{TEN_MIN_DELTA_ABNORMAL_THRESHOLD}'
        return 0, last_action_value, last_action_time
    if turn_init:
        if delta_value > 0:
            delta_value = delta_value - YCL_INIT_ACTION_DELTA_THRESHOLD + ACTION_YCL_CHANGE_THRESHOLD
            if delta_value < 0:
                delta_value = 0
        else:
            delta_value = delta_value + YCL_INIT_ACTION_DELTA_THRESHOLD - ACTION_YCL_CHANGE_THRESHOLD
            if delta_value > 0:
                delta_value = 0
    turns = int(abs(delta_value) / ACTION_YCL_CHANGE_THRESHOLD)
    if delta_value > 0:
        delta_value -= ACTION_YCL_CHANGE_THRESHOLD * turns
    else:
        delta_value += ACTION_YCL_CHANGE_THRESHOLD * turns

    if abs(slope) >= ACTION_SLOPE_THRESHOLD3:
        turns *= 3
    elif abs(slope) >= ACTION_SLOPE_THRESHOLD2:
        turns *= 2
    elif abs(slope) >= ACTION_SLOPE_THRESHOLD1:
        turns *= 1
    else:
        # 快速变化0.5KG一调，缓慢变化除于1.5
        turns = int(turns / 1.5)

    turns = ycl_last_action_delta_amount(slope, guaidian_value, current_value, turns, global_result, current_bw2r,
                                         this_action_direction, current_bw1r, bw1r10min_delta, bw2r10min_delta)
    if turns > 0 and abs(ycl20min_delta) < 0.3:
        global_result['YCL变缓修正调整'] = f"修正前调整组数{turns}, 修正后调整组数0"
        turns = 0
    if 1 <= turns <= 3 and abs(slope) < ACTION_CORRECTION_SLOPE_THRESHOLD:
        not_action_number = 0

        for i, delta in point_delta:
            if delta >= PV_SP_DELTA_THRESHOLD and this_action_direction == 1:
                not_action_number += 1
            elif delta <= -PV_SP_DELTA_THRESHOLD and this_action_direction == -1:
                not_action_number += 1

        correction = min(turns, int((9 - not_action_number) / 3))
        if correction != turns:
            global_result['修正调整'] = f"修正前调整组数{turns}, 修正后调整组数{correction}"
        turns = correction

    if turns == 0 or slope == 0:
        return 0, last_action_value, last_action_time

    # 返回本次动作到的ycl值和时间，除不尽的部分留给下次调度
    return int(turns), ycl_current_value - delta_value, current_time - datetime.timedelta(
        seconds=round(delta_value / slope * 60))


def calc_ycl_change_slope(current_time, current_value, last_action_time, last_action_value):
    minutes = (current_time - last_action_time).seconds / 60
    delta_value = current_value - last_action_value
    if not minutes:
        return 0, 0, 0
    slope = round(delta_value / minutes, 2)
    return slope, delta_value, minutes


def action(turns, global_result, action_direction, point_delta):
    # choose_start = choose_action_point(action_direction)
    choose_start = default_cache.get(f'LQD_TURN_ACTION_POS', 0)
    start = int(choose_start) + 1
    end = int(choose_start + turns)

    if turns < 3:
        last_action_point = default_cache.get('LQD_LAST_ACTION_POINT', '')
        global_result["上次调控点"] = last_action_point
        action_amount = [0] * 9
        global_result['各回路PV-SP值'] = point_delta
        lose_position_point: List[int] = choose_lose_position_action_point(action_direction, turns)
        if lose_position_point:
            for point in lose_position_point:
                action_amount[point - 1] = 0.05
                last_action_point += f'{point}'
            global_result['sp失位调整'] = True
        else:
            for i in range(turns * 3):
                if action_direction == 1:
                    j = 0
                    while j < 9 and (last_action_point.find(str(point_delta[j][0])) != -1 or action_amount[
                        point_delta[j][0] - 1] != 0):
                        j += 1
                        if j == 9:
                            last_action_point = ''
                            j = 0
                else:
                    j = 8
                    while j >= 0 and (last_action_point.find(str(point_delta[j][0])) != -1 or action_amount[
                        point_delta[j][0] - 1] != 0):
                        j -= 1
                        if j == -1:
                            last_action_point = ''
                            j = 8
                point = point_delta[j][0]
                action_amount[point - 1] = 0.05
                last_action_point += f'{point}'
        default_cache.set('LQD_LAST_ACTION_POINT', last_action_point, TTL)
    # C7-C9, C4-C6, C1-C3
    else:
        action_every = [0, 0, 0]
        for turn in range(start, end + 1):
            pos = (turn - 1) % 3
            action_every[pos] += 1
        # C1, C2, C3, ..., C9
        action_amount = [
            (action_every[2]) * 0.05,
            (action_every[2]) * 0.05,
            (action_every[2]) * 0.05,
            (action_every[1]) * 0.05,
            (action_every[1]) * 0.05,
            (action_every[1]) * 0.05,
            (action_every[0]) * 0.05,
            (action_every[0]) * 0.05,
            (action_every[0]) * 0.05,
        ]
    for i in range(9):
        if action_amount[i] != 0:
            global_result[KEYS[i]] = action_amount[i] * -action_direction

    retention_ci_change(global_result)
    default_cache.set(f'LQD_TURN_ACTION_POS', end % 6, TTL)


def move_action_point(this_action_time, this_action_value, current_time, current_value, delta_value, global_result):
    slope, _, _ = calc_ycl_change_slope(current_time, current_value, this_action_time,
                                        float(this_action_value))
    if abs(delta_value) < ACTION_POINT_MOVE_DELTA_THRESHOLD and abs(slope) < 0.02:
        global_result['修改锚点'] = f'上次锚点{get_time_str(this_action_time)}, 修改后锚点：{get_time_str(current_time)}'
        default_cache.set(f'LQD_TURN_YCL_ACTION_VALUE', current_value, TTL)
        default_cache.set(f'LQD_TURN_YCL_ACTION_TIME', get_time_str(current_time), TTL)
    elif abs(delta_value) < 0.3 and this_action_time + datetime.timedelta(minutes=30) < current_time:
        global_result['修改锚点'] = f'上次锚点{get_time_str(this_action_time)}, 修改后锚点：{get_time_str(current_time)}'
        default_cache.set(f'LQD_TURN_YCL_ACTION_VALUE', current_value, TTL)
        default_cache.set(f'LQD_TURN_YCL_ACTION_TIME', get_time_str(current_time), TTL)


def ycl_last_action_delta_amount(slope, guaidian_value, current_value, turns, global_result, current_bw2r,
                                 action_direction, current_bw1r, bw1r10min_delta, bw2r10min_delta):
    had_action_turns = int(default_cache.get('LQD_TURN_ACTION_AMOUNT', 0))
    times = default_cache.get(f'LQD_TURN_ACTION_TIMES', 0)
    total_turns = int(abs(guaidian_value - current_value) / ACTION_YCL_CHANGE_THRESHOLD)

    if had_action_turns + turns > total_turns and times >= 2:
        global_result['限幅保护--超过总调整上限'] = \
            f'total_turns:{total_turns},had_action_turns:{had_action_turns},turns:{turns}'
        turns = total_turns - had_action_turns
        if turns < 0:
            turns = 0

    # 前两次调整且斜率较大 力度+两组
    if abs(slope) >= ACTION_SLOPE_THRESHOLD2 and times < 2:
        turns += 2

    temperature_name = choose_temperature(current_bw1r, current_bw2r, action_direction, global_result)
    if temperature_name == "BW1R":
        temperature_current = current_bw1r
        xishu = BW1R_ACTION_NUMBER
        delta_10min = bw1r10min_delta
    else:
        temperature_current = current_bw2r
        xishu = BW2R_ACTION_NUMBER
        delta_10min = bw2r10min_delta
    turns = temperature_delta_action_amount(global_result, temperature_name, temperature_current, turns,
                                            action_direction,
                                            had_action_turns, xishu, delta_10min)

    if turns >= 6:
        global_result['限幅保护--大趋势单次调整量上限为全员0.1'] = turns
        turns = 6
    elif 3 <= turns < 6:
        global_result['限幅保护--小趋势单次调整量上限为全员0.05'] = turns
        turns = 3
    if turns > 0:
        default_cache.set('LQD_TURN_ACTION_BW1R_VALUE', current_bw1r, TTL)
        default_cache.set('LQD_TURN_ACTION_BW2R_VALUE', current_bw2r, TTL)
    return turns


def get_mean(data, end_time):
    before_time = end_time - datetime.timedelta(seconds=60 * 2 + 10)
    end_time = end_time + datetime.timedelta(seconds=10)
    before_time = get_time_str(before_time)
    end_time = get_time_str(end_time)
    values = np.array([float(item["value"]) for item in data if before_time <= item["time"] <= end_time])
    if not values.any():
        return None
    return round(np.mean(values), 2)


def choose_lose_position_action_point(action_direction, turns):
    c1 = default_cache.get(f'LQD_TURN_ACTION_C1', 0)
    c2 = default_cache.get(f'LQD_TURN_ACTION_C2', 0)
    c3 = default_cache.get(f'LQD_TURN_ACTION_C3', 0)
    c4 = default_cache.get(f'LQD_TURN_ACTION_C4', 0)
    c5 = default_cache.get(f'LQD_TURN_ACTION_C5', 0)
    c6 = default_cache.get(f'LQD_TURN_ACTION_C6', 0)
    c7 = default_cache.get(f'LQD_TURN_ACTION_C7', 0)
    c8 = default_cache.get(f'LQD_TURN_ACTION_C8', 0)
    c9 = default_cache.get(f'LQD_TURN_ACTION_C9', 0)

    action_total = [[1, c1], [2, c2], [3, c3], [4, c4], [5, c5], [6, c6], [7, c7], [8, c8], [9, c9]]
    action_total.sort(key=lambda x: x[1])
    if abs(action_total[-1][1] - action_total[0][1]) >= 0.3:
        if action_direction == 1:
            action_total.sort(key=lambda x: -x[1])
            return [i for i, _ in action_total[:turns * 3]]
        else:
            action_total.sort(key=lambda x: x[1])
            return [i for i, _ in action_total[:turns * 3]]
    return None


def choose_action_point_follow_pv(current_time):
    point_delta = []
    for i in range(1, 10):
        pv_name = f"TC2_C{i}TH.PIDA.PV"
        sp_name = f"TC2_C{i}TH.PIDA.SP"

        pv_data = get_data("7", pv_name, get_time_str(current_time - datetime.timedelta(minutes=60)),
                           get_time_str(current_time + datetime.timedelta(seconds=10)))
        sp_data = get_data("7", sp_name, get_time_str(current_time - datetime.timedelta(minutes=3)),
                           get_time_str(current_time + datetime.timedelta(seconds=10)))

        cur_pv = get_mean(pv_data, current_time)
        cur_sp = get_mean(sp_data, current_time)

        point_delta.append([i, round(cur_pv - cur_sp, 2)])

    point_delta.sort(key=lambda tup: tup[1])

    return point_delta


def ycl_return_central_value(current_time, cur_ycl_value, ycl20min_delta, bw1r20min_delta, bw2r20min_delta,
                             global_result):
    # 25min内系统没有拉趋势
    this_action_direction = 0
    ycl_action_time = default_cache.get('LQD_LAST_ACTION_TIME', '')
    global_result['上次动作时间'] = ycl_action_time
    if ycl_action_time and get_time(ycl_action_time) + datetime.timedelta(
            minutes=YCL_LOCATION_ACTION_INTERVAL) > current_time:
        return 0, this_action_direction
    if cur_ycl_value >= YCL_HIGH_THRESHOLD:
        if ycl20min_delta <= -0.5:
            return 0, this_action_direction
        if bw2r20min_delta <= -0.05:
            return 0, this_action_direction
        this_action_direction = 1
    elif cur_ycl_value <= YCL_LOW_THRESHOLD:
        if ycl20min_delta >= 0.5:
            return 0, this_action_direction
        if bw2r20min_delta >= 0.05:
            return 0, this_action_direction
        this_action_direction = -1
    if this_action_direction != 0:
        if this_action_direction == 1 and bw1r20min_delta <= -TEMPERATURE_ACTION_DELTA_THRESHOLD:
            return 0, this_action_direction
        elif this_action_direction == -1 and bw1r20min_delta >= TEMPERATURE_ACTION_DELTA_THRESHOLD:
            return 0, this_action_direction
        global_result[
            "YCL长时间处于高低位调整"] = f'当前YCL值{cur_ycl_value},YCL20min变化量{ycl20min_delta},BW2R20min变化量{bw2r20min_delta}'
        return YCL_LOCATION_ACTION_TURN, this_action_direction
    return 0, this_action_direction


def temperature_delta_action_amount(global_result, temperature_name, current_value, turns, action_direction,
                                    had_action_turns, xishu, delta_10min):
    guai_dian_value = default_cache.get(f'LQD_TURN_{temperature_name}_VALUE', current_value)
    pre_action_value = default_cache.get(f'LQD_TURN_ACTION_{temperature_name}_VALUE', current_value)
    delta = round(current_value - pre_action_value, 2)
    global_result[f'{temperature_name}上次动作差值'] = delta
    # if abs(delta_10min) <= TEMPERATURE_ACTION_DELTA_THRESHOLD:
    #     global_result[f"{temperature_name}变化趋势较小退避"] = f"原调整次数{turns}"
    #     turns = 0
    # else:
    if ((action_direction == 1 and delta_10min <= -TEMPERATURE_ACTION_DELTA_THRESHOLD) or
            (action_direction == -1 and delta_10min >= TEMPERATURE_ACTION_DELTA_THRESHOLD)):
        global_result[f"{temperature_name}反方向变化动作退避"] = f"原调整次数{turns}"
        turns = 0
    else:
        upper_limit_turns = int((current_value - guai_dian_value) / 0.05 * xishu) * action_direction
        if had_action_turns + turns > upper_limit_turns:
            now_turns = upper_limit_turns - had_action_turns
            if now_turns < 0:
                now_turns = 0
            global_result[
                f"{temperature_name}限幅保护"] = f"{temperature_name}变化量{round(current_value - guai_dian_value, 2)}，最大调整上限{upper_limit_turns}，原调整次数{turns}，现调整次数{now_turns}"
            turns = now_turns
        elif had_action_turns + turns + 1 < upper_limit_turns:
            global_result[
                f'{temperature_name}变化快增大调整'] = f"{temperature_name}变化量{round(current_value - guai_dian_value, 2)}，最大调整上限{upper_limit_turns}，原调整次数{turns}，现调整次数{turns + 1}"
            turns += 1
    return turns


def choose_temperature(current_bw1r, current_bw2r, action_direction, global_result):
    pre_bw1r = default_cache.get('LQD_TURN_BW1R_VALUE', current_bw1r)
    pre_bw2r = default_cache.get('LQD_TURN_BW2R_VALUE', current_bw2r)

    delta_bw1r = round(current_bw1r - pre_bw1r, 2)
    delta_bw2r = round(current_bw2r - pre_bw2r, 2)
    global_result["温度变化量"] = f"BW1R变化量{delta_bw1r}, BW2R变化量{delta_bw2r}"
    if action_direction == 1:
        if delta_bw1r > 0 > delta_bw2r:
            return "BW1R"
        elif delta_bw1r < 0 < delta_bw2r:
            return "BW2R"
    elif action_direction == -1:
        if delta_bw1r > 0 > delta_bw2r:
            return "BW2R"
        elif delta_bw1r < 0 < delta_bw2r:
            return "BW1R"
    if BW1R_ACTION_NUMBER * abs(delta_bw1r) >= BW2R_ACTION_NUMBER * abs(delta_bw2r):
        return "BW1R"
    else:
        return "BW2R"


# 额外控制力度的加减
def extra_action_strength(action_direction, turns, current_time, current_ycl, current_bw1r, bw1r20min_delta,
                          global_result):
    # 根据来料决定额外力度
    f1l1rb_data = get_data("9", "F2R1RB", get_time_str(current_time - datetime.timedelta(minutes=150)),
                           get_time_str(current_time))
    cur_f1l1rb = get_mean(f1l1rb_data, current_time - datetime.timedelta(minutes=30))
    pre_f1l1rb = get_mean(f1l1rb_data, current_time - datetime.timedelta(minutes=120))
    if not cur_f1l1rb or not pre_f1l1rb:
        return turns
    delta_f1l1rb = round(cur_f1l1rb - pre_f1l1rb, 2)
    extra_turns = min(int(delta_f1l1rb / 0.1), 2)
    extra_turns = max(extra_turns, -2)
    global_result["来料-额外控制力度"] = f"F2R1RB变化量{delta_f1l1rb}，额外控制力度{extra_turns}"
    now_turns = turns
    if extra_turns != 0:
        if action_direction == 1:
            now_turns = turns + extra_turns if turns + extra_turns > 0 else 0
        elif action_direction == -1:
            now_turns = turns - extra_turns if turns - extra_turns > 0 else 0
        global_result[
            "额外控制力度"] = f"当前调整次数{turns}，额外控制力度{action_direction * extra_turns}，最终调整次数{now_turns}"

    if (
            current_bw1r > BW1R_CENTER_LINE and action_direction == 1 and bw1r20min_delta > TEMPERATURE_ACTION_DELTA_THRESHOLD) or (
            current_bw1r < BW1R_CENTER_LINE and action_direction == -1 and bw1r20min_delta < -TEMPERATURE_ACTION_DELTA_THRESHOLD):
        now_turns += BW1R_EXTRA_ACTION_TURN
        global_result["BW1R中心线额外力度"] = f"BW1R当前值{current_bw1r}, 额外调控组数{BW1R_EXTRA_ACTION_TURN}"

    return now_turns


def bd4r_delta_action(global_result, current_time, ycl10min_delta, this_action_direction):
    ycl_action_time = default_cache.get('LQD_LAST_ACTION_TIME', '')
    if ycl_action_time and get_time(ycl_action_time) + datetime.timedelta(
            minutes=BD4R_DELTA_ACTION_INTERVAL) > current_time:
        return 0, this_action_direction
    bd4r_data = get_data("9", "BD4R.UNIQUE", get_time_str(current_time - datetime.timedelta(minutes=70)),
                         get_time_str(current_time))
    cur_bd4r = get_mean(bd4r_data, current_time)
    pre_bd4r = get_mean(bd4r_data, current_time - datetime.timedelta(minutes=60))
    if not cur_bd4r or not pre_bd4r:
        return 0, this_action_direction
    delta_bd4r = round(cur_bd4r - pre_bd4r, 2)
    bd4r_direction = 1 if delta_bd4r > 0 else -1
    ycl_direction = 1 if ycl10min_delta > 0 else -1 if abs(ycl10min_delta) > 0.3 else 0

    if abs(delta_bd4r) > BD4R_ACTION_DELTA and bd4r_direction != ycl_direction:
        global_result["BD4R变化过多LQD调整"] = f'BD4R 60min变化量{delta_bd4r}'
        return BD4R_DELTA_ACTION_TURN, ycl_direction
    return 0, this_action_direction
