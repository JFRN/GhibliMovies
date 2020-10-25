import unittest
from ghibli import GhibliConsumer


class GhibliConsumerTest(unittest.TestCase):
    def test_convert_film_url_to_id(self):
        """
        TODO: Add more test cases, fuzzed URLs, etc.
        """
        ghibli = GhibliConsumer()
        self.assertEqual(ghibli.convert_film_url_to_id(
            'https://ghibliapi.herokuapp.com/films/603428ba-8a86-4b0b-a9f1-65df6abef3d3'), '603428ba-8a86-4b0b-a9f1-65df6abef3d3')

    def test_convert_data_to_dict(self):
        """
        TODO: We are assuming that 'id' always exists. This may not be the case. Test it sometime.
        """
        pass

    def test_get_films_fixed(self):
        """
        TODO: Mock this
        TODO: Test for empty values
        TODO: Use list instead of dict for the people field and make sure the method returns dict
        """
        pass

    def test_get_people(self):
        """
        TODO: Mock this
        """
        pass

    def test_get_films(self):
        """
        TODO: Mock this
        """
        pass


if __name__ == '__main__':
    unittest.main()
