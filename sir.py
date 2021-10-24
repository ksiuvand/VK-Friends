import requests

token = '3872f36d3872f36d3872f36d0d3800ae06338723872f36d66a4e813309e2bb997c65531'
version = '5.107'
user_id = input("Введите id пользователя" + '\n')
sp = []


def get_friends_by_id(id):
    response = requests.get('https://api.vk.com/method/friends.get', params={
        'access_token': token,
        'v': version,
        'user_id': id,
        'fields': 'nickname'
    })

    data = response.json()

    f = open('itog.csv', mode="w")
    for i in data['response']['items']:
        node = '{}, {}, {}'.format(i['first_name'], i['last_name'], i['id'])+'\n'
        sp.append(i['id'])
        f.write(node)
    for i in sp:
        response = requests.get('https://api.vk.com/method/friends.get', params={
            'access_token': token,
            'v': version,
            'user_id': i,
            'fields': 'nickname'
        })
        if "error" not in response.json():
            data = response.json()
            f = open('itog.csv', mode="a")
            for j in data['response']['items']:
                node2 = '{}, {}'.format(j['first_name'], j['id']) + '\n'
                f.write(node2)
            f.close()


get_friends_by_id(user_id)


