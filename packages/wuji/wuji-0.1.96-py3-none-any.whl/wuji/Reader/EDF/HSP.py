#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   HSP 
@Time        :   2023/12/13 16:42
@Author      :   Xuesong Chen
@Description :   
"""
import matplotlib.pyplot as plt

from wuji.Reader.EDF.Base import Base
import pyedflib

assert pyedflib.__version__ == '0.1.1038', print('please install pyedflib==0.1.1038 in coding.net')


class HSPEDFReader(Base):
    pass


if __name__ == '__main__':
    fp = '/Users/cxs/Downloads/chat-baseline-300641.edf'
    reader = HSPEDFReader(fp)
    sig = reader.get_signal(type='ecg', tmin=3600, tmax=3600 + 300)
    plt.plot(sig)
    plt.show()
    print()
    pass
