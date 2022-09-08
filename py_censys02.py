from censys.search import CensysHosts

h=CensysHosts()

try:
    host=h.view('8.8.8.8',at_time='2022-07-28T17:49:05Z')
    print(host)

except Exception as e:
    print(e)
