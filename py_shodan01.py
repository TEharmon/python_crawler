import shodan
SHODAN_API_KEY='iZZg3ad1xuIhOE7TuulgA9YtZxKDiukn'
api=shodan.Shodan(SHODAN_API_KEY)
in_string=input("검색어를 입력하세요 ->> ")
co=' country:kr'
query=in_string+co
print(query)
try:

    results=api.search('query')


    for result in results['matches']:
        print('IP: {}',format(result['ip_str']))
        print(result['data'])
        print('')

except shodan.APIError as e:

    print('oops...There is API Error...The API is not normal, so do not panic.')

