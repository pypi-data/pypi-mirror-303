import datetime
import numpy as np

TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
TIME_FORMAT_2 = '%Y-%m-%d %H:%M:%S'


def time_delta_check(current_item, values, cur_index, interval_, threshold_):
    iter_ = cur_index - 1
    cur_time = get_time(current_item['time'])
    while iter_ >= 0:
        time_str = values[iter_]['time']
        target_time = get_time(time_str)
        if cur_time - target_time > datetime.timedelta(seconds=interval_):
            break
        iter_ = iter_ - 1
    if iter_ >= 0:
        if abs(float(values[iter_]['value']) - float(current_item['value'])) > threshold_:
            return False
    return True


def get_time(time_str):
    if len(time_str) > 19:
        return datetime.datetime.strptime(time_str, TIME_FORMAT)
    else:
        return datetime.datetime.strptime(time_str, TIME_FORMAT_2)


def get_time_str(time_):
    return datetime.datetime.strftime(time_, TIME_FORMAT_2)


def get_value(pre_val, post_val, index, total):
    return pre_val + (post_val - pre_val) * (index + 1) / total


def point_to_line_distance(x0, y0, m, b):
    """
    来自通义千问
    计算点(x0, y0)到直线y = mx + b的距离
    """
    # 直线的法线向量n = (m, -1)
    # 点到直线的距离公式：|n·P0 - n·P| / ||n||
    numerator = abs(m * x0 - y0 + b)
    denominator = np.sqrt(m ** 2 + 1)
    return numerator / denominator


def linear_regression(y_):
    # 返回斜率和均方差
    lin_regress_num = len(y_)
    x_ = np.array(range(lin_regress_num))
    coef = np.polyfit(x_, y_, 1)
    model = np.poly1d(coef)
    y_pred = model(x_)
    mse = np.mean((y_ - y_pred) ** 2)
    mean_distance = mse / (coef[0] ** 2 + 1)
    return coef[0], mse, mean_distance, coef[1]


def abandon_abnormal_ycl(unique_data):
    filtered_time_ycls = []
    threshold_1_min = 1.35
    threshold_2_min = 2.0
    threshold_3_min = 3.0
    current_filter = -1000
    interval_1_min = 70  # seconds
    interval_2_min = 130
    interval_3_min = 190
    recover_step = 5
    # current_value = -9999
    normal_slope = None
    normal_truncate = None
    linear_start_index = None
    recover_index = None

    for index, item in enumerate(unique_data):
        if index > 0:
            is_normal = (time_delta_check(item, unique_data, index, interval_1_min, threshold_1_min)
                         and time_delta_check(item, unique_data, index, interval_2_min, threshold_2_min)
                         and time_delta_check(item, unique_data, index, interval_3_min, threshold_3_min)
                        )

            def get_dis(index_):
                return point_to_line_distance(index_ - linear_start_index, unique_data[index_]['value'],
                                              normal_slope, normal_truncate)

            value_in_recovery = (normal_slope is not None) and (get_dis(index) < 1 and get_dis(index - 1) < 1)

            if recover_index and index - recover_index < 5:
                filtered_time_ycls.append(item)
            elif value_in_recovery:
                # 接近异常值前的水平能恢复
                if not filtered_time_ycls:
                    print(f'bug here, unique_data[0]={unique_data[0]}, unique_data[-1]={unique_data[-1]}')
                if filtered_time_ycls:
                    last_normal_item = filtered_time_ycls[-1]
                else:
                    # FIX-0702 防止开始就遇到缺块，导致数据删除完
                    last_normal_item = {
                        'time': get_time_str(get_time(unique_data[0]['time']) - datetime.timedelta(seconds=30)),
                        'value': item['value']}
                time_delta = get_time(item['time']) - get_time(last_normal_item['time'])
                insert_num = 0
                if time_delta > datetime.timedelta(seconds=35):
                    insert_num = int(time_delta.seconds / 29.5)
                for j in range(insert_num - 1):
                    insert_time = get_value(get_time(last_normal_item['time']), get_time(item['time']), j,
                                            insert_num)
                    insert_value = get_value(float(last_normal_item['value']), float(item['value']), j, insert_num)
                    filtered_time_ycls.append({'time': get_time_str(insert_time), 'value': insert_value})
                filtered_time_ycls.append(item)
                # recover
                current_filter = -1000
                normal_slope = None
                normal_truncate = None
                linear_start_index = None
                recover_index = index

            elif is_normal:
                if current_filter < 0:
                    filtered_time_ycls.append(item)
                else:
                    if index - current_filter <= recover_step:
                        pass
                    else:
                        # print('#落在老逻辑里')
                        # 只有超过一定区间才能恢复
                        if not filtered_time_ycls:
                            print(f'bug here, unique_data[0]={unique_data[0]}, unique_data[-1]={unique_data[-1]}')
                        if filtered_time_ycls:
                            last_normal_item = filtered_time_ycls[-1]
                        else:
                            # FIX-0702 防止开始就遇到缺块，导致数据删除完
                            last_normal_item = {'time': get_time_str(
                                get_time(unique_data[0]['time']) - datetime.timedelta(seconds=30)),
                                'value': item['value']}
                        time_delta = get_time(item['time']) - get_time(last_normal_item['time'])
                        insert_num = 0
                        if time_delta > datetime.timedelta(seconds=35):
                            insert_num = int(time_delta.seconds / 29.5)
                        for j in range(insert_num - 1):
                            insert_time = get_value(get_time(last_normal_item['time']), get_time(item['time']), j,
                                                    insert_num)
                            insert_value = get_value(float(last_normal_item['value']), float(item['value']), j,
                                                     insert_num)
                            filtered_time_ycls.append({'time': get_time_str(insert_time), 'value': insert_value})
                        filtered_time_ycls.append(item)
                        # recover()
                        current_filter = -1000
                        normal_slope = None
                        normal_truncate = None
                        linear_start_index = None
                        recover_index = index
            else:
                # 第一个异常值记录位置
                # current_filter = index
                if current_filter >= 0:
                    continue
                recover_index = None
                # 往前倒推n个值，根据与拟合曲线的关系
                time_ = unique_data[index]['time']
                start_index = -1
                if index > 20:
                    ori_values = [float(item['value']) for item in filtered_time_ycls]
                    ori_values.extend(
                        [float(item['value']) for item in unique_data if item['time'] > filtered_time_ycls[-1]['time']])
                    ori_v_a = np.array(ori_values)

                    # 计算最近10分钟的拟合直线
                    # FIX: 0702-通过过滤后的YCL数据拟合斜率，否则存在连续缺块异常
                    slope, mse, _, truncate = linear_regression(ori_v_a[index - 21:index - 4])

                    distance_list = np.array(
                        [point_to_line_distance(i + 20 - index, ori_v_a[i], slope, truncate) for i in
                         range(index - 20, index)])
                    # print(f'distance_list={distance_list}')
                    # 找到第一个距离突变的点
                    for i in range(len(distance_list)):
                        distance = distance_list[i]
                        if distance > np.mean(distance_list[0:i + 1]) + 0.7:
                            start_index = index - 20 + i
                            start_index_time = unique_data[start_index]['time']
                            linear_start_index = max(0, start_index - 21)
                            slope, mse, _, truncate = linear_regression(ori_v_a[linear_start_index:start_index - 1])
                            normal_slope = slope
                            normal_truncate = truncate
                            # print(
                            #     f'start_index={start_index}, time={start_index_time}, slope={slope}, truncate={truncate}')
                            break

                if start_index < 0:
                    start_index = index - 3
                    # print(f'倒推3个点, start_index={start_index}')
                current_filter = max(start_index, 0)
                start_time = get_time(unique_data[start_index]['time'])
                # 往前倒推3个值删除（用时间1.5分钟过滤）
                length = len(filtered_time_ycls)
                for idx in range(length):
                    idx = length - idx - 1
                    before_time = get_time(filtered_time_ycls[idx]['time'])
                    if before_time >= start_time:
                        filtered_time_ycls = filtered_time_ycls[:-1]
                    else:
                        break
                if len(filtered_time_ycls) > 0:
                    current_value = float(filtered_time_ycls[-1]['value'])
        else:
            filtered_time_ycls.append(item)
    return filtered_time_ycls
