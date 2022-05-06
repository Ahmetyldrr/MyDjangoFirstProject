

from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    
    def test_home_page(self):
        response = self.client.get('/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        
    def test_about_page(self):
            response = self.client.get('/about/')
            print(response.status_code)
            self.assertEqual(response.status_code, 200)
