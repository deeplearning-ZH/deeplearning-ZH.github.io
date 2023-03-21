import numpy as np
import matplotlib.pyplot as plt
import struct


def xshow(filename, nx, nz):
    """

    :param filename: InSAR数据的路径，可以是相对路径，可以是绝对路径
    :param nx: 行号（如果显示的图像不对，可以试着设置为列号，nz设置为行号）
    :param nz: 列号 （如果显示的图像不对，可以试着设置为行号，nx设置为列号）
    :return: 二维矩阵
    """
    f = open(filename, 'rb')
    pic = np.zeros((nx, nz))
    for i in range(nx):
        for j in range(nz):
            data = f.read(4)
            elem = struct.unpack("f", data)[0]
            pic[i][j] = elem
    f.close()
    return pic


if __name__ == '__main__':
    file = r''
    cols = 1200
    lines = 1200
    data = xshow(filename=file, nx=cols, nz=lines)
    plt.imshow(data)
    plt.show()