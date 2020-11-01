import assignment

# TODO: rozšiř řešení, aby fungovalo pro větší počet koulí

balls = assignment.get_balls() # [0, 1, 2]

first_result = assignment.weigh(balls[0:1], balls[1:2])
if first_result == "left":
    print(0)
elif first_result == "right":
    print(1)
else:
    print(2)
