from aiohttp import ClientSession
from asyncio import run
appid = '2b55c282b70ca465a7ba760c0362cbee'
s_city = "Chelyabinsk"


# otvet = requests.get("http://api.openweathermap.org/data/2.5/find", params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
# print(otvet.json())


async def func():
    async with ClientSession() as session:
        wether = await session.get(f"http://api.openweathermap.org/data/2.5/find?q={s_city}&type=like&units=metric&APPID={appid}")
        return await wether.json()

def main():
    pogoda = run(func())
    print(f"погода в {pogoda['list'][0]['name']}: {pogoda['list'][0]['main']['temp']}")

if __name__ == "__main__":
    main()

