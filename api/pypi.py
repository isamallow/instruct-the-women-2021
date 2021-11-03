import requests

# Referências sobre o uso do requests:
#
# Fazendo requisições:
# https://docs.python-requests.org/en/master/user/quickstart/#make-a-request
# Usando JSON retornado:
# https://docs.python-requests.org/en/master/user/quickstart/#json-response-content

def version_exists(package_name, version):
    base_url = "https://pypi.org/pypi"
    url = f'{base_url}/{package_name}/{version}/json'

    response = requests.get(url)
    if response.status_code == 404:
        return False

    return True
   

def latest_version(package_name):
    base_url = "https://pypi.org/pypi"
    url = f'{base_url}/{package_name}/json'

    response = requests.get(url)
    if response.status_code == 404:
        return None
    
    response = response.json()
    version = response['info']['version']
    
    return version