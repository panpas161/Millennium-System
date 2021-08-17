from django.test import TestCase


class PrefectureTestCase(TestCase):
    fixtures = [
        "prefectures.json",
        "municipalities.json"
    ]
    def testrun(self):
        pass