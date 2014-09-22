tracefmt_pb2.py : tracefmt.proto
	@protoc --python_out=${CURDIR} ${<}

all   : tracefmt_pb2.py

clean :
	@rm -f tracefmt_pb2.py
