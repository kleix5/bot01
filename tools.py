import json



def jspSut(city: json, arg: str) -> float:
    """This function gives min,max,mean from json sutochno"""
    f = open(city)
    data = json.load(f)
    places = data['data']['objects']
    prices = []
    for i in places:
        for k, v in i.items():
            if k == 'price':
                prices.append(i[k])
    actions = {
        'max': lambda: max(prices),
        'min': lambda: min(prices),
        'mean': lambda: sum(prices)/len(places)
    }
    selected_action = actions.get(arg)
    f.close()
    return selected_action()



def jspYa(city: json, arg: str) -> float:
    """This function gives min,max,mean from json yandex"""
    f = open(city, encoding='utf-8', errors='ignore')
    data = json.load(f)
    places = data['data']['hotels']
    prices = []
    index = []
    for i in range(len(places)):
        prices.append(float(places[i]['offers'][0]['price']['value']))
    actions = {
        'max': lambda: max(prices),
        'min': lambda: min(prices),
        'mean': lambda: sum(prices)/len(places)
    }
    selected_action = actions.get(arg)
    f.close()
    return selected_action()




def jspOst(city: json, arg: str) -> float:
    """This function gives min,max,mean from json ostrovok"""
    f = open(city)
    data = json.load(f)
    places = data['map_hotels']
    prices = []
    index = []
    for i in range(len(places)):
        prices.append(float(places[i]['price']))
    actions = {
        'max': lambda: max(prices),
        'min': lambda: min(prices),
        'mean': lambda: sum(prices)/len(places)
    }
    selected_action = actions.get(arg)
    f.close()
    return selected_action()




def ssize(path: json, site: str) -> int:
    '''Defining amount of objects(hotels) in json.'''
    f = open(path, encoding='utf-8', errors='ignore')
    data = json.load(f)
    actions = {
        'sut': lambda: len(data['data']['objects']),
        'ost': lambda: len(data['map_hotels']),
        'ya': lambda: len(data['data']['hotels'])
    }
    selected_action = actions.get(site)
    f.close()
    return selected_action()




def  findvalOst(city: json, price=0) -> list:
    '''Returns value of objects(hotels) in json.'''
    f = open(city)
    data = json.load(f)
    places = data['map_hotels']
    value = []
    for i in range(len(places)):
        if float(places[i]['price']) >= price:
            value.append((i, places[i]['price'], places[i]['name'], places[i]['rating']))
            # print(i, places[i]['name'],':' ,  places[i]['price'])
    return value




def findsmallest(value: list) -> tuple:
    """Defines the smallest price. Aplied inside function"""
    smallest = value[0]
    smallest_index = 0
    for i in range(1, len(value)):
        if value[i][1] < smallest[1]:
            smallest = value[i]
            smallest_index = i
        else:
            continue
    return smallest


def sortvalOst(city: json, price=0) -> list:
    '''Sort value from findval().'''
    value = findvalOst(city, price=price)
    newArr = []
    for i in range(len(value)):
        smallest = findsmallest(value)
        newArr.append(value.pop(value.index(smallest)))
    return newArr


def  findvalYa(city: json, price=0) -> list:
    '''Returns value of objects(hotels) in json.'''
    f = open(city, encoding='utf-8', errors='ignore')
    data = json.load(f)
    places = data['data']['hotels']
    value = []
    for i in range(len(places)-1):
         if float(places[i]['offers'][0]['price']['value']) >= price:
                value.append((i, places[i]['offers'][0]['price']['value'], places[i]['hotel']['name'], places[i]['hotel']['rating']))
            # print(i, places[i]['name'],':' ,  places[i]['price'])
    return value

def sortvalYa(city: json, price=0) -> list:
    '''Sort value from findval().'''
    value = findvalYa(city, price=price)
    newArr = []
    for i in range(len(value)):
        smallest = findsmallest(value)
        newArr.append(value.pop(value.index(smallest)))
    return newArr


