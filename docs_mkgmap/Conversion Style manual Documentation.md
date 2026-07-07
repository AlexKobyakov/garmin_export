# Conversion Style manual

## The mkgmap team


### Conversion Style manual

The mkgmap team

Publication date 13 January 2026


## Table of Contents




- 1. Introduction............................................................................................................................................
- 2. Designing the map................................................................................................................................
   - 2.1. The Garmin Map........................................................................................................................
      - 2.1.1. Resolution........................................................................................................................
      - 2.1.2. Level................................................................................................................................
      - 2.1.3. Overview Level...............................................................................................................
- 3. The structure of a style.........................................................................................................................
   - 3.1. Files.............................................................................................................................................
      - 3.1.1. Top level folder...............................................................................................................
   - 3.2. The version file..........................................................................................................................
   - 3.3. The info file................................................................................................................................
   - 3.4. The options file..........................................................................................................................
      - 3.4.1. Non command line options.............................................................................................
   - 3.5. The points file............................................................................................................................
   - 3.6. The lines file...............................................................................................................................
   - 3.7. The polygons file........................................................................................................................
   - 3.8. The relations file........................................................................................................................
- 4. Style rules..............................................................................................................................................
   - 4.1. Introduction.................................................................................................................................
      - 4.1.1. Tag and text values.........................................................................................................
   - 4.2. Tag tests......................................................................................................................................
      - 4.2.1. Allowed operations..........................................................................................................
      - 4.2.2. Combining tag tests.........................................................................................................
      - 4.2.3. Comparing the values of two tags................................................................................
      - 4.2.4. Functions........................................................................................................................
   - 4.3. Action block.............................................................................................................................
      - 4.3.1. add..................................................................................................................................
      - 4.3.2. set...................................................................................................................................
      - 4.3.3. delete..............................................................................................................................
      - 4.3.4. deletealltags....................................................................................................................
      - 4.3.5. addlabel..........................................................................................................................
      - 4.3.6. name...............................................................................................................................
      - 4.3.7. addaccess........................................................................................................................
      - 4.3.8. setaccess.........................................................................................................................
      - 4.3.9. apply...............................................................................................................................
      - 4.3.10. apply_once...................................................................................................................
      - 4.3.11. apply_first....................................................................................................................
      - 4.3.12. echo..............................................................................................................................
      - 4.3.13. echotags........................................................................................................................
   - 4.4. Variables...................................................................................................................................
      - 4.4.1. Variable filters...............................................................................................................
      - 4.4.2. Symbol codes.................................................................................................................
   - 4.5. mkgmap internal tags...............................................................................................................
      - 4.5.1. Tags evaluated by mkgmap...........................................................................................
      - 4.5.2. Tags added by mkgmap................................................................................................
   - 4.6. Element type definition............................................................................................................
      - 4.6.1. level................................................................................................................................
      - 4.6.2. resolution........................................................................................................................ Conversion Style manual
      - 4.6.3. default_name..................................................................................................................
      - 4.6.4. road_class.......................................................................................................................
      - 4.6.5. road_speed.....................................................................................................................
      - 4.6.6. continue..........................................................................................................................
      - 4.6.7. continue with_actions....................................................................................................
   - 4.7. Including files...........................................................................................................................
   - 4.8. Finalize section.........................................................................................................................
   - 4.9. Style syntax extension if then else...........................................................................................
   - 4.10. Troubleshooting......................................................................................................................
   - 4.11. Some examples.......................................................................................................................
      - 4.11.1. Simple examples..........................................................................................................
      - 4.11.2. More involved examples.............................................................................................
- 5. Creating a style....................................................................................................................................
   - 5.1. Testing a style..........................................................................................................................
      - 5.1.1. Tests performed by check-styles...................................................................................
   - 5.2. Making a style package............................................................................................................
      - 5.2.1. Zip archive.....................................................................................................................
      - 5.2.2. Simple file archive........................................................................................................
      - 5.2.3. The Garmin Map...........................................................................................................
      - 5.2.4. Resolution......................................................................................................................
      - 5.2.5. Level..............................................................................................................................
- 6. About...................................................................................................................................................
   - 6.1. Licence......................................................................................................................................
   - 6.2. Authors and acknowledgments................................................................................................
- 4.1. Full list of operations......................................................................................................................... List of Tables
- 4.2. Style functions..................................................................................................................................
- 4.3. List of all substitution filters............................................................................................................
- 4.4. Highway symbol codes....................................................................................................................
- 4.5. Tags for routable roads....................................................................................................................
- 4.6. Tags that control the treatment of roads..........................................................................................
- 4.7. POI address tags...............................................................................................................................
- 4.8. Tags added by mkgmap...................................................................................................................
- 4.9. Other internal tags............................................................................................................................
- 4.10. Road classes....................................................................................................................................
- 4.11. Road Speeds...................................................................................................................................
- 5.1. Resolutions........................................................................................................................................
- 3.1. An example info file.......................................................................................................................... List of Examples
- 3.2. An example options file.....................................................................................................................
- 4.1. Finalize section in the lines file with access handling.....................................................................
- 4.2. Internet cafes....................................................................................................................................
- 4.3. Guideposts........................................................................................................................................
- 4.4. Car sales rooms................................................................................................................................
- 4.5. Opening hours in postcode field......................................................................................................
- 4.6. Mountain Passes depending on the way they belong to..................................................................
- 5.1. Style package layout........................................................................................................................


Chapter 1. Introduction

This manual explains how to write a mkgmap style to convert between OSM tags and features on a
Garmin GPS device.

A style is used to choose which OSM map features appear in the Garmin map and which Garmin
symbols are used.

There are a few styles built into mkgmap, but as there are many different purposes a map may be used
for, the default styles in mkgmap will not be ideal for everyone, so you can create and use styles external
to mkgmap.

The term style could mean the actual way that the features appear on a GPS device, the colour, thickness
of the line and so on. This manual does not cover such issues, and if that is what you are looking for,
then you need the documentation for TYP files.

Few people will want to write their own style from scratch, most people will use the built in conversion
style, or at most make a few changes to the default style to add or remove a small number of features.
For general information about running and using mkgmap see the Tutorial document.

To be clear this is only needed for converting OSM tags, if you are starting with a Polish format file,
there is no style involved as the garmin types are already fully specified in the input file.

For general information about the OpenStreetMap project see the OpenStreetMap wiki [http://
wiki.openstreetmap.org].


Chapter 2. Designing the map

You can completely change which features are displayed and at what zoom levels.

First you need to understand a little about the way that the zoom works in Garmin maps. There are two
concepts resolution and level.

### 2.1. The Garmin Map........................................................................................................................

Each Garmin map may contain several separate maps which are prepared at different levels of detail, the
most appropriate of these is displayed depending on the zoom selected by the user.

When creating the map, the map maker will choose which of these level maps is displayed according to
the resolution (or zoom) selected. For example, a map might contain three levels (0, 1 & 2); On the level
2 map (showing the largest area) a town might just be represented by a named dot; as the user zooms in,
the display might switch to the level 1 map showing an outline of the town. Zooming in further might
switch to the level 0 map, with the individual streets of the town shown.

In addition the GPS itself might decide when to show or hide individual features in each of the level
maps, especially with POIs. This is also affected by the detail setting in the map config menu.

#### 2.1.1. Resolution........................................................................................................................

The first is resolution this is a number between 1 and 24 with 24 being the most detailed resolution and
each number less is half as detailed. So for example if a road was 12 units long at resolution 24 it would
be only 6 at resolution 23 and just 3 at resolution 22.

On a Legend Cx the resolution corresponds the these scales on the device:

```
Resolution Scale on device
16 30km-12km
18 8km-3km
20 2km-800m
22 500m-200m
23 300m-80m
24 120m-50m
```
It may be slightly different on different devices. There is an option to increase or decrease the detail and
if you change that from Normal then it will change the values above too.

#### 2.1.2. Level................................................................................................................................

The next is level. This is a number between 0 and 16 (although perhaps numbers above 10 are not
usable), with 0 corresponding to the most detailed view. The map consists of a number of levels starting
(usually) with 0. For example 0, 1, 2, 3 and a different amount of detail is added at each level.

The map also contains a table to link the level to the resolution. So you can say that level 0 corresponds
to resolution 24.

This mapping is specified in the file options within the style directory in use. You can also specify it on
the command line, for example:

```
--levels=0:24,1:22,2:
```

```
Designing the map
```
This means that the map will have three levels. Level 0 in the map will correspond to resolution 24 (the
most detailed), level 1 will show at resolution 22 (between scales of 500m and 200m) and so on. The
lowest level needs to include at least an object, therefore the default lowest level of 16 will create a
broken map, if your osm input file has no information at zoom level 16 or lower included. Up to 8 levels
are allowed.

#### 2.1.3. Overview Level...............................................................................................................

The next is overview-level. The meaning is the same as in level, but it is used for the creation of the
overview map. The overview map is used in PC programs like Basecamp or Mapsource, it improves the
drawing speed when looking at the whole map.

The GARMIN map contains only one overview map, so it should not contain too many details, else it
will reach size limits.

This mapping is specified in the file options within the style directory in use. You can also specify it on
the command line, for example:

```
--overview-levels=3:18,4:16,5:
```
It is recommended to continue the numbers of the levels. Again, up to 8 levels are allowed.


Chapter 3. The structure of a style

A style consists of a number of files in a single directory. The best way is to start out with an existing
style that is close to what you want and then work from there.

A style can be packed into a single file using the standard zip utilities that are available on every
operating system, or it can be written as one large text file using the single file style format. These
alternatives are explained in making a style package.

### 3.1. Files.............................................................................................................................................

These files are read in the order that they are listed here. In general, files that are read first take priority
over files read later. The only one of these files that is actually required is the version file, as that is
used to recognise the style. At least one of the points, lines or polygons files must be present or else
the resulting maps will be empty.

#### 3.1.1. Top level folder...............................................................................................................

Choose a short name for your style, it should be one word or a couple of words joined by an underscore
or hyphen. This is how people will refer to the style when it is finished. Create a directory or folder with
that name. Then you must create one or more files in this directory as detailed below. Only the version
file is required.

### 3.2. The version file..........................................................................................................................

This file must exist as it is used to recognise a valid style. It contains the version number of the style
language itself, (not the version number of your style, which you can specify in the info file if you so
wish). The current version number of the style language is 1. Make sure that there is a new line after the
number, place an empty line afterwards to be sure.

### 3.3. The info file................................................................................................................................

This file contains information about your style. It is all optional information, and there is only really any
point adding this information if you are going to distribute your style, or you have more than one style
that you maintain.

The file consists of key=value pairs in the same syntax as the command line option file. To summarise
you can use either an equal sign = or a colon : to separate the key from the value. You can also surround
the value with curly braces { } and this allows you to write the value over several lines.

```
version The version number of your style.
summary A short description of your style in one line.
description A longer description of your style.
base-style Do not use anymore. This was used to base a style on another one. However, it is
bug prone and behaves in a way that is not intuitive without a good understanding of
how things work. The preferred way to do this is to use the include mechanism. This
command will be removed altogether at some point in the future.
```
### Example 3.1. An example info file

Here is an example based on the info file from the default style. You can see it uses both equal and
colon as separators, normally you would just pick one and use it consistently, but it doesn’t make any


```
The structure of a style
```
difference which one you use. The description is written over several lines surrounded in curly braces.
Lines beginning with a hash symbol # are comments and are ignored.

```
#
# This file contains information about the style.
#
```
```
summary: The default style
```
```
version=1.
```
```
description {
The default style. This is a heavyweight style that is
designed for use when mapping and especially in lightly covered
areas.
}
```
### 3.4. The options file..........................................................................................................................

This file contains a number of options that should be set for this style as if they were set on the command
line. Only command line options that affect the style will have any effect. The current list is levels,
overview-levels, and extra-used-tags.

It is advisable to set up the levels that you want, as the default is not suitable for all kinds of maps and
may change in the future. Ideally, you should set the same levels as are used in your style files. For
example, if your style files use levels 12,16,20,22,23,24 then it’s a good idea to make sure your options
style file declares these levels explicitly.

### Example 3.2. An example options file

```
levels = 0:24, 1:22, 2:20, 3:
overview-levels = 4:17, 5:16, 6:15, 7:14, 8:
extra-used-tags=
```
#### 3.4.1. Non command line options.............................................................................................

Most of the options are the same as the command line option of the same name and so you should see its
description in the option help. There are however some options that can only be set in this file (just the
currently).

extra-used-tags

```
A list of tags used by the style. You do not normally need to set this, as mkgmap can work out which
tags are used by a style automatically in most cases. It exists only to work around cases where this
doesn’t work properly.
```
### 3.5. The points file............................................................................................................................

This files contains a set of rules for converting OSM nodes to Garmin POIs (restaurants, bars, ATMs
etc). It can also contain rules for some kind of OSM nodes that may affect routing behavior, for example
barriers, traffic_calming, traffic_signals, etc.

If this file is not present or empty then there will be no POI’s in the final map.

The syntax of the file is described in the style rules section. Like all other files, a hash symbol #
introduces a comment.


```
The structure of a style
```
### 3.6. The lines file...............................................................................................................................

This file contains a set of rules for converting OSM ways to Garmin lines (roads, rivers, barriers, etc).
The syntax of the file is described in the style rules section.

### 3.7. The polygons file........................................................................................................................

This file contains a set of rules for converting polygons to Garmin areas (fields, buildings, residential
areas, etc). The syntax of the file is described in the style rules section.

### 3.8. The relations file........................................................................................................................

This file contains a set of rules to convert OSM relations. Unlike the points, lines and polygons files
this file does not lead directly to a Garmin object. Instead it is used to modify the ways or nodes that are
contained in the relation.

So for example, if the relation represents a route, then you might add one or more tags to all the ways
that make up the route so that they can be processed in the lines file specially.

The syntax of the file is also described in the style rules section, but the rules can only have an action
part, they must not have a type description part.


Chapter 4. Style rules

Rules allow you to take a map feature in the OSM format, which uses a set of tags to describe the feature
into the format required by Garmin maps, where features are identified by a number.

The rules for converting points, lines and polygons are held in correspondingly named files, as described
in the structure of a style.

Each file contains a number of rules. Rules test the values of the tags of an OSM node, way or relation.
They also select a specific Garmin type based on the result of those tests and set mkgmap internal tags
(mkgmap:*) to assign specific attributes to a map element.

### 4.1. Introduction.................................................................................................................................

Each rule starts off with an expression to test the value of one or more tags.

A rule is made up of two or three parts. The three possible parts are:

- The first part is required: this is a set of tests that are performed on the tags of the item to be
    converted.
- The second part is the action block that can be used to do things with the tags of objects that match the
    tests and is contained in curly braces {...}.
- The third part is the element type definition and sets the Garmin type and sometimes other parameters
    that will be used if the tests match. This part is contained in square brackets [...].

If you want to add two or more different map elements you can do this with repeated square brackets
following one expression [...]

Here is an example of a rule containing all three sections:

```
natural=cliff { name '${name} cliff' | 'cliff' } [0x10501 resolution 22]
```
- The tests section is natural=cliff
- The action block is { name '${name} cliff' | 'cliff' }
- The element type definition is [0x10501 resolution 22]

As a general point, space and newlines don’t matter. There is no need to have rules all on the same line,
and you can spread them out over several lines and add extra spaces wherever you like if it helps to
make them easier to read.

Example with lots of extra space and newlines.

```
natural=cliff
{
name '${name} cliff'
| 'cliff'
}
```
```
[
0x
resolution 22
]
```

```
Style rules
```
Example with all unneeded spaces removed.

```
natural=cliff{name'${name} cliff'|"cliff"}[0x10501 resolution 22]
```
#### 4.1.1. Tag and text values.........................................................................................................

Tag names and vales are often single words consisting of letters and perhaps digits. If however a value
(or tag, although that is less common) contains a space or punctuation character then the whole value
must be enclosed in quotation marks. You can use either single quotes (') or double quotes (").

If your text contains a quote then you must use the other kind of quote around the value.

```
highway=primary
"highway"="primary" # quotes not needed, but do no harm
name='Main Street' # quotes needed to keep 'Main Street' as one thing
name="Ten O'Clock Tavern" # Double quotes used because text contains single quotes
```
### 4.2. Tag tests......................................................................................................................................

The most common test is that a particular OSM tag has a given value. So for example if we have

```
highway=motorway
```
This means that we look up the highway tag in the OSM input file and if it exists and has the value
motorway then this test has matched.

You can also compare numeric quantities:

```
population > 10000
lanes >= 2
population < 10000000
```
Respectively, these mean: a population greater than ten thousand, a road with at least two lanes and a
population less than one million.

You may also use regular expressions:

```
ele ~ '\d*00'
```
This checks whether ele is a multiple of 100.

#### 4.2.1. Allowed operations..........................................................................................................

The following table describes the operations that may be used.

### Table 4.1. Full list of operations

```
Operation description and examples
tag=value This matches when a tag has the given value.
tag!=value This is true when the tag does not have the given value, or the tag
is not present at all.
tag=* Matches when the tag exists, regardless of its value.
tag!=* Matches when the tag does not exist.
tag < value Matches when the tag when converted as a number is less than
the given value. If the value is not numeric then this is always
```

```
Style rules
```
```
Operation description and examples
false. This is also the case if value contains a unit. Conversion
for the maxspeed tag can be done with the maxspeedkmh() and
maxspeedmph() function (see Functions).
tag <= value,
tag > value, tag
>= value
```
```
As above, for less than or equal, greater than and greater than or
equal.
```
```
tag ~ REGEX This is true when the value of the tag matches the given regular
expression. The Java regular expression [http://docs.oracle.com/
javase/7/docs/api/java/util/regex/Pattern.html] syntax is
recognised. For example name ~ '.*[Ll]ane' would match
every name that ended in Lane or lane.
! (expr) The not operator (!) reverses the truth of the expression following.
That expression must be in parentheses.
```
#### 4.2.2. Combining tag tests.........................................................................................................

Although it is possible to convert many OSM nodes and ways just using one tag, it is also often
necessary to use more than one.

For example, say you want to take roads that are tagged both as highway=unclassified and lanes>
differently to roads that are just highway=unclassified. In this type of case, you might create two
separate rules as follows:

```
highway=unclassified & lanes>2 [0x06]
highway=unclassified [0x05]
```
This means that roads that are unclassified and have more than two lanes would use Garmin element
type 0x06, whereas unclassified roads without a lanes tag, or where it is less or equal than 2 would use
type 0x05.

It is important to note that the order of the rules is important here. The rules are matched in the order that
they occur in the style file and mkgmap stops trying to apply them after the first one that matches. If you
had the rules above in the reverse order, then the highway=unclassified rule would match first to any
OSM way with that tag/key pair, and the second rule would never get applied. Therefore, in general you
want the most specific rules first and simpler, more general rules later on to catch the cases that are not
caught by the more complex rules.

You can also combine alternatives into the one rule using a logical or, represented with a pipe (|) symbol.
For example

```
highway=footway | highway=path [0x07]
```
This means if the road has either the highway=footway tag or the highway=path tags (or both), then
the condition matches and mkgmap would use type 0x07 for the map. This works exactly the same as if
you had written two separate rules - one for footway and one for path - and indeed is converted to two
separate rules internally when mkgmap runs.

You are not limited to two tests for a given rule... you can combine and group tests in almost whatever
way you like. So for a slightly forced example the following would be possible:

```
place=town & (population > 1000000 | capital=true) | place=city
```

```
Style rules
```
This would match if there was a place tag which had the value town and either the population was over
a million or it was tagged a capital, or there was a place tag with the value city.

```
There used to be some restrictions on the kind of expression you could use. Now the only
restriction is you must have at least one test that depends on a tag existing. So you cannot
match on everything, regardless of tags, or test for an object that does not have a tag.
```
#### 4.2.3. Comparing the values of two tags................................................................................

Sometimes you may want to compare the values of two tags, rather than the value of one tag with a fixed
value. Use a dollar sign to indicate that you want the tag value.

```
# If you had the following tags:
# name=Fford-y-Mor
# name:en=Terrace Road
# name:cy=Fford-y-Mor
```
```
name = $name:cy { } # this would match
name = $name:en { } # and this would not
```
This tests if the value of the name tag is the same as the welsh name tag (name:cy)

It is worth noting that the normal case

```
highway=primary
```
is exactly the same as

```
$highway=primary
```
#### 4.2.4. Functions........................................................................................................................

Functions calculate a specific property of an OSM element.

### Table 4.2. Style functions

```
Function NodeWayRel. Description
length() x x Calculates the length in m. For relations its the sum of all
member length (including sub relations).
area_size() x Calculates area size in (garmin units)^2. A non closed
way has an area_size() of 0. In case a polygon is an outer
part of a multipolygon the whole area size of all outer
multipolygon parts is returned.
The size of one (garmin unit)^2 in m^2 varies depending on
the latitude. Sample values:
5.71 m^2 at latitude 0°
4.03 m^2 at (+-)45°
2.85 m^2 at (+-)60°
0.5 m^2 at (+-)85°
is_complete() x true if all nodes of a way are contained in the tile. false if
some nodes of the way are missing in the tile.
```

```
Style rules
```
```
Function NodeWayRel. Description
is_closed() x true the way is closed (start and end point are the same).
false the way is not closed and cannot be processed as
polygon.
maxspeedkmh() x Retrieves the value of the maxspeed tag converted to km/h.
maxspeedmph() x Retrieves the value of the maxspeed tag converted to mph.
type() x x x Retrieves the type of the OSM element: node, way,
relation.
osmid() x x x Retrieves the id of the OSM element. This can be useful for
style debugging purposes. Note that due to internal changes
like merging, cutting etc. some element ids are changed and
some have a faked id > 4611686018427387904.
is_in(tag,value,method) x x true if the element is in polygon(s) having the specified
tag=value according to the method, false otherwise.
value can be '*' which matches any polgon having tag. The
methods available depend on the Style section:
polygons: all - all of the closed way is within the
polygon(s). any - some is within.
points: in - the node is within a polygon. in_or_on - it is
within or on the edge. on - it is on the edge.
lines: all - part of the way is within the polygon(s), none
is outside; it might touch an edge. all_in_or_on - none is
outside. on - it runs along the edge. any - part is within.
none - part is outside, none is inside.
A common case is a line outside the polygon that runs
to the edge, joining a line that is inside. The method to
match an outside line (none) allows part to be on the
edge, likewise, the method to match an inside line (all)
allows part to be on the edge. Compared to all, the method
all_in_or_on additionally matches lines which are only on
the edge of the polygon.
is_drive_on_left() x true the element is in a drive_on_left country. false
the element is not a drive_on_left country or the
information given in the tags mkgmap:admin_level
and mkgmap:country could not be used to retrieve the
information.
```
The following rule matches for all service ways longer than 50m.

```
highway=service & length()>
```
### 4.3. Action block.............................................................................................................................

An action block is enclosed in braces { ... } and contains one or more statements that can alter the
element being displayed; multiple statements are separated by ‘;’ symbol. When there is an action block,
the element type definition is optional, but if used it must come after the action block.


```
Style rules
```
A list of all the command that can be used in the action block follows. In the examples you will see
notation of the form ${name}, this is how tag values can be substituted into strings, in a similar way to
many computer languages. For full details see the section on variable substitution.

#### 4.3.1. add..................................................................................................................................

The add command adds a tag if it does not already exist. This is often used if you want to set the value of
a tag as a default but do not want to overwrite any existing tag.

For example, motorways are one way by default so we need to add the oneway=yes tag in the style so
that is treated as one way by the device. But there are some stretches of motorway that are one-way and
these will be tagged as oneway=no. If we used set then that tagging would be lost, so we use add.

```
highway=motorway { add oneway=yes }
```
The other use is in in relations with the apply command.

All the same you can set any tag you want, it might be useful so you can match on it elsewhere in the
rules.

You can also use substitutions.

```
{add name='${ele}'; add name='${ref}';}
```
These two commands would set the name tag to the value of the ele tag if it exists, or to the value of the
ref tag if that exists.

You can also give a list of alternative expressions separated with a vertical bar in the same way as on the
name command. The first one that is fully defined will be used.

```
{add key123 = '${name:en}' | '${name}'; }
```
If key123 is not set it will set key123 to the value of the name:en tag if it exists and to the name tag if
not.

#### 4.3.2. set...................................................................................................................................

The set command is just like the add command, except that it sets the tag, replacing any existing value it
had.

#### 4.3.3. delete..............................................................................................................................

The delete command deletes a tag.

```
{ delete key123 }
```
#### 4.3.4. deletealltags....................................................................................................................

The deletealltags command deletes all tags. Usually this stops all further processing of the element.

```
{ deletealltags }
```
#### 4.3.5. addlabel..........................................................................................................................

Each item in the Garmin map can have up to four labels. Usually only the first label is displayed. On
some Garmin units the second label is used for routing instructions. The third and fourth label are known
to be used for address search only. The four labels can be assigned by setting the tags mkgmap:label:n
where n is a number between 1 and 4.


```
Style rules
```
The addlabel command assigns the first empty mkgmap:label:n tag with the given value.

```
{addlabel '${name} (${ref})' | '${ref}' | '${name}'}
```
If both the name and ref tags are are set, then the first alternative would be completed and the resulting
label might be Main St (A1). If just name was set, then the first two alternatives can not be fully and so
the final label might in that case be Main St.

Highway shields can be used in the first label only. You can use the notation ${tagname|highway-
symbol:box}. Valid symbols are interstate, shield, round, hbox, box and oval. The appropriate
kind of highway shield will be added to the value of tagname. The exact result of the way it looks is
dependent on where you view the map.

#### 4.3.6. name...............................................................................................................................

This sets the first label of the element but only if it is not already set. This is a helper action. The same
effect can be produced with different notations as it is shown in the following example where all three
lines have the same effect.

```
{name '${name} (${ref})' | '${ref}' | '${name}'}
{add mkgmap:label:1='${name} (${ref})' | '${ref}' | '${name}'}
mkgmap:label:1!=* {set mkgmap:label:1='${name} (${ref})' | '${ref}' | '${name}'}
```
#### 4.3.7. addaccess........................................................................................................................

The "addaccess" action sets all unset mkgmap access restriction tags to the given value. This is a helper
action to avoid long action blocks.

```
{ addaccess 'no' }
```
is the same as

```
{
add mkgmap:foot=no;
add mkgmap:bicycle=no;
add mkgmap:car=no;
add mkgmap:taxi=no;
add mkgmap:truck=no;
add mkgmap:bus=no;
add mkgmap:emergency=no;
add mkgmap:delivery=no
}
```
#### 4.3.8. setaccess.........................................................................................................................

The "setaccess" action sets all mkgmap access restriction tags to the given value no matter if they
already have a value or not. This is a helper action to avoid long action blocks.

```
{ setaccess 'no' }
```
is the same as

```
{
set mkgmap:foot=no;
set mkgmap:bicycle=no;
set mkgmap:car=no;
```

```
Style rules
```
```
set mkgmap:taxi=no;
set mkgmap:truck=no;
set mkgmap:bus=no;
set mkgmap:emergency=no;
set mkgmap:delivery=no
}
```
#### 4.3.9. apply...............................................................................................................................

The "apply" action only makes sense in relations. Say you have a relation marking a bus route, but none
of the ways that are in the relation have any special tags to indicate that they form part of that bus route,
and you want to be able to tell from looking at the map which buses go where. You can write a rule in
the relations file such as:

```
type=route & route=bus {
apply {
set route=bus;
set route_ref='${route_ref}';
}
}
```
Then in the lines file you will need to write a rule to match route=bus. All the relation rules are run
before any others so that this works.

The substitution ${route_ref} takes the value of the tag on the relation and applies it to each of the
ways in the relation.

The substitution $(route_ref) (with parenthesis, rather than curly braces) can be used for accessing the
value of the tag on the actually processed member of the relation, e.g.

```
type=route & route=bus {
apply {
set route=bus;
set name='$(name) ${route_ref}';
}
}
```
The "apply" action can be limited to members with a special role by adding role=rolevalue after the
apply keyword.

```
type=route & route=bus {
apply role=forward {
set route=bus;
set name='$(name) ${route_ref}';
}
}
```
#### 4.3.10. apply_once...................................................................................................................

The apply_once action is like apply, but it will apply the action once per relation member. A round-trip
route relation may include the same ways multiple times, unless all member ways have been defined as
parallel one way streets.

#### 4.3.11. apply_first....................................................................................................................

The apply_first action is like apply, but it will apply the action only to the first relation member as
appearing in the input file. In combination with the --add-pois-to-lines option this might be used with


```
Style rules
```
route relations to mark the beginning of a route, presuming that the relation is complete and ordered so
that the first member is the start of the route.

#### 4.3.12. echo..............................................................................................................................

The echo action prints the element id plus a text to stderr or to where directed by a logging configuration
file. This can be used for quality checks and debugging purposes. When using a logging configuration
file, the messages are logged with custom level ECHO (1200).

```
highway=motorway_link & oneway!=* { echo "motorway_link without oneway tag" }
```
#### 4.3.13. echotags........................................................................................................................

The echotags action prints the element id, all tags and values plus a text to stderr or to where directed
by a logging configuration file. This can be used for style debugging purposes. When using a logging
configuration file, the messages are logged with custom level ECHO (1200).

```
highway=living_street { echotags "This is a living_street" }
```
### 4.4. Variables...................................................................................................................................

You can substitute the value of tags within strings in an action. A dollar sign ($) introduces the
substitution followed by the tag name surrounded by curly braces like so ${name}.

The most obvious use for variables is in setting the name of the element. You are able to use any
combination of tags to make the name from. Here we name a fuel station by its brand and the operator in
parentheses following.

```
amenity=fuel { name '${brand} (${operator})' } [ 0x2f01 ]
```
If the operator tag was not set, then the name would not be set because all substitutions in a string must
exist for the result to be valid. This is why the "name" command takes a list of possibilities, if operator
was simply replaced with a blank, then you would have an empty pair of parentheses. So you would fix
the previous rule by adding another name option.

```
amenity=fuel
{ name '${brand} (${operator})' | '${brand}' }
[ 0x2f01 ]
```
If only the brand tag exists, then the first option will be skipped and the second will be used.

#### 4.4.1. Variable filters...............................................................................................................

The value of a variable can be modified by filters. The value of the tag can be transformed in various
ways before being substituted.

A filter is added by adding a vertical bar symbol "|" after the tag name, followed by the filter name, then
a colon ":" and an argument. If there is more than one argument required then they are usually separated
by colons too, but that is not a rule.

${tagname|filter:"arg1:arg2"}

You can apply as many filter expressions to a substitution as you like.

${tagname|filter1:"f1Args"|filter2:"f2Args"}


```
Style rules
```
For backward compatibility, most argument strings do not actually need to be quoted, however we
would recommend that you do for clarity. If you need a pipe symbol or a closing curly backet, then you
must use quotes.

### Table 4.3. List of all substitution filters

```
Name Arguments Description
def default If the variable is not set, then use the argument as a default value.
This means that the variable will never be ‘unset’ in places where
that matters.
${oneway|def:"no"}
conv m=>ft Use for conversions between units. With the argument m\=\>ft the
value is converted into feet, with the value being assumed to be in
meters, unless the value includes a unit already. If any of the units
are not recognised then the value is unchanged.
${height|conv:"m=>ft"}
So if height is 10, then the result is 33, and if height is 10ft, then
the result is 10, as it is already in feet.
The possible units are:
```
- Length: m, km, ft (feet), feet, mi (miles).
- Speed: mph, km/h (or kmh, kmph), knots
- Weight: t, kg, lb (or lbs)
subst from=>to
from~>to

```
Substitutes all occurrences of the string from with the string to in
the tag value. The => operator can be used for an exact matches
while ~> accepts regular expressions in the from attribute.
to can be empty to remove the from string altogether.
Example, if name ="Queen Street"
${name|subst:"Queen=>"} returns " Street"
${name|subst:"Queen=>King"} returns "King Street"
${name|subst:".*\s~>"} returns "Street"
part separator
operator
partnumber
```
```
Split a value in parts and returns one or more part(s) of it. If
partnumber is negative, the part returned is counted from the end of
the split
If not specified, the default separator is ; and the first part is returned
(i.e. ${name|part:""}=${name|part:";:1"}).
If the operator is : the part specified by partnumber is returned.
If the operator is < or > the correspondent number of parts before or
after the partnumber are returned
Example: if the value is "Aa#Bb#Cc#Dd#Ee"
${name|part:"#:1"} returns Aa
```

```
Style rules
```
Name Arguments Description

```
${name|part:"#:-1"} returns Ee
${name|part:"#:2"} returns Bb
${name|part:"#:-2"} returns Dd
${name|part:"#>1"} returns Bb#Cc#Dd#Ee#
${name|part:"#<5"} returns Aa#Bb#Cc#Dd#
${name|part:"#<-1"} returns Aa#Bb#Cc#Dd#
This can be especially useful for tags like ref, exit_to and destination
or to switch words, example if value is "word1 word2 ... wordN-1
wordN"
${name|part:" :-1"}, ${name|part:" <-1"} returns "wordN,
word1 word2 ... wordN-1 "
```
highway-
symbol

```
symbol:max-
num:max-alpha
```
```
Prepares the value as a highway reference such as "A21" "I-80" and
so on. A code is added to the front of the string so that a highway
shield is displayed, any ";" are replaced by "/" and spaces are
removed.
${ref|highway-symbol:"box:4:8"}
See below for a list of the highway-symbol values.
The first number is the maximum number of characters to allow
for references that contain numbers and letters. The second is the
maximum length of references that do not contain numbers. If there
is just the one number then it is used in both cases. If no numbers are
given, the default value 8 is used.
If the reference, after spaces have been removed, is longer than
the maximum length then the filter passes the string onwards
unchanged; the highway-symbol is not prepended.
```
height m=>ft This is exactly the same as the conv filter, except that it prepends
a special separation character before the value which is intended
for elevations so that the Garmin software can convert it to the unit
configured by the user. If no argument is given the default is m=>ft,
else the target unit must be ft (foot).
${ele|height:"m=>ft"}

country-ISO Use to normalize country names to the 3 character ISO 1366 code.
The filter has no arguments. It uses the list in LocatorConfig.xml.
Possible inputs are country names, or ISO codes in 2 or 3 characters,
for example "Deutschland", "Germany", "Bundesrepublik
Deutschland", or "DE" will all return "DEU", also different cases
like "GERMANY" or " germany " will work.
If the value is not found in the list, then the value is unchanged.

not-equal tag Used to check for duplicate tags. If the value of this tag is equal to
the value of the tag named as the argument to not-equal, then value
of this tag is set to undefined.


```
Style rules
```
```
Name Arguments Description
place=* {
name '${name} (${int_name|not-equal:"name"})'
| '${name}'
}
```
```
In that example, if the international name is different to the name
then it will be placed in parenthesis after the name. Otherwise there
will just be the name as given in the "name" tag.
substring start:end Extract part of the string. The start and end positions are counted
starting from zero and the end position is not included.
${name|substring:"2:5"} If the "name" was "Dorset Lane", then
the result is "rse". If there is just the one number, then the substring
starts from that character until the end of the string.
not-contained separator:tag Used to check for duplicate values. If the value of this tag is
contained in the list being the value of the tag named as the
argument to not-contained, then value of this tag is set to
undefined.
```
```
type=route & route=bus & ref=* {
apply {
set route_ref=
'$(route_ref),${ref|not-contained:",:route_ref"}'
| '$(route_ref)' | '${ref}';
}
}
```
```
Here, ref value is only added to route_ref when it is not already
contained in that list (with separator ,). Otherwise, the value of
route_ref is unchanged. This helps to get correct labeling (no
duplicates) for public transport lines where there can be multiple
relations with the same ref attribute (e.g. one for the forward and
one for the backward direction).
For example, if route_ref was already "1,2,150" and ref would
again be "150", this value would not be added to the list as it is
already there. In contrast, ref equal to "229" would be added, so
after that route_ref would have the value "1,2,150,229"
```
#### 4.4.2. Symbol codes.................................................................................................................

Here is a list of all the symbols that can be created with images to give an idea of where they should be
used. The actual symbol will depend on the device that it is displayed on.

### Table 4.4. Highway symbol codes

```
Shield name Symbol Description
interstate US Interstate, digits only
```
```
shield US Highway shield, digits
only
```

```
Style rules
```
```
Shield name Symbol Description
round US Highway round, digits
only
hbox Box for major roads
```
```
box Box for medium roads
```
```
oval Box for smaller roads
```
### 4.5. mkgmap internal tags...............................................................................................................

There are lots of tags prefixed with mkgmap:. Some of them need to be set in the style file to set specific
attributes of the Garmin map elements, e.g. access restrictions, labels, attributes required for address
search etc. Others are added to the OSM elements by mkgmap so that they can be evaluted in the style
files to change the processing.

#### 4.5.1. Tags evaluated by mkgmap...........................................................................................

These tags need to be set within the style file to set specific attributes of the Garmin map elements.

```
highway=* & (bicycle=no | bicycle=private) { set mkgmap:bicycle='no' }
```
This rule defines that the road cannot be used by bicycles.

### Table 4.5. Tags for routable roads

```
Attribute mkgmap tag Example Notes
Labels mkgmap:label:1
mkgmap:label:2
mkgmap:label:3
mkgmap:label:4
```
```
Eastern
Avenue
A112
```
```
Usually only the first label is
displayed. On some units the
second label of roads is displayed
as routing instruction. All labels are
used for address search.
Country mkgmap:country GBR Three letter ISO code, e.g. for GBR
United Kingdom
Region mkgmap:region London
Borough of
Waltham
Forest
```
```
The regions name. Useful if there
are multiple cities with the same
name.
```
```
City mkgmap:city London
Street mkgmap:street High Road
Leyton
```
```
This value is used by house number
search to match the addr:street
tag of an OSM element with house
number to the corresponding road.
It must be set so that house number
search is working.
Zipcode mkgmap:postal_code E10 5NA
```

```
Style rules
```
Attribute mkgmap tag Example Notes

Access restrictions mkgmap:foot
mkgmap:bicycle
mkgmap:car
mkgmap:taxi
mkgmap:truck
mkgmap:bus
mkgmap:emergency
mkgmap:delivery

```
no These tags are evaluated for
routable lines (roads) only. By
default access for a specific vehicle
type is allowed. Only in case the
value of the tag is no access is
blocked for the given type.
```
Throughroute mkgmap:throughroute no If this tag is set to no routing is
allowed on this road only if the
start or end point lies on the road.

Carpool lane mkgmap:carpool yes If this tag is set to yes the road is
marked to have a carpool lane. This
does not seem to work on all units.

Toll road mkgmap:toll yes If this tag is set to yes the road
can be used only when paying a
specific toll.

Unpaved mkgmap:unpaved yes If this tag is set to yes the road is
marked to be unpaved. Some units
can avoid unpaved roads.

Ferry mkgmap:ferry yes If this tag is set to yes the line is
marked to be a ferry line. Some
units can avoid ferry lines.

Road speed mkgmap:road-speed-class 2 A value between 0 and 7. Overrides
the road_speed definition in the
element type definition if this tag is
set.

Road speed
modifier

```
mkgmap:road-speed +1 Modifies the road speed class by
the given value. In case the value is
prefixed with + or - the road speed
class is modified. In case the value
does not start with + or - the road
speed class value of the element
type definition is overriden.
```
Road speed limiters mkgmap:road-speed-min
mkgmap:road-speed-max

```
5 Defines the minimum/maximum
road speed class. This can be used
to limit the modification of the road
speed class (mkgmap:road-speed).
```
Road class mkgmap:road-class -1 Modifies the road class defined in
the element type definition. In case
the value is prefixed with + or - the
road class is modified. In case the
value does not start with + or - the


```
Style rules
```
```
Attribute mkgmap tag Example Notes
road class value of the element type
definition is overriden.
Road class limiters mkgmap:road-class-min
mkgmap:road-class-max
```
```
2 Defines the minimum/maximum
road class. This can be used to limit
the modification of the road class
(mkgmap:road-class).
```
### Table 4.6. Tags that control the treatment of roads

```
Tag Description Required mkgmap
option
mkgmap:way-has-pois true for ways that have at least
one point with a tag access=*,
barrier=*, or highway=*
```
```
link-pois-to-ways
```
```
mkgmap:dead-end-check Set to false to disable the dead
end check for a specific way
```
```
report-dead-ends
```
```
mkgmap:flare-check Set to true to force the flare check
for a specific way, set to false to
disable it
```
```
check-roundabout-flares
```
```
mkgmap:dir-check Set to false to tell mkgmap to
ignore the way when checking
roundabouts for direction
```
```
check-roundabouts
```
```
mkgmap:no-dir-check Set to true to tell mkgmap to
ignore the way when checking
roundabouts for direction
```
```
check-roundabouts
```
```
mkgmap:synthesised Set to true to tell mkgmap that
this is an additional way created
using the continue statement in an
action block and that it should be
excluded from checks
```
```
check-roundabouts,
check-roundabout-flares
```
```
mkgmap:set_unconnected_type Set to none to remove unconected
roads from the map once that all
roads are known, or to a valid line
type if you want a normal line
instead of a road. Works also with
overlay lines for the same way.
mkgmap:set_semi_connected_type Like
mkgmap:set_unconnected_type,
but matches for roads with exactly
one connection to other roads
```
### Table 4.7. POI address tags

```
Attribute mkgmap tag Example Notes
Name mkgmap:label:1 Pizza Express Names of the POI
```

```
Style rules
```
```
Attribute mkgmap tag Example Notes
mkgmap:label:2
mkgmap:label:3
mkgmap:label:4
Country mkgmap:country GBR Three letter ISO code,
e.g. for GBR United
Kingdom
Region mkgmap:region Nottinghamshire The regions name.
Useful if there are
multiple cities with the
same name.
City mkgmap:city Nottingham
Street mkgmap:street King Street
Housenumber mkgmap:housenumber 20
Zipcode mkgmap:postal_code NG1 2AS
Phone mkgmap:phone +44 115 999999 Phone number in any
format
```
```
Wikipedia [http://en.wikipedia.org/wiki/ISO_3166-1_alpha-3] has a list of all ISO 3166-1
alpha 3 codes
```
#### 4.5.2. Tags added by mkgmap................................................................................................

Some tags are added by mkgmap to indicate some property calculated by mkgmap.

```
mkgmap:admin_level2=* { add mkgmap:country='${mkgmap:admin_level2}' }
```
The tag mkgmap:admin_level2 is added to each OSM element if the bounds option is set. In the rule
above it is used to assign the country location.

### Table 4.8. Tags added by mkgmap

```
Tag Description Required mkgmap option
mkgmap:admin_level2 Name of the
boundary=administrative
relation/polygon with
admin_level=2 the element is
located in
```
```
bounds
```
```
mkgmap:admin_level3 Name of the
boundary=administrative
relation/polygon with
admin_level=3 the element is
located in
```
```
bounds
```
```
mkgmap:admin_level4 Name of the
boundary=administrative
relation/polygon with
```
```
bounds
```

```
Style rules
```
Tag Description Required mkgmap option

```
admin_level=4 the element is
located in
```
mkgmap:admin_level5 Name of the
boundary=administrative
relation/polygon with
admin_level=5 the element is
located in

```
bounds
```
mkgmap:admin_level6 Name of the
boundary=administrative
relation/polygon with
admin_level=6 the element is
located in

```
bounds
```
mkgmap:admin_level7 Name of the
boundary=administrative
relation/polygon with
admin_level=7 the element is
located in

```
bounds
```
mkgmap:admin_level8 Name of the
boundary=administrative
relation/polygon with
admin_level=8 the element is
located in

```
bounds
```
mkgmap:admin_level9 Name of the
boundary=administrative
relation/polygon with
admin_level=9 the element is
located in

```
bounds
```
mkgmap:admin_level10 Name of the
boundary=administrative
relation/polygon with
admin_level=10 the element is
located in

```
bounds
```
mkgmap:admin_level11 Name of the
boundary=administrative
relation/polygon with
admin_level=11 the element is
located in

```
bounds
```
mkgmap:postcode Name of the postal code relation/
polygon the element is located in

```
bounds
```
mkgmap:residential Name of the residential relation/
polygon the element is located in
or yes if unnamed

```
none
```
mkgmap:area2poi The value is true if the POI is
derived from a polygon

```
add-pois-to-areas
```

```
Style rules
```
```
Tag Description Required mkgmap option
mkgmap:line2poi The value is true if the POI is
derived from a line
```
```
add-pois-to-lines
```
```
mkgmap:line2poitype The tag is set for each POI
generated from a line. Possible
values are: start, end, mid,
inner.
```
```
add-pois-to-lines
```
```
mkgmap:from-node:attname The attribute is set for each POI
generated from a line. These are
the original attributes of the node
(part of the line) from which the
point was generated
```
```
add-pois-to-lines
```
```
mkgmap:way-length The tag is set for each POI
generated from a line. It gives the
way length rounded to meters.
```
```
add-pois-to-lines
```
```
mkgmap:exit_hint true for the part on link roads
that should contain information
about the exit
```
```
process-exits
```
```
mkgmap:exit_hint_name The name tag value of the links
exit node
```
```
process-exits
```
```
mkgmap:exit_hint_ref The ref tag value of the links exit
node
```
```
process-exits
```
```
mkgmap:exit_hint_exit_to The exit_to tag value of the
links exit node
```
```
process-exits
```
```
mkgmap:dest_hint The tag is set to a reasonable
destination value for the part on
link roads that should contain
destination information about the
link
```
```
process-destination
```
```
mkgmap:synthesised The value is yes if the way was
added by the make-opposite-
cycleways option
```
```
make-opposite-cycleways
```
```
mkgmap:mp_created The value is true if the way was
created by the internal multi-
polygon-relation handling
```
```
none
```
```
mkgmap:option:<key> Tag generated by the --style-
option option
```
```
style-option
```
### Table 4.9. Other internal tags

```
Tag Description
mkgmap:skipSizeFilter If set to true the line or polygon will pass the size
filter, no matter what size it has
```

```
Style rules
```
```
Tag Description
mkgmap:highest-resolution-only If set to true the object will only be added for the
highest resolution configured in the element type
definition.
mkgmap:execute_finalize_rules If set to true mkgmap will execute the finalize
rules even if no object is created fot the element.
mkgmap:numbers If set to false for a node or way mkgmap will
ignore the object in the calculations for the --
housenumber option
mkgmap:drawLevel Set to a number from 1 to 100. Overrides the
polygon area that is used by --order-by-decreasing-
area. 1..50 are larger than typical polygons and be
overwritten by them, 51..100 are smaller and will
show. Higher drawLevels will show over lower
values.
mkgmap:stylefilter Set to either polyline or polygon for ways which
have mkgmap:mp-created=true. Is used to decide
which rules should be used. Should not be set or
modified in the relations style.
```
### 4.6. Element type definition............................................................................................................

As noted above this is contained in square brackets and if used must be the last part of the rule.

The first and only mandatory part of this section is the Garmin type code which must always be written
in hexadecimal. Following this the element type definition rule can contain a number of optional
keywords and values.

#### 4.6.1. level................................................................................................................................

This is the highest zoom level that this element should appear at (like EndLevel in the mp format). The
lower the level the detailed the view. The most detailed, most zoomed in, level is level 0. A map will
usually have between three and five levels. If the level for an object is not given then it defaults to 0 and
so the specified feature will only appear at the most detailed level.

In the following example, we set highways to appear from zoom level 4 down to zoom level 0:

```
highway=motorway [0x01 level 4]
```
```
You can use level to place elements into the layers of the map that you want but you can’t
force the device to actually display them.
```
```
Some pieces of software (such as QLandkarteGT, I believe) will honour your selections,
but actual GPS devices have their own ideas about which POI’s can be shown at which
resolutions.
```
Level ranges. You can also give a range (e.g. 1-3) and the map will then contain the object only
between the specified levels.

```
highway=motorway [0x01 level 3-5]
```

```
Style rules
```
In this example, motorways will appear at zoom level 5, which is most zoomed out, and continue to be
visible until zoom level 3, which is moderately zoomed in, and then will not be shown in zoom levels 2,
1 and 0 (most zoomed-in).

```
Of course you are unlikely to want a feature to disappear as you zoom in, but this can be used
for interesting effects where a different representation takes over at the lower zoom levels.
For example a building may be a point at high levels and then become a polygon at lower
levels.
```
#### 4.6.2. resolution

This is an alternative way of specifying the zoom level at which an object appears. It is specified as a
number from 1-24, which corresponds to one of the zoom levels that Garmin hardware recognises. You
should not use resolution if you have used level as they achieve the same outcome.

In either case, the mapping between level and resolution is given in the options style file, where you will
see something like this:

```
# The levels specification for this style
#
levels = 0:24, 1:23, 2:22, 3:20, 4:18, 5:16
```
This sets level zero equal to resolution 24, level 1 to resolution 23 and so on.

Although the default style uses resolution rather than level it is on the whole much easier to use
level as it is immediately clear where the element will end up. If you use a resolution that is
‘between’ two levels for example it will only show up in the lower one.

Resolution ranges. Just as with levels, you can specify a range of resolutions at which an object
should appear. Here is an example.

```
highway=residential [0x06 resolution 16-22 continue]
highway=residential [0x07 resolution 23-24]
```
This example creates roads of type 0x06 between resolutions 16 and 22, then roads of type 0x07 between
resolutions 23 and 24. This example makes use of the continue statement, which is discussed in more
detail below.

```
Since 24 is the default upper bound for a range, that second range could just have been
written as the single number ‘23’.
```
#### 4.6.3. default_name..................................................................................................................

If the element has not already had a name defined elsewhere in the rule, it will be given the name
specified by default_name. This might be useful for things that usually don’t have names and don’t
have a recognisable separate Garmin symbol. You could give a default name of ‘bus stop’ for example
and all bus stops that didn’t have their own name would now be labelled as such.

```
Be careful to use this sparingly and not overwhelm the map or the search.
```
#### 4.6.4. road_class.......................................................................................................................

Setting this makes the line a "road" and it will be routable and can be part of an address search. It gives
the class of the road where class 4 is used for major roads that connect different parts of the country,


```
Style rules
```
class 3 is used for roads that connect different regions, down to class 0 which is used for residential
streets and other roads that you would only use for local travel.

It is important for routing to work well that most roads have lower classes and there are fewer and
fewer roads in each of the higher classes. Also, the class of connector roads (links, roundabouts, ramps)
matches the class of the highest class of roads being connected.

### Table 4.10. Road classes

```
Class Used as
4 Major HW/Ramp
3 Principal HW
2 Arterial St / Other HW
1 Minor or Service road
0 Residential Street / Unpaved
road / Trail
```
#### 4.6.5. road_speed.....................................................................................................................

This keyword is used along with road_class to indicate that the line is a "road" that can be used for
routing and for address searches. It is an indication of how fast traffic on the road is. 0 is the slowest and
7 the fastest. This is not a speed limit and does not activate the maximum speed symbol on the newer
Garmin car navigation systems. The speed limits that Garmin knows are shown in the following table:

### Table 4.11. Road Speeds

```
road_speed highest speed
7 No speed limit
6 70 mph / 110 kmh
5 60 mph / 90 kmh
4 50 mph / 80 kmh
3 35 mph / 60 kmh
2 25 mph / 40 kmh
1 15 mph / 20 kmh
0 3 mph / 5 kmh
```
#### 4.6.6. continue..........................................................................................................................

As discussed above, style rules are matched in the order that they occur in the style file. By default, for
any given OSM object mkgmap will try each rule in turn until one rule wth a element type definition
matches; it will then stop trying to match further rules against the current OSM object. If the rule only
has an action block mkgmap will continue to find other matches.

However, if you add a continue statement to the definition block of a rule, mkgmap will not stop
processing the object but will instead carry on trying to match subsequent rules until it either runs out of
rules or finds a matching rule that does not include a continue statement.

This feature is used when you want more than one symbol to result from a single OSM element. This
could be for clever effects created by stacking two lines on top of each other. For example if you want to


```
Style rules
```
mark a bridge in a distinctive way you could match on bridge=yes, you would then almost always use
continue so that the highway tag could be matched later. If you failed to do this then there might be a
break in the road for routing purposes.

Note that when using the continue statement, the action block of the rule (if there is one) will only
be applied within this rule and not during any following rule matches. Use the continue with_actions
statement if you want to change this behaviour (see next section).

#### 4.6.7. continue with_actions....................................................................................................

The with_actions statement modifies the continue behaviour in such a way, that the action block of this
rule is also applied, when this element is checked for additional conversions.

Example of a full element type definition.

```
[0x2 road_class=3 road_speed=5 level 2
default_name 'example street' continue with_actions]
```
### 4.7. Including files...........................................................................................................................

Its often convenient to split a file into smaller parts or to use the same rules in two different files. In
these cases you can include one rule file within another.

```
include "inc/common";
```
Here some common rules have been included in a rule file from a directory called "inc" within the style.
Note that the line ends in a semi-colon which is easy to forget.

```
The included files don’t have to be located within the style and can be anywhere else.
```
When you include a file, the effect is exactly as if you had replaced the include line with the contents
of the file. An include directive can occur anywhere that a rule could start, and it is possible to include
another file from with in the file that is included.

Including from another style. It is also possible to include a file from another style. To do this you
simply add from stylename to the end of the include statement.

```
include "points" from default;
```
That will include the points file from the default style. This might be useful if you want to only change
a few things about the default style.

### 4.8. Finalize section.........................................................................................................................

The points, lines and polygons style files can have a finalize section at the end of the style file. It starts
with the line <finalize>.

The finalize section contains actions only and must not have an element type definition. Its rules are
executed each time an element type definition in the style file matches. The finalize section is often
useful to set the mkgmap internal tags.

### Example 4.1. Finalize section in the lines file with access handling

Two elements tagged with


```
Style rules
```
```
Way 1: highway=motorway, ref=A1
Way 2: highway=service, name=Main Road, access=no, foot=yes, bicycle=yes
```
using the lines file

```
highway=motorway [0x01 road_class=4 road_speed=7 resolution 15]
highway=service [0x07 road_class=0 road_speed=1 resolution 24]
```
```
<finalize>
highway=* { name '${name} (${ref})' | '${name}' | '${ref}' }
highway=motorway { add bicycle=no; add foot=no }
bicycle=* { add mkgmap:bicycle='${bicycle}' }
foot=* { add mkgmap:foot='${foot}' }
access=* { addaccess '${access}' }
```
will result in

```
Way 1: highway=motorway, ref=A1, mkgmap:label:1=A1, mkgmap:foot=no,
mkgmap:bicycle=no
Road 1 in Garmin map: Type 0x01, Name 'A1', no access for bicycle and foot
Way 2: highway=service, name=Main Road, access=no, foot=yes, bicycle=yes,
mkgmap:label:1=Main Road, mkgmap:foot=yes, mkgmap:bicycle=yes,
mkgmap:car=no, mkgmap:truck=no, mkgmap:bus=no, ...
Road 2 in Garmin map: Type 0x07, Name 'Main Road', no access for all vehicle
types except bicycle and foot
```
```
Actions in the finalize section are not persistent in terms of the continue or continue
with_actions statement
```
### 4.9. Style syntax extension if then else...........................................................................................

To avoid the repetition of expressions you can use the following syntax: if (tests) then i-rule(s) end

or

if (tests) then rule(s) else e-rules(s) end

```
Rules within if and end must be written with an expression. The shortest valid expression is
a pair of round brackets ().
```
So, instead of

```
boundary=administrative { name '${mkgmap:boundary_name}' }
boundary=administrative & admin_level<3 [0x1e resolution 12]
boundary=administrative & admin_level<5 [0x1d resolution 19]
boundary=administrative & admin_level<7 [0x1c resolution 21]
boundary=administrative & admin_level<9 [0x1c resolution 22]
boundary=administrative [0x1c resolution 22]
```
you may write

```
if (boundary=administrative) then
() { name '${mkgmap:boundary_name}' }
admin_level<3 [0x1e resolution 12]
admin_level<5 [0x1d resolution 19]
admin_level<7 [0x1c resolution 21]
```

```
Style rules
```
```
admin_level<9 [0x1c resolution 22]
() [0x1c resolution 22]
end
```
If statements may also be nested and you can also use them in combination with the include statement.

```
if (mkgmap:option:routing=car) then
include "inc/car-rules";
end
if (mkgmap:option:routing=bicycle) then
include "inc/cycle-rules";
end
```
### 4.10. Troubleshooting......................................................................................................................

For each node/way/relation, mkgmap goes through the tags exactly once in order from the top of the file
downward. For each rule that matches, any action block will be run. As soon as a rule that ends with a
type definition is found then processing stops and that is the Garmin symbol that is produced.

The only exception is if the Type Definition contains the continue statement. In that case mkgmap will
continue looking for further matches.

- Where possible always have the same tag on the left. This will make things more predictable.
- Always set made-up tag names if you want to also match on them later, rather than setting tags that
    might be used already.
- Use the echo and echotags actions to understand what’s going on during style processing.

### 4.11. Some examples.......................................................................................................................

The following are some examples of style rules, with explanations of what they do.

#### 4.11.1. Simple examples..........................................................................................................

In the majority of cases everything is very simple. Say you want roads that are tagged as
highway=motorway to have the Garmin type 0x01 ("motorway") and for it to appear up until the zoom
level 3.

Then you would write the following rule.

```
highway=motorway [0x01 level 3]
```
Nodes that have an id and a subid are referenced by concatenating both ids.

```
amenity=bank [0x2f06 level 3]
```
This will be explained in more detail in the following sections along with how to use more than one tag
to make the choice.

For a roundabout you may want to use the special Garmin type 0xc in combination with an overlaying
way that shows the road importance. You can do this with two rules like this

```
junction=roundabout & (highway=tertiary | highway=tertiary_link)
[0x0c road_class=1 road_speed=1 resolution 24 continue]
junction=roundabout & (highway=tertiary | highway=tertiary_link)
[0x10804 resolution 21]
```

```
Style rules
```
or shorter with one rule that has two type definitions

```
junction=roundabout & (highway=tertiary | highway=tertiary_link)
[0x0c road_class=1 road_speed=1 resolution 24] [0x10804 resolution 21]
```
#### 4.11.2. More involved examples.............................................................................................

A few tips and tricks showing how the rules can be used to create almost any effect.

### Example 4.2. Internet cafes

```
amenity=cafe & internet_access=wlan {name '${name} (wifi)'} [0x2a14 resolution 23]
```
Checks to see if an OSM object has both the amenity=cafe and internet_access=wlan key/tag pairs. If
name=Joe’s Coffee Shop, then the Garmin object will be named Joe’s Coffee Shop (wifi). The Garmin
object used will be 0x2a14 and the object will only appear at resolutions 23 and 24

### Example 4.3. Guideposts

```
information=guidepost
{ name '${name} - ${operator} - ${description} '
| '${name} - ${description}'
| '${name}'
| '${description}'
| '${operator}'
| '${ref}'
}
[0x4c02 resolution 23 default_name 'Infopost']
```
Checks to see if an OSM object has the information=guidepost key/tag pair. If so then the name will be
set depending on the available name, operator and description tags as follows.

1.If for example we have the tags name="Route 7", operator="Kizomba National Parks" and
description="Trail signpost", then the Garmin object will be named Route 7 - Kizomba
National Parks - Trail signpost.

2.If the OSM object just has the name and description tags set, the Garmin object will be named
Route 7 - Trail signpost

3.If just the name tag is available, the Garmin object will be named Route 7

4.If just the description tag is available, the Garmin object will be named Trail signpost;

5.and if just the operator tag is available, the Garmin object will be named Kizomba National Parks.

The Garmin object used will be 0x4c02 and will only appear at resolutions 23 and 24

### Example 4.4. Car sales rooms

```
shop=car {name '${name} (${operator})' | '${name}' |'${operator}'} [0x2f07 resolution 23]
```
If name="Alice’s Car Salesroom" and operator=Nissan, the Garmin object will be named Alice’s Car
Salesroom (Nissan)


```
Style rules
```
### Example 4.5. Opening hours in postcode field

This is a trick to get opening hours to show up in the postcode field of a POI. Tricks like this can
enhance the map for certain uses, but of course may prevent the proper use of the postcode field.

```
opening_hours=* {set addr:postcode = '${addr:postcode} open ${opening_hours}'
| 'open ${opening_hours}'}
```
For any OSM object which has the opening_hours key set to a value, this sets the postcode to include
the opening hours. For example, if addr:postcode=90210, addr:street=Alya Street, addr:city=Lagos and
addr:housenumber=7 and opening_hours=09.00-17.00, the address field of the Garmin POI will be 7,
Alya Street, Lagos, 90210 open 09.00-17.00.

### Example 4.6. Mountain Passes depending on the way they belong to

```
mkgmap:from-node:mountain_pass=yes & highway=* & highway!=path & highway!=track
{set mkgmap:label:1='${mkgmap:from-node:name}'} [0x5208 resolution 24-14]
```
Note: This only works if you activated --add-pois-to-lines. When you activate this option, all points of a
line (a way in OpenStreetMap) generate a point.

Those points attributes are those from OpenStreetMap’s way. The specific node’s attributes are set as
mkgmap:from-node:attribute_name. For instance, here, all points from a way are available to a "points"
rule. We’re looking for mountain passes, but only if they can be reached by something else than a path
or a track. So we match all points that belong to a way that’s not a path or a track, and where the original
point is tagged as a mountain pass.

Please note that if the point is part of several ways, you’ll get duplicates (you could use --nearby-poi-
rules to solve this).


Chapter 5. Creating a style

### 5.1. Testing a style..........................................................................................................................

You can test your style by calling mkgmap with the --style-file=path-to-style and the --list-
styles option. If you see your style listed, then your style is recognized by mkgmap. Additional tests
are performed if you use the --check-styles option. The type values are verified to make sure that they
are valid. Further checks try to find rules which assign a routable type to a line without making it a road
by assigning road_class or road_speed. This is known to cause problems with routing in routable maps.
Then you can test if your style is valid by using it when creating a map. A style can be used just as it was
created, but if you want to make it available to others it will be easier if you make a zip file out of it and
then you just have the one file to distribute. You just can zip all files of the style. Several different styles
can be placed into the same zip archive file.

To use a zipped style, you can use --style-file=stylename.zip. If there is more than one style in the
zip file, then you can use --style-file=zipname.zip --style=stylename.

#### 5.1.1. Tests performed by check-styles...................................................................................

The --check-styles option verfies that your style uses type values which can processed by mkgmap.

The following rules are verified:

1.If a type is >= 0x0100 (means it has more than one byte), the rightmost byte must be between 0x00
and 0x1f, so e.g. 0x011f is ok, 0x0120 is not.

2.If a type is >= 0x010000, it is an extended type, which can be used for points, lines, and polygons.

3.If the type is not extended, it must be >= 0x0100 for a point, < 0x3f for a line, and < 0x7f for a
polygon.

4.The polygon type 0x4a is reserved for the overview map.

5.It is known that the usage of routable types for non-routable lines in resolution 24 can cause routing
problems (e.g. address search doesn’t work). The check will flag rules that assign a routable type for
a line in resolution 24 without giving road_class or road_speed. A routable type is between 0x01 and
0x13 or one of: 0x1a, 0x1b, 0x16.

6.If road_class or road_speed is given in combination with a non-routable type, the rule is flagged.

### 5.2. Making a style package............................................................................................................

A style can be used just as it was created, but if you want to make it available to others it will be easier if
you combine all the individual files into a single archive file.

#### 5.2.1. Zip archive.....................................................................................................................

The first way of doing this is to combine the files into a zip file and then you just have the one file to
distribute.

To use a zipped style, you can use --style-file=stylename.zip

It does not matter if you include the directory holding the files or not in the archive. The style is found
by searching for the version file.


```
Creating a style
```
You can have more than one style in the zip file, each in their own directory. In this case you must
include the top level directories of the style (and you can include other parent directories as well if you
like). If there is more than one style in the zip file, then you can use the --style option alongside the --
style-file option. --style-file=zipname.zip --style=stylename.

### Example 5.1. Style package layout

```
`-- mystyles
|-- cycle
| |-- lines
| |-- points
| |-- polygons
| `-- version
`-- hiking
|-- lines
|-- points
|-- polygons
`-- version
```
Here there are two styles named cycle and hiking. You can select the ‘hiking’ style with the options --
style-file=mystyles.zip --style=hiking

#### 5.2.2. Simple file archive........................................................................................................

This is formed by appending all of the files of a style into a single file separated by lines that contain the
file name in triple angle brackets.

Single file archive.

```
<<<version>>>
0
```
```
<<<points>>>
amenity=doctor [0x2a2a level 0]
# More point definitions here...
```
```
<<<lines>>>
# All the line definitions here...
```
The file must have a name ending in .style to be recognised.

This file can be easily created in its entirity in a text editor, but you can also convert between the files-in-
a-directory format and the single-file format using the following command:

```
# (to be typed all on one line)
java -cp mkgmap.jar uk.me.parabola.mkgmap.osmstyle.StyleImpl
mystyle > mystyle.style
```
To convert back then supply the file as the argument, rather than the directory.

#### 5.2.3. The Garmin Map...........................................................................................................

Each Garmin map may contain several separate maps which are prepared at different levels of detail, the
most appropriate of these is displayed depending on the zoom selected by the user.

When creating the map, the map maker will choose which of these level maps is displayed according to
the resolution (or zoom) selected. For example, a map might contain three levels (0, 1 & 2); On the level


```
Creating a style
```
2 map (showing the largest area) a town might just be represented by a named dot; as the user zooms in,
the display might switch to the level 1 map showing an outline of the town. Zooming in further might
switch to the level 0 map, with the individual streets of the town shown.

'In addition the GPS itself might decide when to show or hide individual features in each of the 'level
maps, especially with POIs. This is also affected by the detail setting in the map config menu.''

#### 5.2.4. Resolution......................................................................................................................

The first is resolution this is a number between 1 and 24 with 24 being the most detailed resolution and
each number less is half as detailed. So for example if a road was 12 units long at resolution 24 it would
be only 6 at resolution 23 and just 3 at resolution 22.

On a Legend Cx the resolution corresponds the these scales on the device:

### Table 5.1. Resolutions

```
Resolution Scale on device
16 30km-12km
18 8km-3km
20 2km-800m
22 500m-200m
23 300m-80m
24 120m-50m
```
It may be slightly different on different devices. There is an option to increase or decrease the detail and
if you change that from Normal then it will change the values above too.

#### 5.2.5. Level..............................................................................................................................

The next is level. This is a number between 0 and 16 (although perhaps numbers above 10 are not
usable), with 0 corresponding to the most detailed view. The map consists of a number of levels starting
(usually) with 0. For example 0, 1, 2, 3 and a different amount of detail is added at each level.

The map also contains a table to link the level to the resolution. So you can say that level 0 corresponds
to resolution 24.

This mapping is specified in the file options within the style directory in use. You can also specify it on
the command line, for example:

```
--levels=0:24,1:22,2:20
```
This means that the map will have three levels. Level 0 in the map will correspond to resolution 24 (the
most detailed), level 1 will show at resolution 22 (between scales of 500m and 200m) and so on. The
lowest level needs to include at least an object, therefore the default lowest level of 16 will create a
broken map, if your osm input file has no information at zoom level 16 or lower included.

Watch out with levels when building topographical maps

According to the principle that a map is never allowed to have an empty layer, if you have two input
files for mkgmap, you have to specify --levels for each input file. This is especially important when one
of the input files consists exclusively of contour lines. Take the following command as example on how


```
Creating a style
```
to create such a map. (Attention the line wrap is only here for the wiki, this has to be one command in
cmd.exe or terminal)

```
java -jar mkgmap.jar --style-file=D:\path\to\mkgmap\resources\styles\style_name \
--levels=0:24,1:22,2:20,3:18,4:16,5:14,6:12,7:10 data.osm
--levels=0:24,1:22,2:20 srtm.osm
```
This would assume that your contour lines are in layer 24 (minor), 22 (medium) and 20 (major) and your
normal osm data spread between 24 and 10. If you don’t adhere to proper levels you will get problems
with the map not displaying at lower zoom levels, not displaying at higher zoom levels or not displaying
at all (you’ll only see the background polygon 0x4c).

There are 2 alternatives to circumvent having to assign different levels on compile. a) Introduce dummy
objects at the lowest level into your map. A POI in the lowest level per input file is enough. b) Merge
your osm files (either by script or in text editor (text editor may crash though on opening huge .osm
files), and then use the lowest resulting level. Concluding the easiest is to include dummy objects at
lowest level. (it should be thought about mkgmap doing this by default). The lower your lowest level
the later the basemap will exchange your osm map. Your lowest level object is the defined by the object
with the lowest level (as defined in your style) actually present in your osm input file.


Chapter 6. About

### 6.1. Licence......................................................................................................................................

This manual is released under the Creative Commons Attribution-ShareAlike 2.0 license [http://
creativecommons.org/licenses/by-sa/2.0/]. It makes use of some material that was added to the OSM
Wiki which is release under the same licence.

### 6.2. Authors and acknowledgments................................................................................................

This manual is created from material that originated from the mkgmap doc files and added to OSM wiki.
While on the OSM wiki modifications were made by many people.

People who have contributed suggestions and corrections to this document are: Carlos Dávila, Geoff
Sherlock, Ticker Berkin

The list of nicknames of everyone that had modified the wiki pages at the time that this manual was
created is as follows: Brogo, Christian Gawron, Csdf, De muur, Derstefan, DirkS, Extremecarver,
Gernot, !i!, Jinx1971, Katpatuka, MarkS, Master, Mezzanine, Nakor, Nop, Richard, Skela,
SomeoneElse, Tommybgoode, Ulfl, Walterschloegl, WanMil, Willem1, Yggdrasil


