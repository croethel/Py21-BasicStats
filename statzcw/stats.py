import math
from typing import List

# There are four small datasets in this lab. You are to write a python package which contains a series of functions
# which can analyze these data sets. The package, statzcw, will have a series of python files,
# each of which implement a standard statistic.

# zcount(list: List[]) -> float
# zmean(list: List[]) -> float
# zmode(list: List[]) -> float
# zmedian(list: List[]) -> float
# zvariance(list: List[]) -> float
# zstddev(list: List[]) -> float
# zstderr(list: List[]) -> float
# zcorr(listx: List[], listy: List[]) -> float

# You may only use the following functions to construct your code:

# python builtin `sum()`
# python builtin `max()`
# python builtin `min()`
# python Math function `Math.sqrt()`
# python normal operators on floats (*, /, +, -, etc)
# Per Kris - can use len & sort

def zcount(list: List[float]) -> float:
    return len(list)

def zmean(list: List[float]) -> float:
    return sum(list) / len(list)

def zmode(list: List[float]) -> float:
    return max(set(list), key=list.count)

def zmedian(list: List[float]) -> float:
    sorted_list = sorted(list)
    n = len(list)
    index = (n - 1) // 2

    if n % 2 == 0:
        return sorted_list[index]
    else:
        return (sorted_list[index] + sorted_list[index + 1]) / 2

def zvariance(list: List[float]) -> float:
    count = zcount(list)
    mean = zmean(list)
    deviations = []
    squared_deviations = []
    for value in list:
        value_deviation = value - mean
        deviations += [value_deviation]
    for deviation in deviations:
        squared_deviation = deviation * deviation
        squared_deviations += [squared_deviation]
    squared_sum = sum(squared_deviations)
    sample_variance = squared_sum / (count - 1)
    return sample_variance

def zstddev(list: List[float]) -> float:
    return math.sqrt(zvariance(list))

def zstderr(list: List[float]) -> float:
    return zstddev(list) / math.sqrt(zcount(list))

def zcov(listx: List[float], listy: List[float]) -> float:
    n = zcount(listx)
    sum_of_product = 0
    counter = 0

    while counter < len(listx):
        product = listx[counter] * listy[counter]
        sum_of_product += product
        counter += 1

    sums = (sum(listx) * sum(listy)) / n

    cov = (sum_of_product - sums) / (n - 1)
    return cov

def zcorr(listx: List[float], listy: List[float]) -> float:
    cov = zcov(listx, listy)
    sx = zstddev(listx)
    sy = zstddev(listy)

    return (cov) / (sx * sy)