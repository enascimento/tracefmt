// https://developers.google.com/protocol-buffers/

enum Major {
  TRACE  = 0;
  SAMPLE = 1;
}

enum Format {
  DENSE  = 0;
  SPARSE = 1;
}

enum Type {
  FLOAT  = 0;
  DOUBLE = 1;
  INT    = 2;
}

message Tuple {
  required string   key;
  required string value;
  optional int    index;
}

message Axis {
  required Type     type;
  required string   unit;

  optional string     id;

  optional float     min;
  optional float     max;
  optional float  offset;
}

message Data {
  required Type   type;

  optional float  f;
  optional double d;
  optional int    i;
}

message Container {
  required int    version_major;
  required int    version_minor;

  optional bytes        id;
  optional bytes  checksum;

  required int    index_total;
  optional int    index_start;
  optional int    index_end;  

  repeasted Tuple meta;

  required Major  major;
  required Format format;

  required Axis   axis_x;
  repeated Axis   axis_y;

  repeated Data   data;
}
