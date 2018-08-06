import faust
import google.protobuf
import logging
import os
import subprocess

logger = logging.getLogger(__name__)


class ProtoFaustConverter(object):
    def __init__(self, input_dir=None, output_dir=None, validate=False):
        self._input_dir = input_dir
        self._output_dir = output_dir
        self._validate = validate

    def build(self):
        ''' Generates the *_pb2.py files from a directory of .proto files.
        '''

        # Assert that the input path exists, otherwise no point in spending more time
        assert os.path.exists(self._input_dir), "Error: The input directory does not exist!"

        proto_in_str = os.path.join(self._input_dir, '*.proto')
        subprocess.check_call(['protoc', '--proto_path', self._input_dir, '--python_out', self._output_dir, proto_in_str])

    def convert(self):
        ''' Converts all loaded Protobuf models into Faust records.
        '''

        # Assert that the output path exists, otherwise no point in spending more time
        assert os.path.exists(self._output_dir), "Error: The output directory does not exist!"
