from .Arm import Arm
from .OneS import OneS


class Wrapper(Arm, OneS):

    def __init__(self, region, domain, access_key):
        super().__init__(region, domain, access_key)
