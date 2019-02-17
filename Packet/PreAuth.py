# -*- coding: utf-8 -*-

from Packet.Writer import Writer


class PreAuth(Writer):
    def __init__(self):
        super().__init__()
        self.Id = 10100

    def process(self):
        self.putInt(2)
        self.putInt(13)
        self.putInt(1)
        self.putInt(41)
        self.putInt(17)
        self.putString('')
        self.putInt(2)
        self.putInt(2)
