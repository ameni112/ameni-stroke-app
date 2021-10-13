from app.app  import app
import unittest
class test(unittest.TestCase):
    def setUp(self):
        self.app=app1.app.test_client()
        self.app.testing=True
    def test_status_code(self):
        response=self.app.get("/")
        self.assertEqual(response.status_code,200)
if __name__ == "__main__":
    unittest.main() 