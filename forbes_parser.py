import requests

url = 'https://www.forbes.com/forbesapi/org/powerful-brands/2020/position/true.json?limit=2000'



def get():
    result = requests.get(url)
    res = result.json()['organizationList']['organizationsLists']
    values = []
    for value in res:
        values.append(value.get('uri'))
    with open('src\\files\\brands.txt', 'w') as f:
        for val in values:
            f.write(val+'\n')


if __name__ == '__main__':
    get()

