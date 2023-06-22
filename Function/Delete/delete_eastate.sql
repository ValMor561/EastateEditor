CREATE OR REPLACE FUNCTION delete_eastate(p_id INTEGER)
RETURNS VOID AS $$
BEGIN
    DELETE FROM "RealEastateObject" WHERE "ObjectId" = p_id;
END;
$$ LANGUAGE plpgsql;