CREATE OR REPLACE FUNCTION get_passports()
RETURNS TABLE (PassportNumber INT) AS $$
BEGIN
  RETURN QUERY SELECT pc."PassportNumber" FROM "PassportClient" pc ORDER BY pc."PassportNumber";
END;
$$ LANGUAGE plpgsql;
