import requests
from typing import Final, Dict, List, Any
from pprint import pprint

BASE_URL: Final[str] = 'https://ghibliapi.herokuapp.com'

FILMS_ENDPOINT: Final[str] = 'films'
PEOPLE_ENDPOINT: Final[str] = 'people'


class GhibliConsumer:
    def get_films(self) -> List[Dict]:
        """
        TODO: Handle corner cases (check for HTTP 200, what if the JSON is invalid, what if it throws an exception)
        """
        r = requests.get(f'{BASE_URL}/{FILMS_ENDPOINT}')
        return r.json()

    def get_people(self) -> List[Dict]:
        """
        TODO: Handle corner cases (check for HTTP 200, what if the JSON is invalid, what if it throws an exception)
        """
        r = requests.get(f'{BASE_URL}/{PEOPLE_ENDPOINT}')
        return r.json()

    def get_films_fixed(self) -> Dict[str, Dict[str, Any]]:
        """
        Simulate that the /films endpoint works.
        Given that the people field of the /films endpoint is broken, we need a way
        map people and films without too much fuss
        TODO: Benchmark and tweak performance if needed in the future
        TODO: Make this more readable by using custom types
        """
        films = self.convert_data_to_dict(self.get_films())
        people = self.convert_data_to_dict(self.get_people())

        for film_id, film in films.items():
            film['people'] = {}

        for person_id, person in people.items():
            for i, film in enumerate(person['films']):
                people[person_id]['films'][i] = self.convert_film_url_to_id(
                    film)
                film_id = people[person_id]['films'][i]

                films[film_id]['people'][person_id] = person
        return films

    def convert_data_to_dict(self, data: List[Dict]) -> Dict[str, Dict[str, Any]]:
        """
        These endpoints JSON structure is flat, convert them to a proper map with IDs

        Go from [{'id', ...}, ...] to {'id': {...}, ...}
        """
        proper_map = dict()
        for x in data:
            proper_map[x['id']] = x
            proper_map[x['id']].pop('id', None)
        return proper_map

    def convert_film_url_to_id(self, url: str) -> str:
        return url.rpartition("/")[-1]
