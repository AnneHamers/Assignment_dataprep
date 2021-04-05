# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#PART 1
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)
print(scorers)

#For variable report i've tried multiple solutions but both are not correct according to Wincpy check
#I don't know what i did wrong
report = scorer_0 + ' scored in the ' + str(goal_0) + 'nd minute \n' + scorer_1 + ' scored in the ' + str(goal_1) + 'th minute'
#report = f'{scorer_0} scored in the {goal_0}nd minute \n {scorer_1} scored in the {goal_1}th minute'
print(report)

#PART 2
player = 'Marco van Basten'
first_name = player[:(player.find(" "))]
last_name_len = len(player[6:])
name_short = player[0] + '.' + player[5:]
chant = (len(first_name) * (first_name + '! '))[0:-1]
good_chant = chant[-1] != ' '

print(player)
print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)
