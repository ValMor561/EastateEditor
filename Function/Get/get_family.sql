CREATE OR REPLACE FUNCTION get_family()
RETURNS TABLE (p_family varchar(18)) AS $$
BEGIN
  RETURN QUERY SELECT DISTINCT pc."Family" FROM "PassportClient" pc;
END;
$$ LANGUAGE plpgsql;
