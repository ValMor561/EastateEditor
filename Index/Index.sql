CREATE INDEX default_index ON "PassportClient" ("PassportNumber");
select check_index(10000);
DROP INDEX default_index;

CREATE INDEX hash_index ON "PassportClient" USING HASH ("PassportNumber");
select check_index(10000);
DROP INDEX hash_index;

CREATE INDEX brin_index ON "PassportClient" USING BRIN ("PassportNumber");
select check_index(10000);
DROP INDEX brin_index;

CREATE INDEX btre_index ON "PassportClient" USING BTREE ("PassportNumber");
select check_index(10000);
DROP INDEX btree_index;
