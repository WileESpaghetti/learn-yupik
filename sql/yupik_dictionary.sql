PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

-- These represent the 4 sections of the Red Dictionary --
CREATE TABLE sections (
  id integer primary key,
  name text
);

INSERT INTO "sections" VALUES(1,'bases');
INSERT INTO "sections" VALUES(2,'postbases');
INSERT INTO "sections" VALUES(3,'ending');
INSERT INTO "sections" VALUES(4,'enclitic');

-- word types are mainly for converting from citation form  to base --
-- FIXME this is only for words in the 'bases' section of the dictionary
CREATE TABLE word_types (
  id integer primary key,
  type text
);

INSERT INTO "word_types" VALUES(1, 'noun');
INSERT INTO "word_types" VALUES(2, 'demonstrative pronoun');
INSERT INTO "word_types" VALUES(3, 'demonstrative adverb');
INSERT INTO "word_types" VALUES(4, 'positional base');
INSERT INTO "word_types" VALUES(5, 'verb');
INSERT INTO "word_types" VALUES(6, 'exclamation');
INSERT INTO "word_types" VALUES(7, 'adverb');
INSERT INTO "word_types" VALUES(8, 'interogative participal');
INSERT INTO "word_types" VALUES(9, 'root');

CREATE TABLE dialects (
  id integer primary key,
  abr text,
  name text
);

INSERT INTO "dialects" VALUES(1, 'NSU', 'unaliq/Norton Sound North');
INSERT INTO "dialects" VALUES(2, 'NSK', 'kotlik/Norton Sound South');
INSERT INTO "dialects" VALUES(3, 'NS', 'Norton Sound');
INSERT INTO "dialects" VALUES(4, 'Y', 'Yukon');
INSERT INTO "dialects" VALUES(5, 'HBC', 'Hooper Bay and Chevak');
INSERT INTO "dialects" VALUES(6, 'NI', 'Nelson Island');
INSERT INTO "dialects" VALUES(7, 'NUN', 'Nunivak Island');
INSERT INTO "dialects" VALUES(8, 'K', 'Kuskokwim');
INSERT INTO "dialects" VALUES(9, 'BB','Bristol Bay');
INSERT INTO "dialects" VALUES(10, 'NR', 'Nushagak');
INSERT INTO "dialects" VALUES(11, 'LI', 'Lake Illiamna');
INSERT INTO "dialects" VALUES(12, 'UK', 'Upper Kuskokwim');

 -- word does not belong to a particular dialect. --
 -- this should be the default --
INSERT INTO "dialects" VALUES(13, 'NONE', 'NONE');


CREATE TABLE words (
  id integer primary key,
  citation_form text,
  section,
    wtype,
  dialect,
   parent,
  FOREIGN KEY(section) REFERENCES sections(id),
  FOREIGN KEY(wtype) REFERENCES word_types(id),
  FOREIGN KEY(dialect) REFERENCES dialects(id),
  FOREIGN KEY(parent)  REFERENCES words(id) -- useful for creating subentries --
);


CREATE TABLE definitions (
  def_id integer PRIMARY KEY,
  definition text,
  word, FOREIGN KEY(word) REFERENCES words(id)
);


CREATE TABLE examples (
  ex_id integer primary key,
  ex_word text, -- the word being used in the example --
  translation text,
  parent, FOREIGN KEY(parent) REFERENCES words(id) -- the main entry word --
);


COMMIT;
