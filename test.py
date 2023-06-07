import unittest
import requests


class TestAPI(unittest.TestCase):
    URL1 = "http://127.0.0.1:4000/beer"
    URL2 = "http://127.0.0.1:4000/add-beer"

    expected_result ={
    "1.beer_id": 73513517,
    "2.name": "Estrella",
    "3.price": 17.0,
    "4.alcoholPercentage": 6.6
    }

    data1 = {
        "priceFrom": 1,
        "priceTo": 20,
        "alcoholPercentageFrom": 4,
        "alcoholPercentageTo": 10
    }

    data2 ={
        "id": 10,
        "beer_id": 73513522,
        "name": "Falcon",
        "price": 9,
        "alcohol_percentage": 3.5
    }

    def test_1_get_beer(self):
        resp = requests.get(self.URL1 + "/73513517")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), self.expected_result)
        print("Test 1 completed")

    def test_2_search_beer(self):
        resp = requests.post(self.URL1, json=self.data1)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 6)
        print("Test 2 completed")

    def test_3_delete_beer(self):
        resp = requests.delete(self.URL1 + "/73513522")
        self.assertEqual(resp.status_code, 200)
        print("Test 3 completed")

    def test_4_add_beer(self):
        resp = requests.post(self.URL2, json=self.data2)
        self.assertEqual(resp.status_code, 200)
        print("Test 4 completed")

if __name__ == "__main__":
    tester = TestAPI()
    tester.test_1_get_beer()
    tester.test_2_search_beer()
    tester.test_3_delete_beer()
    tester.test_4_add_beer()