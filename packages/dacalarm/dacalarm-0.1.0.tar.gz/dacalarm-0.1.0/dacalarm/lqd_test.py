import math

import numpy as np
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime, timedelta

from alarm.utils.dac_facade import get_data
from alarm.utils.ycl_abandon_abnormal import get_time_str


def cron_run(minutes, start_time, end_time):
    from alarm.lqd_1010 import do
    result = {"time": [], "value": [], "info": []}
    while start_time < end_time:
        one_end_time = start_time + timedelta(minutes=minutes)
        global_result = {}
        data = get_data('9', 'YCL.UNIQUE', get_time_str(one_end_time - timedelta(minutes=60)),
                        get_time_str(one_end_time))
        if len(data) > 80:
            do(data, global_result)

            if global_result:
                action_value = global_result.get('本次调整组数', 0)
                print('----------------------------------------------------------------------------------')
                print(global_result.get("当前YCL值时间"), global_result)
                if global_result.get('YCL长时间处于高低位调整'):
                    result['time'].append(global_result['当前YCL值时间'])
                    result['value'].append(global_result['当前YCL值'])
                    result['info'].append('YCL调整')
                    # print(global_result.get('YCL长时间处于高低位调整'))
                elif action_value:
                    action_time = global_result['当前YCL值时间']
                    value = global_result['当前YCL值']
                    turn_info = f'共:{global_result["拐点共调整组数"]},本:{action_value}'
                    result['time'].append(action_time)
                    result['value'].append(value)
                    result['info'].append(turn_info)

                    # print(one_end_time, global_result)
                    # if global_result.get('sp失位调整'):
                    #     print('sp失位调整', global_result.get('sp失位调整'))
                    # print(
                    #     f'action----------拐点共调整组数: {global_result["拐点共调整组数"]}, 本次调整组数: {action_value}')
                    # print('-----------------------------')
        else:
            pass
        start_time = one_end_time

    return result


def adjust_ycl(v_ycl):
    threshold = 2
    start_indices, end_indices = [], []

    # Detect regions
    is_abnormal = False
    pre_normal_v = 0
    start_idx = -1
    for i in range(1, len(v_ycl) - 1):
        if is_abnormal:
            if abs(v_ycl[i] - pre_normal_v) < threshold:
                start_indices.append(start_idx)
                end_indices.append(i)
                # print(f"start: {start_idx}, end: {i}")
                is_abnormal = False
        else:
            if abs(v_ycl[i] - v_ycl[i - 1]) > threshold:
                # start_indices.append(i - 1)
                start_idx = i - 1
                is_abnormal = True
                pre_normal_v = v_ycl[i - 1]

    # Interpolate values within detected regions
    v_ycl_corrected = v_ycl.copy()
    for start, end in zip(start_indices, end_indices):
        if start >= 0 and end < len(v_ycl) - 1:
            v_ycl_corrected[start:end + 1] = np.linspace(v_ycl[start], v_ycl[end + 1], end - start + 1)

    return v_ycl_corrected


date = '1017'
# dir = f'C:/Users/quan.zhang/Desktop/data/{date}/'
# dir = f'E:/zhanwan_code/tools/data/{date}/'
dir = f'D:/ws/alarm/{date}/'
file_info = [
    ('YCL.UNIQUE.csv', (1, 2), (1030, 1060), 'YCL', 'left', 'blue'),
    # ('F1L1RB.csv', (1, 2), (1625, 1630), 'F1L1RB', 'right', 'brown'),
    # ('F2R1RB.csv', (1, 2), (1615, 1620), 'F2R1RB', 'right', 'brown'),
    # ('D_DSPC.csv', (1, 2), (15, 40), 'D_DSPC', 'right', 'green'),
    # # ('S3RR.CL.csv', (1, 2), (1465, 1475), 'S3RR', 'right', 'teal'),
    # ('D3LR.UNIQUE.csv', (1, 2), (1465, 1475), 'D3LR', 'right', 'purple'),
    # ('TC2_C1TH.PIDA.SP.csv', (1, 2), (1271, 1281), 'C1SP', 'right', '#FFD700'),
    # ('TC2_C2TH.PIDA.SP.csv', (1, 2), (1253, 1263), 'C2SP', 'right', '#EE82EE'),
    # ('TC2_C3TH.PIDA.SP.csv', (1, 2), (1242, 1252), 'C3SP', 'right', '#008080'),
    # ('TC2_C4TH.PIDA.SP.csv', (1, 2), (1235, 1245), 'C4SP', 'right', '#FFD700'),
    # ('TC2_C5TH.PIDA.SP.csv', (1, 2), (1202, 1212), 'C5SP', 'right', '#2E8B57'),
    # ('TC2_C6TH.PIDA.SP.csv', (1, 2), (1189, 1199), 'C6SP', 'right', 'black'),
    # ('TC2_C7TH.PIDA.SP.csv', (1, 2), (1188, 1198), 'C7SP', 'right', '#9400D3'),
    # ('TC2_C8TH.PIDA.SP.csv', (1, 2), (1168, 1178), 'C8SP', 'right', '#708090'),
    # ('TC2_C9TH.PIDA.SP.csv', (1, 2), (1186, 1196), 'C9SP', 'right', 'gold'),

    # ('TC2_C2TH.PIDA.PV.csv', (1, 2), (1253, 1263), 'C2PV', 'right', 'cyan'),
    # # ('TC2_C2TH.PIDA.OP.csv', (1, 2), (56, 62), 'C2OP', 'right', 'pink'),
    # ('TC2_C5TH.PIDA.PV.csv', (1, 2), (1202, 1212), 'C5PV', 'right', '#FFD700'),
    # # ('TC2_C5TH.PIDA.OP.csv', (1, 2), (50, 65), 'C5OP', 'right', '#EE82EE'),
    # ('TC2_C7TH.PIDA.PV.csv', (1, 2), (1188, 1198), 'C7PV', 'right', '#008080'),
    # # ('TC2_C7TH.PIDA.OP.csv', (1, 2), (60, 75), 'C7OP', 'right', '#FFD700'),
    # ('TC2_C8TH.PIDA.PV.csv', (1, 2), (1168, 1178), 'C8PV', 'right', '#00008B'),
    # # ('TC2_C8TH.PIDA.OP.csv', (1, 2), (60, 75), 'C8OP', 'right', '#8B0000'),
    # ('TC2_C9TH.PIDA.PV.csv', (1, 2), (1186, 1196), 'C9PV', 'right', 'teal'),
    # # ('TC2_C9TH.PIDA.OP.csv', (1, 2), (50, 56), 'C9OP', 'right', 'coral'),
    # ('TC2_CETH.PIDA.OP.csv', (1, 2), (20, 40), 'CE', 'right', 'coral'),
    # ('SUM2.UNIQUE.csv', (1, 2), (30, 45), 'SUM2', 'right', '#D3D3D3'),
    # ('CR11R.CL.csv', (1, 2), (1192, 1198), 'CR11R', 'right', 'olive'),
    # ('BW1R.UNIQUE.csv', (1, 2), (1248, 1252), 'BW1R', 'right', 'orange'),
    # ('BW2R.UNIQUE.csv', (1, 2), (1219, 1223), 'BW2R', 'right', 'teal'),
    # ('BL4SHPC.csv', (1, 2), (45, 55), 'BL4SH', 'right', 'magenta'),
    # ('BD4R.UNIQUE.csv', (1, 2), (1220, 1230), 'BD4R', 'right', 'red')
]

start_time = f'2024-{date[:2]}-{date[2:]} 00:00:00'
end_time = f'2024-{date[:2]}-{date[2:]} 23:59:59'

start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

result = cron_run(5, start_time, end_time)
resampled_data = pd.DataFrame.from_dict(result)
resampled_data['time'] = pd.to_datetime(resampled_data['time'])

# 创建每 5 分钟的计算结果 trace
result_trace = go.Scatter(
    x=resampled_data['time'],
    y=resampled_data['value'],
    mode='markers+text',  # 显示点和文本
    text=[v for v in resampled_data['info']],
    textposition='top center',
    marker=dict(size=5, color='red'),
    name='冷却段动作',
    hovertemplate=
    '时间: %{x}<br>' +
    '值: %{y}<extra></extra>'
)
resampled_data['value'].to_csv("result.csv")

# Array of file information: (filename, column range, y-axis range, y-axis title)
traces = [result_trace]
for i, (file, cols, y_range, name, side, color) in enumerate(file_info):
    df = pd.read_csv(dir + file, usecols=range(3))

    time, value = pd.to_datetime(df.iloc[:, cols[0]]), df.iloc[:, cols[1]]
    # pd.set_option("display.max_rows", None)
    if name == 'YCL':   
        value.to_csv("original.csv")
        # trace1 = go.Scatter(x=time, y=value, mode='lines', name=name, yaxis='y', line=dict(color='blue'))
        # traces.append(trace1)
        value = adjust_ycl(value)  # Adjust YCL values if needed
        value.to_csv("adjust.csv")

    print(f"{name}[{math.floor(min(value))}, {math.ceil(max(value))}], {color}")
    yaxis = f'y{i + 1}' if i > 0 else 'y'
    if name == 'BW2R' or name == 'BW1R':
        # 4. 中心对称 EWMA（以 EWMA 的一种特殊形式处理）
        center_ewma = value.ewm(span=21, adjust=False).mean().iloc[::-1].ewm(span=21, adjust=False).mean().iloc[
                      ::-1].rolling(window=11).mean()
        trace = go.Scatter(x=time, y=center_ewma, mode='lines', name=name, yaxis=yaxis, line=dict(color=color))

    # Create a trace for the file with correct y-axis reference
    else:
        trace = go.Scatter(x=time, y=value, mode='lines', name=name, yaxis=yaxis, line=dict(color=color))
    traces.append(trace)

# Define layout with dynamic y-axis configuration
layout = go.Layout(
    title=f'{date}',
    xaxis=dict(title='时间'),
    yaxis=dict(title='N_YCL', side='left', range=file_info[0][2]),
    legend=dict(x=1, y=1)
)

# Add y-axes configurations dynamically
for i, (_, _, y_range, name, side, _) in enumerate(file_info[1:], start=2):
    layout[f'yaxis{i}'] = dict(
        title='',
        side=side,
        overlaying='y',
        showgrid=False,
        showline=False,
        showticklabels=False,
        range=y_range
    )

fig = go.Figure(data=traces, layout=layout)
fig.write_html(f'lqd{date}.html')
