#!/usr/bin/env python

import base64
import os

from avocado import Test
from avocado import main


class WhiteBoard(Test):

    """
    Simple test that saves test custom data to the test whiteboard

    :param whiteboard_data_file: File to be used as source for whiteboard data
    :param whiteboard_data_size: Size of the generated data of the whiteboard
    :param whiteboard_data_text: Text used when no file supplied
    :param whiteboard_writes: How many times to copy the data into whiteboard
    """

    def test(self):
        os.chdir(self.datadir)    # Just to stress out Avocado
        data_file = self.params.get('whiteboard_data_file', default='')
        data_size = self.params.get('whiteboard_data_size', default='10')
        if data_file:
            self.log.info('Writing data to whiteboard from file: %s',
                          data_file)
            whiteboard_file = open(data_file, 'r')
            size = int(data_size)
            data = whiteboard_file.read(size)
        else:
            offset = int(data_size) - 1
            data = self.params.get('whiteboard_data_text',
                                   default='default whiteboard text')[0:offset]

        iterations = int(self.params.get('whiteboard_writes', default=1))

        result = ''
        for _ in xrange(0, iterations):
            result += data
        self.whiteboard = base64.encodestring(result)


if __name__ == "__main__":
    main()
