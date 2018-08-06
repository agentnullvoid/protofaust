import faust
import google.protobuf
import importlib
import logging
import os
import subprocess

logger = logging.getLogger(__name__)


class ProtoFaustConverter(object):
    def __init__(self, input_dir=None, output_dir=None, validate=False):
        self._input_dir = input_dir
        self._output_dir = output_dir
        self._validate = validate
        self._loaded_modules = list()

        if self._validate:
            logger.info('ProtoFaust validation enabled')

    def run(self):
        ''' Builds and converts the specified .proto files into Faust records
        '''
        self._build()
        self._load_proto()
        self._convert()
        self._write_output_records()

    def _build(self):
        ''' Generates the *_pb2.py files from a directory of .proto files.
        '''
        # Assert that the paths exist, otherwise no point in spending more time
        assert os.path.exists(self._input_dir), "Error: The input directory does not exist!"
        assert os.path.exists(self._output_dir), "Error: The output directory does not exist!"

        # Ugh, so this is dumb, but we have to do it since protoc is stupid with regards
        # to paths and directories with multiple .proto files. We must iterate over
        # the input directory and find all .proto files, then do a check_call to convert them
        for filename in os.listdir(self._input_dir):
            if filename.endswith('.proto'):
                proto_in_str = os.path.join(self._input_dir, filename)
                subprocess.check_call(['protoc', '--proto_path', self._input_dir, '--python_out', self._output_dir, proto_in_str])

        logger.info('Generated all _pb2.py files from the .proto directory')

    def _load_proto(self):
        ''' Loads the generated Python classes into memory
        '''
        # From the output directory, identify all the _pb2.py files and their
        # module names, load them into memory
        prefix = os.path.basename(os.path.normpath(self._output_dir))

        for filename in os.listdir(self._output_dir):
            if filename.endswith('_pb2.py'):
                full_path = os.path.join(self._output_dir, filename)
                module = filename.replace('.py', '')
                full_module = prefix + "." + module

                # Load the module into memory, track it in a list so that we can
                # iterate over it for conversion
                _spec = importlib.util.spec_from_file_location(full_module, full_path)
                _module = importlib.util.module_from_spec(_spec)
                _spec.loader.exec_module(_module)
                self._loaded_modules.append(_module)

        logger.info('Loaded all generated modules into memory')

    def _convert(self):
        ''' Converts all loaded Protobuf models into Faust records.
        '''
        pass

    def _write_output_records(self):
        ''' Cleans up the output directory from _pb2.py files and writes out
        the equivalent Faust record Python files
        '''
        pass
