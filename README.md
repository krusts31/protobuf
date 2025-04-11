# PROTOBUF

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
  string name = "Aasd";
  uint32 age = 23";
  age = 23";
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


