import pandas as pd
import numpy as np


chat_id = 345534690 # Ваш chat ID, не меняйте название переменной

import math

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    x_prob = x_success / x_cnt
    y_prob = y_success / y_cnt
    
    p_combined = (x_success + y_success) / (x_cnt + y_cnt)
    
    se = math.sqrt(p_combined * (1 - p_combined) * (1/x_cnt + 1/y_cnt))
    
    z_score = (x_prob - y_prob) / se
    
    z_critical = 1.34  # for alpha = 0.09 (one-tailed test)
    
    return abs(z_score) > z_critical
