import numpy as np
import pandas as pd
from read_data import xshow


def linear_correction(phase, height, height_data_without_nan):
    """

    :param phase:phase data ----> ndarray
    :param height: height data ----> ndarray
    :param height_data_without_nan:
    :return:
    """
    phase = phase
    height = height
    data = height_data_without_nan

    A = np.vstack([height, np.ones(len(height))]).T   # np.ones_like

    # 获得最小二乘系数
    a, b = np.linalg.lstsq(A, phase.T, rcond=None)[0]

    # 使用原始dem模拟高程相关大气相位
    original_height = data.dropna()

    original_height_array = original_height['height'].values

    # 通过已知的高程数据及拟合的最小二乘参数计算高程相关大气相位
    atm_phase = np.dot(original_height_array, a) + b

    # 根据原始高程数据的非nan值的index来使得根据高程得到的预测相位写入CSV文件中
    predict_ = pd.DataFrame(pd.Series(index=data[~data['phase'].isna()].index,
                                      data=np.array(atm_phase).astype(float)))

    data['predict_phase'] = predict_

    # 获得改正后的相位

    data['corrected_phase'] = data['phase'] - data['predict_phase']

    return data


if __name__ == '__main__':
    phase_data = xshow(filename='./data/phase', nx=1200, nz=1200)  # ndarray
    height_data = xshow(filename='./data/dem', nx=1200, nz=1200)  # ndarray
    lon_data = xshow(filename='./data/lon', nx=1200, nz=1200)  # ndarray
    lat_data = xshow(filename='./data/lat', nx=1200, nz=1200)  # ndarray
    data = pd.DataFrame(data=None, columns=['phase', 'lon', 'lat'])
    data['phase'] = phase_data.flatten()
    data['lon'] = lon_data.flatten()
    data['lat'] = lat_data.flatten()

    phase = data.dropna()['phase'].values
    lon = data.dropna()['lon'].values
    lat = data.dropna()['lat'].values
    height = data.dropna()['height'].values

    data = linear_correction(phase, height, data['height'].dropna().values)
    print()