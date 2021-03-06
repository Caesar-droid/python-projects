import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """test for the class AnonymousSurvey"""
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question="What language did your first learn to speak?"
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
if __name__=='__main__':
    unittest.main()