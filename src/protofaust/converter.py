import faust
import protobuf
import logging

logger = logging.getLogger(__name__)


class ProtoFaustConverter(object):
    def __init__(self, directory, validate=False):
        self._directory = directory
        self._validate = validate

    def build(self):
        pass

    def convert(self):
        pass
