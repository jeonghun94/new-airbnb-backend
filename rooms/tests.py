from rest_framework.test import APITestCase

# Create your tests here.


class test_cal(APITestCase):
    def test_two_plus_two(self):
        self.assertEqual(2 + 1, 4, "2+2 should be 4")
