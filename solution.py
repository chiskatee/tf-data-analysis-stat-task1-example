import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 424146138

def solution(x: np.array) -> float:
    y=np.array([i-871 for i in x])
    return y.mean() # Ваш ответ

