import datetime
import json
import logging
from typing import Optional, List

import pandas as pd

from dacalarm.utils.dac_facade import default_cache
# from alarm.models import RuleDictStorage
# from utils.calc_rule_table import get_data_tree_cache, get_variable_list_in_all, CalcUtils
from dacalarm.utils.ycl_abandon_abnormal import get_time
# from common.db_utils import close_db_connection
# from common.redis import default_cache
# from variable_management.utils import get_variable_values_map

logger = logging.getLogger(__name__)


def get_execute_time(last_time, TIME_SHIFT: int, INTERVAL_MINS: int):
    # last_time是数组里最后一个数据的时间
    # TIME_SHIFT是cron表达式里第一位的偏移量
    # INTERVAL_MINS是cron表达式的间隔，表述每x分钟调度一次
    if isinstance(last_time, str):
        last_time = get_time(last_time)
    last_ref_time = last_time - datetime.timedelta(seconds=TIME_SHIFT)
    nearest_time = last_ref_time.minute // INTERVAL_MINS * INTERVAL_MINS
    execute_time = last_ref_time.replace(minute=nearest_time, second=0, microsecond=0) + datetime.timedelta(
        seconds=TIME_SHIFT
    )
    if execute_time < last_ref_time:
        execute_time += datetime.timedelta(minutes=INTERVAL_MINS)
    return execute_time


# @close_db_connection
# def query_actions(global_result, alarm_rule_id: int) -> dict:
#     # 注意这个函数只应该被最后一个规则调用
#     try:
#         rule_dict_table_ids = RuleDictStorage.objects.filter(alarmRule_id=alarm_rule_id).values_list("id", flat=True)
#         actions = {}
#         for excel_id in rule_dict_table_ids:
#             calc_tree = get_data_tree_cache(alarm_rule_id, excel_id)
#             if calc_tree is None:  # 如果获取不到规则树，则认定此规则未导入规则树
#                 logger.warning("ID为%s 趋势计算规则尚未导入规则树")
#                 continue
#             variable_list = get_variable_list_in_all(excel_id)
#             variable_value_map = get_variable_values_map(variable_list)
#             calc_util = CalcUtils(value_map=global_result, variable_value_map=variable_value_map)
#             rule_list, node_log = calc_util.calc_of_tree(calc_tree)
#             logger.debug(str(alarm_rule_id) + "\n" + node_log)
#             if rule_list:  # Todo 确认是否仅有触发的规则的时候才调用后续记录［即如果没有实际触发的话，就不记录］
#                 kv_map = {}
#                 for k, v in global_result.items():
#                     kv_map["@{" + k + "}"] = v
#                 for k, v in global_result.items():
#                     kv_map["#{" + k + "}"] = v
#                 rule_list = calc_util.clear_black_actions(rule_id=alarm_rule_id, excel_id=excel_id, rule_list=rule_list)
#                 for rule in rule_list:
#                     for action in rule.get("actions", []):
#                         actions[action.get("反控属性", "未定义")] = action
#             if not rule_list:
#                 logger.warning(str(alarm_rule_id) + "\n" + json.dumps(global_result, indent=4) + "\n" + node_log)
#         return actions
#
#     except Exception:
#         logger.exception("error")
#         return {}


def get_time_by_shift(last_time, TIME_SHIFT: int, INTERVAL_MINS: int, LAY_TIME) -> datetime.datetime:
    execute_time = get_execute_time(last_time, TIME_SHIFT, INTERVAL_MINS)
    return execute_time - datetime.timedelta(minutes=LAY_TIME)


def get_data_before_time(data: List[dict], end_time: datetime.datetime) -> list:
    res = []
    for ele in data:
        if get_time(ele["time"]) <= end_time:
            res.append(ele)
    return res


def get_expected_end_time(key, last_time, TIME_SHIFT: int, INTERVAL_MINS: int, LAY_TIME) -> Optional[datetime.datetime]:
    state_dict = json.loads(default_cache.get(key, "{}"))
    index = state_dict.get("__index__spec", -1)
    # index = -1 表示为无数据
    # index = 1 表示为第一次判断已过,即将进行第二次判断
    # index = 2 表示为第二次判断已过,即将进行第三次判断
    # index = 3 表示为第三次判断 (实际不存在)
    if index == -1:
        return get_execute_time(last_time, TIME_SHIFT, INTERVAL_MINS)
    if index == 1:
        return get_time_by_shift(last_time, TIME_SHIFT, INTERVAL_MINS, LAY_TIME)
    if index == 2:
        return None  # 触发异常回调终止


def centered_ewm(
    data: List[dict],
    span: Optional[float] = None,
    alpha: Optional[float] = None,
    adjust: bool = True,
):
    df = pd.DataFrame(data)
    forward_ewm = df["value"].ewm(alpha=alpha, span=span, adjust=adjust).mean()
    backward_ewm = df["value"][::-1].ewm(alpha=alpha, span=span, adjust=adjust).mean()[::-1]
    df["value"] = 0.5 * (forward_ewm + backward_ewm)
    data = df.to_dict(orient="records")
    return data


def bl4sh_pre(data):
    # 去重
    unique_data = []
    for row in data:
        time = row["time"]
        value = float(row["value"])
        if not unique_data or abs(value - float(unique_data[-1]["value"])) > 0.18:
            unique_data.append({"time": get_time(time), "value": value})
    return unique_data


def combine(data):
    # FIX-0703 合并间隔在x分钟以内的变化
    combine_minute = 4
    length = len(data)
    delta_data = []
    for i in range(1, length):
        post_item = data[i]
        prev_item = data[i - 1]
        delta_data.append({"time": post_item["time"], "value": float(post_item["value"]) - float(prev_item["value"])})
    combined_data = []
    for index, item in enumerate(delta_data):
        if not combined_data:
            combined_data.append(item)
        else:
            this_time = item["time"]
            prev_delta = combined_data[-1]
            prev_time = prev_delta["time"]
            if this_time - prev_time <= datetime.timedelta(minutes=combine_minute):
                # do combine
                combined_data = combined_data[:-1]
                sum_value = prev_delta["value"] + item["value"]
                if abs(sum_value) > 0.2:
                    combined_data.append({"time": this_time, "value": sum_value})
            else:
                combined_data.append(item)
    return combined_data


def get_bl4sh_delta(data):
    data = bl4sh_pre(data)
    # 往前遍历直至第一个方向不一致的位置为止，取变化量
    combined_delta = combine(data)
    print(f"combined data: {combined_delta}")
    combined_delta.reverse()

    if combined_delta:
        if len(combined_delta) == 1:
            return combined_delta[0]["value"]
        else:
            result = 0
            is_positive = combined_delta[0]["value"] > 0
            for delta in combined_delta:
                if (delta["value"] > 0 and is_positive) or (delta["value"] < 0 and not is_positive):
                    result += delta["value"]
                else:
                    break
        return result
    else:
        return 0


# ========以下不要复制===========
# import csv
# if __name__ == '__main__':
#     data_ = []
#     with open(r'../../testdata/0627_BL4SH.csv', 'r', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')
#         next(reader)
#         for row in reader:
#             time = row[0]
#             value = row[1]
#             data_.append({'time': time, 'value': value})

#     result_ = get_bl4sh_delta(data_)
#     print(result_)

