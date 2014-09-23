import tracefmt_pb2 as tracefmt, Crypto.Cipher.AES as AES, random ; from array import array

# -----------------------------------------------------------------------------

# Example: DPA-style traces

# The target in this example is some device from which we can acquire power
# consumption traces: each time we invoke the device, it generates a random
# plaintext, encrypts it to produce a ciphertext and trace, and returns all
# three as a result.

def target() :
  # generate a cipher key
  k  = array( 'B', [ i                       for i in range( 0, 16 ) ] ).tostring()
  # generate a plaintext
  pt = array( 'B', [ random.getrandbits( 8 ) for i in range( 0, 16 ) ] ).tostring()
  # compute a ciphertext
  ct = AES.new( k ).encrypt( pt )

  # generate a "fake" power consumption trace for the encryption operation
  trace = []

  for i in range( 0, 100 ) :
    sample = tracefmt.Sample()

    sample.value.i32 = random.randint( 0, 2 ** 16 )
    sample.index     = i

    trace.append( sample )

  return pt, ct, trace

# The example uses the target device to construct a tracefmt container that
# stores l traces each with (an assumed) n samples (truncated from whatever
# the target device actually produces).  Note that

# - the x-axis is measured in seconds and the y-axis in volts,
# - a sparse sample format, meaning each sample has an index in addition to
#   a value, and trace-major order is used,
# - the container is annotated with meta data key-value pairs to associate 
#   a plaintext/ciphertext with each trace.

def example( l, n ) :
  # create a new container
  C = tracefmt.Container()

  # configure the number and length of traces in the container
  C.trace_count  = l
  C.trace_length = n

  # configure the sample format and order
  C.format = tracefmt.SPARSE
  C.order  = tracefmt.TRACE

  # configure the x-axis
  C.axis_x.type = tracefmt.INT32
  C.axis_x.unit = tracefmt.SECOND

  # configure the y-axis
  C.axis_y.extend( [ tracefmt.Axis() ] )
  C.axis_y[ -1 ].type = tracefmt.INT16
  C.axis_y[ -1 ].unit = tracefmt.VOLT

  # populate the container with samples
  for i in range( 0, l ) :
    pt, ct, trace = target()

    C.meta.extend( [ tracefmt.Meta() ] )
    C.meta[ -1 ].key   = "pt"
    C.meta[ -1 ].value =  pt
    C.meta[ -1 ].index =  i
    C.meta.extend( [ tracefmt.Meta() ] )
    C.meta[ -1 ].key   = "ct"
    C.meta[ -1 ].value =  ct
    C.meta[ -1 ].index =  i

    C.samples.extend( trace[ 0 : n ] )

  return C

# -----------------------------------------------------------------------------

if ( __name__ == "__main__" ) :
  # generate an example container, with 10 traces each of 100 samples
  C = example( 10, 100 )
  
  # dump a serialised, binary version of the container
  f = open( 'example.tfc', 'wb' )
  f.write( C.SerializeToString() )
  f.close()

  # dump a human-readable, stringified version of the container
  f = open( 'example.txt', 'wb' )
  f.write( str( C ) )
  f.close()

# -----------------------------------------------------------------------------
