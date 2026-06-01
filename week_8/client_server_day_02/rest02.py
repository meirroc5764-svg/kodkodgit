import requests


def safe_get(url):
    try:    
        respons = requests.get(url)
        if respons.status_code == 404 :
            return None
        if respons.status_code == 200 :
            return respons.json()
    except Exception as e:
        raise e(f"eror {e}")  
  