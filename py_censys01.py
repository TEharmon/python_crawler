from censys.search import CensysHosts
h=CensysHosts()

try:
    #query=h.search("services.service_name:HTTP",per_page=5)
    #print(query())
    for page in h.search("services.service_name:HTTP",per_page=5, pages=2):
        print(page)
        print('')

except Exception as e:
    print('Thereare some errors...',e)
    
