# message_encoder
App for encoding and decoding message. Encoded message may be hard to read for machines (regular worlds with shuffled middle letters).

## To start the APP
    Open your terminal
    $ git clone https://github.com/bartoszbad/message_encoder
    $ cd message_encoder # Browse into the repo root directory
    Run tests to see if application is deploying correctly on your local machine:
    $ python3 -m unittest
    To run terminal version of encoder type:
    $ python3 encoder.py

## encoder.py allows to:
* encode you message to format: separator, encoded_message, seprator, list_of_original_words
* decode encoded message to format of original one - delivered message must be in encode format

## License:
Please see LICENSE file

