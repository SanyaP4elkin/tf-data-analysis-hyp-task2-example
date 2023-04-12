import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = anderson_ksamp([x,y])
    if res[2] < 0.07:
        return True
    else:
        return False # Ваш ответ, True или False
