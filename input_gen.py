import random
hidden_var_name = ('sunny', 'foggy', 'rainy')
observation_var_name = ('no', 'yes')
input_list = []
i = 0
while(i<100):
    if random.random() < 0.8:
        input_list.append('sunny,no')
    else:
        input_list.append('sunny,yes')
    i+=1
i=0
while(i<100):
    if random.random() < 0.4:
        input_list.append('foggy,no')
    else:
        input_list.append('foggy,yes')
    i+=1
i=0
while(i<100):
    if random.random() < 0.2:
        input_list.append('rainy,no')
    else:
        input_list.append('rainy,yes')
    i+=1
random.shuffle(input_list)
for data in input_list:
    with open('input.txt', 'a') as f:        
        f.write(data)
        f.write('\n')