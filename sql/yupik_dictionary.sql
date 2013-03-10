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


CREATE TABLE words (
  id integer primary key,
  citation_form text,
  section, FOREIGN KEY(section) REFERENCES sections(id)
);


CREATE TABLE definitions (
  def_id integer PRIMARY KEY,
  definition text,
  word, FOREIGN KEY(word) REFERENCES words(id)
);


COMMIT;
