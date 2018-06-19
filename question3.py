import random
goal = 20
current_goal = goal
way = []
ways = {}
before_break = 1000000
denom = [1,2,3,4]

while before_break:
   # while current_goal > 0:
    num = random.choice(denom)
    check = current_goal - num
    if check < 0:
        pass
    elif check == 0:
        way.append(num)
        way.sort()
        if "{}".format(way) in ways:
            before_break = before_break - 1
            way = []
            current_goal = goal
            pass
        else:
            ways["{}".format(way)] = 1
            way = []
            current_goal = goal
            before_break = 1000000
    else:
        way.append(num)
        if current_goal - num < 0:
            pass
        else:
            current_goal = current_goal - num

print len(list(ways))
book = list(ways)
book.sort()
print book
        
        
        
