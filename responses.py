import requests
import json
import constants as keys

def help():
        text = "/krypto <Valuutan koko nimi> <*Lisävalinta>\n"
        text += "/louhinta <Valuutan lyhenne> <*mhs>\n"
        text += "/louhinta <Näytönohjain>\n"
        text += "/osake <Osakkeen lyhenne>\n"
        text += "/kello <Näytönohjain>\n"
        text += "* = ei pakollinen\n"
        return text





def krypto(teksti, valinta):
    user_message = str(teksti).lower()
    print(user_message)

    if user_message == "eth" or user_message == "etukka":
        user_message = "ethereum"
    if user_message == "btc":
        user_message = "bitcoin"
    if user_message == "cfx" or user_message == "conflux":
        user_message = "conflux-token"
    if user_message == "snx" or user_message == "synthetix":
        user_message = "havven"

    url = "https://api.coingecko.com/api/v3/coins/" + user_message
    r = requests.get(url)

    if r.status_code == 200:
        try:
            data = r.json()

            kuvaus = teksti + ":\n"
            hinta = float(data['market_data']['current_price']['eur'])
            suunta_24h = float(data['market_data']['price_change_percentage_1h_in_currency']['eur'])
            if (valinta != "Ei_valintaa"):
                tilasto = str(data['market_data'][valinta]['eur'])
                teksti_tilasto = valinta + ": " + tilasto + '€'
            else:
                teksti_tilasto = ""

            teksti_hinta = str(hinta) + "€\n"
            teksti_suunta = "{:.2f}% 24h\n".format(suunta_24h)
            
            return kuvaus + teksti_hinta + teksti_suunta + teksti_tilasto
        except Exception as e:
            print(e)
            return "Väärä syöte :(."

def louhinta(teksti, hashit, palautus):

    user_message = str(teksti).lower()
    print(user_message)

    url = "https://api.minerstat.com/v2/coins?list=" + user_message
    r = requests.get(url)

    if r.status_code == 200:
        try:
            data = r.json()
            tuotto_krypto = float(data[0]['reward']) * hashit*10**6 * 24
            tuotto_usd = tuotto_krypto * data[0]['price']
            kuvaus_teksti = "24h tuotto " + str(hashit) + "Mh/s:\n"
            teksti_krypto = "{:.5f} ".format(tuotto_krypto) + user_message + "\n"
            teksti_usd = "{:.2f} $".format(tuotto_usd)
            if palautus == 0:
                return kuvaus_teksti + teksti_krypto + teksti_usd
            elif palautus == 1:
                return teksti + " " + str(hashit) + " Mh/s: " + teksti_usd
        except Exception as e:
            print(e)
            return "Error"


def osake(teksti):
    user_message = str(teksti).lower()
    print(user_message)

    url = "https://api.twelvedata.com/price?symbol=" + user_message + "&apikey=" + keys.STOCK_API_KEY
    url_2 = "https://api.twelvedata.com/time_series?symbol=" + user_message + "&interval=8h&apikey=" + keys.STOCK_API_KEY
    r = requests.get(url)
    r_2 = requests.get(url_2)

    if r.status_code == 200:
        try:
            data_2 = r_2.json()
            print(data_2['values'][0]['open'])

            data = r.json()
            print(data['price'])
            
            kuvaus = "Osake " + teksti + ":\n"
            hinta_osake = float(data['price'])

            paivan_muutos = ((hinta_osake - float(data_2['values'][0]['open'])) / float(data_2['values'][0]['open'])) * 100
            teksti_muutos = "{:.2f}%".format(paivan_muutos)

            teksti_osake = "{:.2f} $\n".format(hinta_osake)
            
            return kuvaus + teksti_osake + teksti_muutos
        except Exception as e:
            print(e)
            return "Väärä valinta, tai liikaa yrityksiä"
    else:
        print(r.status_code)

def kellotus(kortti):
    teksti = "COIN: CORE MEM PL\n"
    if kortti == "3070ti":
        teksti += "ETH: 1400 2450 245\n"
        teksti += "CFX: 1400 2400 240\n"
        teksti += "RVN: 1500 2400 245\n"
        teksti += "ERG: 1800 2700 240\n"
        teksti += "FIRO: 1400 1800 230\n"
        teksti += "FLUX: 1750 2600 200\n"
    elif kortti == "3060":
        teksti += "ETH: 1550 2500 150\n"
    elif kortti == "3060ti":
        teksti += "Ei tietoa, kysy Villeltä :D\n"
    elif kortti == "3060til":
        teksti += "ETH: 1400 2450 125\n"
        teksti += "CFX: 1450 2400 160\n"
        teksti += "ERG: 1350 2000 110\n"
    elif kortti == "3080ti":
        teksti += "ETH: 1200 1900 270\n"
        teksti += "CFX: 1250 1800 330\n"
        teksti += "RVN: 1250 1600 330\n"
        teksti += "ERG: 2040 2300 250\n"
        teksti += "FIRO: 1400 1800 340\n"
        teksti += "FLUX: 1750 2000 300\n"
    elif kortti == "3080":
        teksti += "ETH: 1200 2400 215\n"
        teksti += "CFX: 1400 2400 265\n"
        teksti += "RVN: 1300 2000 255\n"
        teksti += "ERG: 2040 2600 200\n"
        teksti += "FIRO: 1400 1800 290\n"
        teksti += "FLUX: 1750 2600 250\n"
    elif kortti == "3080l":
        teksti += "ETH: 1100 2450 190\n"
    elif kortti == "3070":
        teksti += "ETH: 1100 2600 125\n"
    elif kortti == "3070l":
        "Ei tietoa, kysy Villeltä :D\n"
    elif kortti == "1660s":
        teksti += "ETH: 1100 2100 80\n"
        teksti += "Samsung tai Micron\n"
    
    print(kortti)

    return teksti