# cifer_aggregation/aggregation.py

from typing import List
import numpy as np

def average_parameters(parameters_list: List[List[float]]) -> List[float]:
    """
    รวมพารามิเตอร์โดยการคำนวณค่าเฉลี่ย

    :param parameters_list: รายการของพารามิเตอร์จากหลาย client
    :return: พารามิเตอร์ที่รวมแล้ว
    """
    if not parameters_list:
        raise ValueError("Parameter list is empty")
    
    num_parameters = len(parameters_list[0])
    averaged_parameters = [sum(p[i] for p in parameters_list) / len(parameters_list) for i in range(num_parameters)]
    
    return averaged_parameters

def weighted_average_parameters(parameters_list: List[List[float]], weights: List[float]) -> List[float]:
    """
    รวมพารามิเตอร์โดยใช้ weighted average

    :param parameters_list: รายการของพารามิเตอร์จากหลาย client
    :param weights: น้ำหนักที่ใช้สำหรับแต่ละ client
    :return: พารามิเตอร์ที่รวมแล้ว
    """
    if not parameters_list or not weights:
        raise ValueError("Parameter list or weights list is empty")
    if len(parameters_list) != len(weights):
        raise ValueError("Parameter list and weights list have different lengths")
    
    num_parameters = len(parameters_list[0])
    weighted_sum = [0] * num_parameters
    total_weight = sum(weights)
    
    for i in range(len(parameters_list)):
        for j in range(num_parameters):
            weighted_sum[j] += parameters_list[i][j] * weights[i]
    
    averaged_parameters = [ws / total_weight for ws in weighted_sum]
    
    return averaged_parameters

def geometric_median_parameters(parameters_list: List[List[float]]) -> List[float]:
    """
    รวมพารามิเตอร์โดยใช้ geometric median

    :param parameters_list: รายการของพารามิเตอร์จากหลาย client
    :return: พารามิเตอร์ที่รวมแล้ว
    """
    def geometric_median(data: np.ndarray, eps: float = 1e-5) -> np.ndarray:
        """
        คำนวณ geometric median ของข้อมูล

        :param data: ข้อมูลที่ใช้ในการคำนวณ
        :param eps: ค่าความแม่นยำที่ต้องการ
        :return: geometric median ของข้อมูล
        """
        data = np.array(data)
        median = np.mean(data, axis=0)
        while True:
            distances = np.linalg.norm(data - median, axis=1)
            nonzero_distances = distances > 0
            if np.any(nonzero_distances):
                weights = 1 / distances[nonzero_distances]
                weights /= weights.sum()
                new_median = np.average(data[nonzero_distances], axis=0, weights=weights)
                if np.linalg.norm(new_median - median) < eps:
                    return new_median
                median = new_median
            else:
                return median
    
    parameters_array = np.array(parameters_list)
    median_parameters = geometric_median(parameters_array)
    
    return median_parameters.tolist()
