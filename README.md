# PROTOBUF

<mark>There is also a thing called FlatBuffers that is worth checking out if you ever return to this repo when thinking if to use protbuf</mark>

seriliztion vs deserilization
what format to chose for seriliztion

Lets say we have a object like 
```
User
username: lol
password: hahah
```

So we would change this object to some datastructure to save it.
Then we would the data saved datastructure and "deserialize it" to get data.

1. The ideal serilization protocol would be language agnosite so we would be able to open it multiple languages and it would work acres OS.
2. Size of serialized data is as little as possible
3. Keep the relationships between objects.

## how to name file

`.proto`

### A good rool of thumb
the `smaller` the serilized data the harded human redeable it becomes
the `bigger` the serilized data the harder machine redables it becomes.

## Most popular serilization fromats

XML 1998
very verbose, has a lot of boilder plate
```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<root testAttr="testValue">
  <result>
    <child>data1</child>
    <child>A1343358848.646</child>
    <child>
      <internal>
       <data>one</data>
       <data>two</data>
       <unique>Z1343358848.646</unique>
</internal>
    </child>
  </result>
</root>
```
JSON 2000
less verbose, has types, has arrays
```json
{
  "id":"6ce4a00a-677d-4265-8144-4873d3d0075d",
  "url":"https://api.filepreviews.io/v2/previews/6ce4a00a-677d-4265-8144-4873d3d0075d/",
  "year": 2009,
  "status":"success",
  "names": ["Alex", "Dude"]
  "preview":{
    "original_size":{
      "width":"1280",
      "height":"1024"
    },
  },
}
```

ProtoBuff 2001(dev) 2008 (public)

```protobuf
sytax = "proto3";

message Book {
  string name = 1;
  uint32 age = 2;
}
```

When it is serilized it gets converted in to binary but you can read in hexadecimal.

## Compiler

protobuff has a `Protoc` Compiler.
So you can feed in protovuf schema and it will transpile it to a choosen language giveing you the ideal storage types.

## Baisic types

int, float, string, bool

## WHAT HAppens to the name?

it does not get serilized.

## What are TAGS

min is 1 max go up to 500`000`000.
19`000 to 19999 are used for libs.

Tag is what is set after = ;
so 1 would be a tag here

message Book {
	string lol = 1;
}


## NULL

in protobuf 3 all the values are optional.

## ARRAY

```protobuf
message book {
	repeated string test = 1;//default value is []
}
```

## MAPS

```protobuf
message Book {
  map<string, string> contacts = 1;
}
```

You can use complex tyes as values but only simples types like int and string ar accepted as keys.
You can not put `repteted` before the keyword `map`.
defualt value empty map.

## Nestaed

```protobuf
message gf {
  string name = 1;
}

message test_2 {
  repeted gf nested = 1;
}
```

## Enumurations

```protobuf
enum FileType {
	UNSPECIFIED = 0; //default value on enum
	MP3 = 1;
	MP4 = 2;
	JPG = 3;
}
```

## OneOfs

The value can only be 1 or the other.

Use full for clasification models where the value is like on this is 0.76% dog.

Default value is OneOn with out default set.

```protobuf
message CatOrDog {
  oneof results {
    float cat = 1;
    float dog = 2;
  }
}
```


## How to import proto file in a nother protofile


```protobuf
import "myfile.proto";
```

## PACKAGES


```protobuf
package mycompany.fs// mycompany is the parent dir and //fs file name
```


```protobuf
package mycompany.fs; 

import “google/protobuf/timestamp.proto”; 

message File {
  google.protobuf.Timestamp created_at = 1;
} 
```

## Nested Messages

```protobuf
message Cat {
  enum Breed {
    UNSPECIFIED = 0;
    BENGAL = 1;
    BURMESE = 2;
  } 

  Breed breed = 1;
} 

message Dog {
  enum Breed {
    UNSPECIFIED = 0;
    DALMATIAN = 1;
    DOBERMANN = 2;
    //…
  } 

  Breed breed = 1;
} 
```

## EXERCISE

1. All in one .proto file as same level messages
```protobuf

message Article {
  string Text = 1;
}

enum VideoType {
  UNSPECIFIED = 0;
  MP4 = 1;
  MOV = 2;
}

message Video {
  VideoType Type = 1;
  string URL = 2;
}

message Content {
  oneof {
    Video video = 1;
    Article article = 2;
  }
}

message Course {
  string Name = 1;
  repeted string authors = 2;
  map<string, Lecture> lecture = 3;
}
```

2. All in one .proto file as nested messages 

```protobuf
message Course {
  message Lecture {
    message Viedo {
      enum Type {
        UNSPECIFIED = 0;
        MP4 = 1;
        MOV = 2;
      }
      VideoType Type = 1;
      string URL = 2;
    }

    message Article {
      string Text = 1;
    }

    oneof Content {
      Video video = 1;
      Article article = 2;
    }
  }

  string Name = 1;
  repeted string Authors = 2;
  map<string, Lecture>Lectures = 3;
}
```

3. Separate files with imports (a message per file) where VideoType is in the same file as Video

##### `Articel.proto`

```protobuf
message Article {
  string Text = 1;
}
```

##### `Video.proto`

```protobuf
enum VideoType {
  UNSPECIFIED = 0;
  MP4 = 1;
  MOV = 2;
}

message Video {
  VideoType Type = 1;
  string URL = 2;
}
```

##### `Lecture.proto`

```protobuf
import "Article.proto";
import "Video.proto";

message Lecture {
  oneof Content {
    Video Video = 1;
    Article Article = 2;
  }
}
```

##### `Course.proto`

```protobuf
import "Lecture.proto";

message Course {
  string Name = 1;
  repeted string Authors = 2;
  map<string, Lecture>Lectures = 3;
}
```

4. Separate files with imports and packages (a message per file all under the same package)

##### `Articel.proto`

```protobuf
message Article {
  string Text = 1;
}
```

##### `Video.proto`

```protobuf
enum VideoType {
  UNSPECIFIED = 0;
  MP4 = 1;
  MOV = 2;
}

message Video {
  VideoType Type = 1;
  string URL = 2;
}
```

##### `Lecture.proto`

```protobuf
package mycompany.mooc;

import "Article.proto";
import "Video.proto";

message Lecture {
  oneof Content {
    Video Video = 1;
    Article Article = 2;
  }
}
```

##### `Course.proto`

```protobuf
package mycompany.mooc;

import "Lecture.proto";

message Course {
  string Name = 1;
  repeted string Authors = 2;
  map<string, mycompany.mooc.Lecture>Lectures = 3;
}
```

5. Separate files with imports and packages (a message per file all under the same package)

##### `Articel.proto`

```protobuf
package mycompany.mooc.conntent;

message Article {
  string Text = 1;
}
```

##### `VideoType.proto`

```protobuf
package mycompany.mooc.conntent;

enum VideoType {
  UNSPECIFIED = 0;
  MP4 = 1;
  MOV = 2;
}
```

##### `Video.proto`

```protobuf
package mycompany.mooc.conntent;

import "VideoType.proto";

message Video {
  mycompany.mooc.conntent.VideoType Type = 1;
  string URL = 2;
}
```

##### `Lecture.proto`

```protobuf
package mycompany.mooc;

import "Article.proto";
import "Video.proto";

message Lecture {
  oneof Content {
    mycompany.mooc.conntent.Video Video = 1;
    conntent.Article Article = 2;
//you can also use package naem difference so mycompany.mooc.conntent - mycompany.mooc = conntent
  }
}
```

##### `Course.proto`

```protobuf

package mycompany.mooc;

import "Lecture.proto";

message Course {
  string Name = 1;
  repeted string Authors = 2;
  map<string, mycompany.mooc.Lecture>Lectures = 3;
}
```

## COMPILER

```bash
brew install protobuf
```

### Create file for programs
```bash
#here you can generate a pytyon out
protoc --python_out=. dummy.proto
#add -I just like in C when you need to tell protoc where to find proto files for compilation
```

### To encode the data
```bash
cat test.txt | protoc --encode=Course all_in_one.proto #encode

cat test.txt | protoc --encode=Course all_in_one.proto > test.bin
cat test.bin | protoc --decode=Course all_in_one.proto #decode
cat test.bin | protoc --decode_raw #here you can decode protoc if you don't know how the schema looks like
```


## PYTHON WITH PROTOBUF

### fieldmasks

so lets say you would print the whole message. 
Okay cool, but lets say you only want to print a part of the message that is when you would use a field mask.


## FORWARD COMPATIBILTY

We need to allow older versions of our applicatoins to work with older ones.

Backward compatibility is a design characteristic that allows a system allows to accept input form a earlier version of itself.


So what happens when the schema changes? SO lets say you add or remove fileds for a message. Unkonw ids get skiped and if the id does exist but we don't use it then it gets the default value.

```protobuf
package org.lf.pbtutorial.v1

message Account {
  uint64 id = 1;
}
```

```protobuf
package org.lf.pbtutorial.v2

message Account {
  uint64 id = 1;
  string name = 2;
}
```

`forward.txt`
```
id: 1
```

`backward.txt`
```
id: 1
name: linux
```

```bash
cat backwards | protoc --encode=org.lf.pbtutorial.v2.Account v2.proto | protoc ---decode=org.lf.pbtutorial.v1.Account v1.proto
id: 42 # was recognized
2: "linux" # was not recognized

cat forward | protoc --encode=org.lf.pbtutorial.v1.Account v1.proto | protoc ---decode=org.lf.pbtutorial.v2.Account v2.proto
id: 42

```

Adding new ids does not break backward and forward compatibilty


#### Reaning a filed

`v1.proto`
```protobuf
message Account {
  uint32 id = 1;
  string first_name = 2;
}
```

`v2.proto`
```protobuf
message Account {
  uint32 id = 1;
  string alias = 2;
}
```

`forward.txt`
```
id: 1
first_name: "linux"
```

`backward.txt`
```
id: 1
alias: "linux"
```

```bash
cat backwards | protoc --encode=org.lf.pbtutorial.v2.Account v2.proto | protoc ---decode=org.lf.pbtutorial.v1.Account v1.proto
id: 42 # was recognized
first_name: "linux"

cat forward | protoc --encode=org.lf.pbtutorial.v1.Account v1.proto | protoc ---decode=org.lf.pbtutorial.v2.Account v2.proto
id: 42
alias: "linux"

```

## Reserving

I did not know this but you can generate uuid.
```bash
uuidgen
```

You can use this `reserved` keyword to not allow the compilation of proto files if some fi

```protobuf
message Account {
  reserved 2, 15, 9 to 15;
  reserved "first_name", "last_name";
  uint32 id = 1;
}
```


v1
```protobuf
syntax = "proto3";
package org.lf.pbtutorial.v1;

message Account {
  uint32 id = 1;
  string first_name = 2;
  string last_name = 3;
}
```


v2
```protobuf
syntax = "proto3";
package org.lf.pbtutorial.v2;

message Account {
  reserved 2, 3;
  reserved "first_name", "last_name";
  uint32 id = 1;
  string alias = 4;
}
```

```bash
echo 'id: 42
first_name: "linux"
last_name: "penguin"' | \
protoc --encode=org.lf.pbtutorial.v1.Account v1.proto | \
protoc --decode=org.lf.pbtutorial.v2.Account v2.proto
#output
id: 42
```

#### What if we remove reserved
v3
```protobuf
syntax = "proto3";
package org.lf.pbtutorial.v2;

message Account {
  uint32 id = 1;
  string alias = 2; // Reusing field number 2
}
```

```bash
echo 'id: 42
first_name: "linux"' | \
protoc --encode=org.lf.pbtutorial.v1.Account v1.proto | \
protoc --decode=org.lf.pbtutorial.v2.Account v2.proto
# results
id: 42
alias: linux
```


### RULES FOR UPDATES

Do not chage/reuse tags

```protobuf
message User {
  string name = 1;
  int32 age = 2;
}
```

```protobuf
- string name = 1;
+ int32 id = 1;
```
then this will break protobuf since you encoded 1 as a string and now it is a int32. This will cause undefined behaviour.

Add new filed
use reserved keyword

Before chaning filed type
1. check the dock
2. add a new field


## What type to choose


So I never though about this but you would thing what are the valu of distribution. If lets say most value will be negative you can use `sint` if most are positive then use `int`. So this is the process of thinking what will the actual values mostly be.


## Learn mroe about protobuf options

`https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto`


## Services and gRPC

protobuf can not send data but it can defined how 2 application have to communicate in.

```protobuf
service FooService {
  rpc GetSomething(GetSomethingRequest) returs (GetSomethingResponse);
  rpc ListSomething(ListSomethingRequest) returs (ListSomethingResponse);
}
```

App 1 = GetSomething(GetSometihngReqeust) -> App 2
App 1 < GetSomethingResponse - App 2


## Style guid

use snake case

`foo_bar.proto`

1. sytnaxe

2. package

3. imports ordered alhpabeticaly

4. options

5. Defenitoins for our types
Name for Variables are in Pascal case.

enum all the fields are in UPERCASE with  _ to sepereate

6. Message fields are in sake case

7. services are in PascalCase.


## ENCODING

Write protocol

0|Varint|int32,int64,bool,enum,uint64,sint32,etc.
1|64-big|fixed64,sfixed64,double
2|Length-delimited|strings,bytes,embedded messages, repeated
5|32-bin|flaot,fixed32


A filed tad is encoded as a Varint.
The bigger the value of the tad the bigger is the overhead
filed tad 1 -> 5bit
filed tag 16 -> 13 bit
...
filed tag 535689911 -> 37 bit

The type fill also add a mem storage size.


```protobuf

syntax = "proto";

message MyMessage {
  uint32 id = 1;
}
#Encoded value
#00001 000
#tag   Type
```

## Varint

The samller the value the smaller the overhead.

value 300 -> 100101100

### ENCODING
```
#add leas sig bit
0000 0010 10101100
Then we rever the bypes
10101100 00000010
AC02
```

### DECODING

```
AC 10101100
02 00000010

Drop the lest sig bit

00000100101100 == 300
```

### ZigZag Encoding

Value Encoded as
0	0
-1	1
1	2
-2	3
4	4

Formula for ZigZag
```
bits == the value type. so if int32 then bits == 32
#encoding
(value >> bits -1)^(value << 1)
#decoding
(value >> 1)^-(value & 1)
```

Sint is encoded with ZigZag encoding on top of VarInt encoding.

So you fist do zigzag and then you do varint encoding.


### STIRNG ENDODING

```protobuf
syntax = "proto";

message MyMessage {
  string id = 1;
}
```
Lets say we want to set id to "test";


Encoded value would be `10 04 74 65 73 74`.
10 = wire type: 2 Tag: 1
04 = Length: 4
... The rest is ascii values in decimal.


### REPETED FILES ENDOCDING

#### When a repeated field is packed
TRUE FOR SIMPLE TYPES.
```
tag + type, length, value.
```

#### When a repeated field is other
for user defined types for comples types will give overhead.

```
tag + type value1, tag + type value2,
```


# Memory Palace


I will use my flast for this.

I arrive at the stairs on them sits a messanger(the messanger from travian roman faction) with boxes that have numbers on them. These boxes he pulls out from currly bags that have message writen on them.
1 Of the boxes is a wraped in sexy string underwarer, one of the boxes labled with `int`ernational.
You like the stinrg one so much that you decide to get a subscritpion so that it comes `repetedly to your house`. 
You say goodbye to the messangre and walk in. There is some stuff piled on the sides of the walk way, bikes, winter showles etc. You notice a good old fashinedn PhoneBook that you pick. When you open it  you ar suprized its full of Lord Of The Rings `maps`. You decide to pick `OneOf` them and go upstairs.  
As you walk up the stairs in turn in to MineCraft/Matrix Remix. You see throw all the blocks and how the string message you go slowly becomes a load of blocks. You can still tell those are the strings but if someone elese came along they would probably not know and mistake them for some other type of fabric. As you are in the matrix you can see how something from reality becomes data. The strings get converted in the binary, and the idea it self that it is a string  the length of the data and the data it self. You can see you age appearing on the left side of the screen. As it does you can see how a number gets devided in half reotated and then trun in to text. Baisicly MrWroldWide gets sawed in half on the begining we add a little bitte of meet and then we reverse it the other way so the the legs are where the head should be and put it in the fridge. Efficient hence protobuf. 


