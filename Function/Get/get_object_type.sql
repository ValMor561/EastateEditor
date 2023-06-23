CREATE OR REPLACE FUNCTION get_object_type()
RETURNS TABLE (ObjectType text) AS $$
BEGIN
  RETURN QUERY SELECT DISTINCT east."ObjectType" FROM "RealEastateObject" east;
END;
$$ LANGUAGE plpgsql;
