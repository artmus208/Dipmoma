import unittest
from flask import url_for
from app import app


class TestFlaskApi(unittest.TestCase):                                          
    def setUp(self):                                                            
        self.app = app                                           
        self.app_context = self.app.test_request_context()                      
        self.app_context.push()                                                 
        self.client = self.app.test_client() 

    def test_hello(self):                                                       
        response =  self.client.get(url_for('api.hello'),                       
                                    content_type='text')                        

        self.assertEqual(response.get_data(as_text=True), 'hello') 


with app.test_request_context():
    """Testing url_for()"""
    print(url_for('static', filename="img/tf.svg"))
    print(url_for('_uploads.uploaded_file', setname='data', filename='test.txt'))
