import pandas as pd
import requests

# url= "https://api.argentinadatos.com/v1/finanzas/indices/riesgo-pais"
# url= "http://api.open-notify.org/iss-now.json"

# req= requests.get(url)

# if req.status_code==200:
#     print("Request Exitoso")
#     data= req.json()
       
# else:
#     print("Error Request")

# # df = pd.DataFrame(data)
# datos = pd.DataFrame(data) 


# if __name__ == "__main__":
#     print(datos.head())
##################################3

def obtener_datos():
    url = "http://api.open-notify.org/iss-now.json"
    req = requests.get(url)

    if req.status_code == 200:
        print("Request Exitoso")
        data = req.json()
        datos = pd.DataFrame([{
            "timestamp": data["timestamp"],
            "latitude": data["iss_position"]["latitude"],
            "longitude": data["iss_position"]["longitude"],
            "message": data["message"]
        }])
        return datos
    else:
        print("Error en el Request")
        return pd.DataFrame()  # retorna vacío si falla

# Solo si ejecutas este archivo directamente
if __name__ == "__main__":
    df = obtener_datos()
    print(df.head())