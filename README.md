# ProtoFaust

ProtoFaust is a library that generaates Faust record classes from a directory
of .proto files. It first generates the Protobuf `*_pb2.py` files and then converts
them to generate `*_pb2_faust.py` files with classes that can be leveraged with Faust.

# Dependencies

ProtoFaust leverages several dependencies to work properly:

* [Faust](https://github.com/robinhood/faust) - Faust is a stream processing library, porting the ideas from Kafka Streams to Python.
* [Protobuf](https://github.com/google/protobuf) - Protocol Buffers (a.k.a., protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.
* [Python 3.6]

# Install

To use ProtoFaust, you just need to clone and `pip install` the repository, like so:

`$ git clone https://github.com/agentnullvoid/protofaust.git`\
`$ cd protofaust`\
`$ pip install .`

Then, to convert a directory of `.proto` files, you can start the process via:

`$ protofaust convert $ORIGIN_DIR $OUTPUT_DIR`

If you want a verbose output, you can pass in the `--verbose` flag, like so:

`$ protofaust --verbose convert $ORIGIN_DIR $OUTPUT_DIR`

License
----

MIT License

Copyright (c) 2018 Alberto De la Rosa Algarin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
