#dic1 = dict()
#dic1['a'].append(1)


#print(dic1['a'])
dict1 = {'a':2}
if 'a' in dict1:
    print('키존재 리스트')
    dict1['a'].append(1)
    print(dict1['a'])
else:
    dict1['a'] = [1]
    print(dict1['a'])

#dic1['a'] = ['1']
#print(dic1['a'])
#dic1['a'].append('2')

#print(dic1['a'])

#dic1['a'].append('3')
#print(dic1['a'])





from collections import defaultdict
#defaultDict1 = defaultdict(list)
#defaultDict1['a'].append(1)
#print(defaultDict1['a'])



#tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

#routes = {}
#for key, value in tickets:
#    if key in routes:
#        routes[key].append(value)
#    else:
#        routes[key] = [value]

#print(tickets)