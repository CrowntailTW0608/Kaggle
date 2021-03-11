
import random
from kaggle_environments.envs.rps.utils import get_score
last_react_action = None
last_10_result = []
k = 20
def myLogic(observation, configuration):
    global last_react_action, last_10_result
    if observation.step != 0 :
        last_10_result.append( observation.lastOpponentAction)
        last_10_result = last_10_result[::-1][:k][::-1]
    if observation.step <= k :
        result = random.randint(0, 2)
    else:
        mode_list = max(set(last_10_result), key=last_10_result.count)
        result = (mode_list + 1) % 3
            
    return result
