import pandas as pd
import numpy as np
from hyppo.ksample import Energy


chat_id = 1126746074 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = Energy().test(x, y)
    if res.pvalue > 0.07:
        return False
    else:
        return True # Ваш ответ, True или False
