import unittest
import core

class DomainTests(unittest.TestCase):
    def test_unknown_intent(self):
        self.assertIsNone(core.answer(core.read(core.DEFAULT),"library fine")["answer"])

    def test_alias_collision(self):
        rows=core.read(core.DEFAULT)
        rows[1]["hi"]=rows[0]["hi"]
        with self.assertRaises(ValueError): core.validate(rows)

    def test_challenge_queries(self):
        rows=core.validate(core.read(core.DEFAULT))
        for query,expected in core.read(core.DEFAULT.parent.parent/"qa/challenge.json"):
            with self.subTest(query=query):
                self.assertEqual(core.answer(rows,query)["answer"],expected)
