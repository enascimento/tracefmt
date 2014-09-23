SHELL := /bin/bash

%_pb2.py    : %.proto
	@protoc --python_out=${CURDIR} ${<}

%.tfc %.txt : %.py  tracefmt_pb2.py
	@python ${<}

%.raw       : %.tfc tracefmt_pb2.py
	@protoc --decode_raw < ${<} > ${@}

protocol : tracefmt_pb2.py

example  : example.tfc example.txt example.raw

all      :  protocol example

clean    :
	@rm -f tracefmt_pb2.{py,pyc}
	@rm -f example.{tfc,txt,raw}

spotless : clean
