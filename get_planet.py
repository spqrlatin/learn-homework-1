import ephem
from datetime import datetime


def get_consilation(planet_name: str) -> str:
    date = datetime.now()
    planet_name = planet_name
    planet_dict = {
        'mars': ephem.Mars(),
        'moon': ephem.Moon(),
        'mercury': ephem.Moon(),
        'sun': ephem.Sun(),
        'jupiter': ephem.Jupiter(),
        'venus': ephem.Venus(),
        'saturn': ephem.Saturn(),
    }

    planet = planet_dict.get(planet_name, None)
    if not planet:
        return "Вы ввели неверную планету"
    return f"Планета {planet_name.capitalize()} находится в созвездии {ephem.constellation(planet)[1]}"

if __name__ == '__main__':
    print(get_consilation("Mars"))
