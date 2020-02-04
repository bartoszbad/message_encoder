import unittest

from functions import decode_message, encode_message, encode_word, is_shuffleable, shuffle

MESSAGE = '‘This is a long looong test sentence,\nwith some big (biiiiig) words!’'


class IsShuffleableTestCase(unittest.TestCase):
    def test_is_shuffleable(self):
        self.assertTrue(is_shuffleable('word'), True)
        self.assertTrue(is_shuffleable('worod'), True)
        self.assertTrue(is_shuffleable('worod'), True)
        self.assertTrue(is_shuffleable('1234'), True)

    def test_is_not_shuffleable(self):
        self.assertFalse(is_shuffleable('biiig'), False)
        self.assertFalse(is_shuffleable('bg'), False)
        self.assertFalse(is_shuffleable('g'), False)


class ShuffleTestCase(unittest.TestCase):
    def test_shuffle_unique(self):
        self.assertNotEqual('or', shuffle('or'))
        self.assertNotEqual('orooo', shuffle('orooo'))
        self.assertNotEqual('1234', shuffle('1234'))


class EncodeWordTestCase(unittest.TestCase):
    def test_is_encoded(self):
        self.assertNotEqual(('word', True), encode_word('word'))
        self.assertNotEqual(('woroood', True), encode_word('woroood'))
        self.assertNotEqual(('1234', True), encode_word('1234'))
        self.assertNotEqual(('[!@#', True), encode_word('[!@#'))

    def test_is_not_encoded(self):
        self.assertEqual(('big', False), encode_word('big'))
        self.assertEqual(('biiiig', False), encode_word('biiiig'))
        self.assertEqual(('!', False), encode_word('!'))
        self.assertEqual(('...', False), encode_word('...'))
        self.assertEqual(('....', False), encode_word('....'))


class EncodeMessageTestCase(unittest.TestCase):
    def test_is_message_encoded(self):
        self.assertNotEqual(MESSAGE, encode_message(MESSAGE))


class DecodeMessageTestCase(unittest.TestCase):
    def test_is_message_decoded(self):
        self.assertEqual(decode_message(encode_message(MESSAGE)), MESSAGE)
        self.assertEqual(decode_message(encode_message('[!#$')), '[!#$')
        self.assertEqual(decode_message(encode_message('Good bad NoTsObAd')), 'Good bad NoTsObAd')
        self.assertEqual(decode_message(encode_message('12345')), '12345')
        self.assertEqual(decode_message(encode_message('12225')), '12225')
        self.assertEqual(decode_message(encode_message('12225')), '12225')
        self.assertEqual(decode_message(encode_message('12225abfr')), '12225abfr')
        self.assertEqual(decode_message(encode_message('test, word ,')), 'test, word ,')
        self.assertEqual(decode_message(encode_message('my fa@#$vourite test')), 'my fa@#$vourite test')
        self.assertEqual(decode_message(encode_message('word word i word')), 'word word i word')

        """Works only because of lucky alphabetic order"""
        self.assertEqual(decode_message(encode_message('This test is a hard tset')), 'This test is a hard tset')

    def test_message_decoded_to_fail(self):
        self.assertNotEqual(decode_message(encode_message('test !@#$')), 'test !@#$')

        """Imperfections of decoder"""
        self.assertNotEqual(decode_message(encode_message('This tset is a hard test')), 'This tset is a hard test')


if __name__ == "__main__":
    unittest.main()
