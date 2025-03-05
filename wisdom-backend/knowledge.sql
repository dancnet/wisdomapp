PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "questions" (
	"id"	INTEGER,
	"node_id"	INTEGER NOT NULL,
	"question"	TEXT NOT NULL DEFAULT '',
	FOREIGN KEY("node_id") REFERENCES "nodes"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "nodes" (
	"id"	INTEGER,
	"parentid"	INTEGER,
	"mindmap_id"	INTEGER NOT NULL,
	"topic"	TEXT NOT NULL DEFAULT 'New node',
	"direction"	INTEGER NOT NULL DEFAULT 1,
	"expanded"	INTEGER NOT NULL DEFAULT 1,
	"isroot"	INTEGER NOT NULL DEFAULT 0,
	"background_color"	TEXT NOT NULL DEFAULT '#607d8b',
	"text_color"	TEXT NOT NULL DEFAULT '#fff',
	"markdown"	TEXT NOT NULL DEFAULT '',
	FOREIGN KEY("mindmap_id") REFERENCES "mindmaps"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("id"),
	FOREIGN KEY("parentid") REFERENCES "nodes"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO nodes VALUES(1,NULL,1,'Playground',1,1,1,'#607d8b','#fff','hi there!');
CREATE TABLE IF NOT EXISTS "attachments" (
	"id"	INTEGER,
	"node_id"	INTEGER NOT NULL,
	"mime_type"	TEXT NOT NULL,
	"data"	BLOB NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("node_id") REFERENCES "nodes"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "mindmaps" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL DEFAULT 'New Mindmap',
	PRIMARY KEY("id")
);
INSERT INTO mindmaps VALUES(1,'Playground');
CREATE VIEW nodes_short AS
SELECT id, mindmap_id, parentid, topic,
CASE WHEN direction = -1 THEN 'left' WHEN direction = 1 THEN 'right' ELSE direction END AS direction,
expanded, isroot, `background_color` AS `background-color`, `text_color` AS `foreground-color`
FROM nodes;
COMMIT;
