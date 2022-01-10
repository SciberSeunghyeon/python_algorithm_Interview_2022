height = [0,1,0,2,1,0,1,3,2,1,2,1] #answer is 6

def produce_layers(height):
  layers = []
  for iter in range(max(height)):
    layer = []
    for i, wall in enumerate(height):
      if wall:
        layer.append(1)
        height[i] -= 1
      else:
        layer.append(0)
    layers.append(layer)

  return layers

def list_rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

def process_layer(layer):
  layer = layer[layer.index(1):list_rindex(layer, 1) + 1]
  return layer.count(0)

layers = produce_layers(height)
answer = 0
for layer in layers:
  answer += process_layer(layer)

print(answer)
#MY SOLUITON
--------------------------------------------------------------
answer = 0
ln = len(height)

for i in range(1, ln - 1):
  #Find left_max and right_max.
  left_max = 0
  right_max = 0
  for j in range(0, i):
    left_max = max(left_max, height[j])

  for j in range(ln - 1, i, -1):
    right_max = max(right_max, height[j])

  #★☆min(left_max, right_max) is a height of surface!!!

  if (min(left_max, right_max) - height[i]) >= 0:
    answer += min(left_max, right_max) - height[i]

print(answer)
#LEETCODE SOLUTION