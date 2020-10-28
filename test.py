import unittest
from app.models import User,Pitch,Review,Role
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

class ReviewTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(id=1,username = 'James',password = 'potato', email = 'james@ms.com',bio="Time is an abstract")
        self.new_review = Review(id=5,review='Review for pitches',posted="2018-09-5",user = self.user_James )

    def tearDown(self):
        Review.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.id,5)
        self.assertEquals(self.new_review.review,'Review for pitches')
        self.assertEquals(self.new_review.posted,"2018-09-5")
        self.assertEquals(self.new_review.user,self.user_James)

    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)

    def test_get_review_by_id(self):
        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)
