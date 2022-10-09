import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **data):
    self.contents = []
    for key, value in data.items():
      i = 0
      while(i < value):
        self.contents.append(key)
        i += 1

  def draw(self, ballsCount):
    if(ballsCount >= len(self.contents)):
      result = self.contents
    else:
      i = 0
      result = []
      while(i < ballsCount):
        result.append(self.contents.pop(random.randrange(len(self.contents))))
        i += 1
    return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successfulExperiments = 0
  i = 0
  while(i < num_experiments):
    currentHat = copy.deepcopy(hat)
    isSuccessful = True
    actualBalls = {}
    drawedBalls = currentHat.draw(num_balls_drawn)
    for ball in drawedBalls:
      if(ball not in actualBalls.keys()):
        actualBalls[ball] = 1
      else:
        actualBalls[ball] += 1

    for key, value in expected_balls.items():
      if(key not in actualBalls.keys()):
        isSuccessful = False
      elif(actualBalls[key] < value):
        isSuccessful = False
    
    if(isSuccessful):
      successfulExperiments += 1
    i += 1
  return successfulExperiments / num_experiments