import pandas as pd
import requests

url= "https://api.argentinadatos.com/v1/finanzas/indices/riesgo-pais"
url= "http://api.open-notify.org/iss-now.json"

req= requests.get(url)

if req.status_code==200:
    print("Request Exitoso")
    data= req.json()
       
else:
    print("Error Request")

# df = pd.DataFrame(data)
datos = pd.DataFrame(data) 


if __name__ == "__main__":
    print(datos.head())
