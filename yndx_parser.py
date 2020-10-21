import yandex_search
from conf import cnf

user_id = cnf['user_id']
key_id = cnf['key_id']
if cnf['strict'] == True:
    strict = '"'
else:
    strict = ''

file_src = open('sources.txt', 'r')
file_req = open('request.txt', 'r')

sources = file_src.read().split('\n')
req = file_req.read().split('\n')[0]

yandex = yandex_search.Yandex(api_user=user_id, api_key=key_id)
i = 0
file_ans = open('ans.html', 'w')
for source in sources:
    q_text = f'site:{source} {strict}{req}{strict}' + "&sortby=rlv"
    res = yandex.search(q_text).items
    for item in res:
        print(i)
        file_ans.write(f'<p>{i}. <a href=' + item['url'] + ">" + item['url'][:60] + "</a></p>" + "\n")
        i += 1
