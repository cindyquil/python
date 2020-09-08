string_covid = '''

Confirmed Cases of COVID in OC by Select Cities
------------------------------------------------
City                Total Cases      Population
------------------------------------------------
Anaheim             8536             359,339
Costa Mesa          1730             115,830
Fountain Valley     480              56,652
Fullerton           2250             142,824
Garden Grove        2728             175,155
Huntington Beach    2259             203,761
Irvine              1513             280,202
Newport Beach       1073             87,180
Orange              2258             141,691
Santa Ana           9579             337,716
Stanton              615             39,307
Tustin              1178             81,369
Westminster          939             92,610
'''

tuple_covid = [("City", "Total Cases", "Population"),
               ("Anaheim", 8536, 359339),
               ("Costa Mesa", 1730, 115830),
               ("Fountain Valley", 480, 56652),
               ("Fullerton", 2250, 142824),
               ("Garden Grove", 2728, 175155),
               ("Huntington Beach", 2259, 203761),
               ("Irvine", 1513, 280202),
               ("Newport Beach", 1073, 87180),
               ("Orange", 2258, 141691),
               ("Santa Ana", 9579, 337716),
               ("Stanton", 615, 39307),
               ("Tustin", 1178, 81369),
               ("Westminster", 939, 92610)]

class City:
    def __init__(self, city_name='', total_cases=0, population=0):
        self.city_name = city_name
        self.total_cases = total_cases
        self.population = population


if __name__ == "__main__":
    print("test")
