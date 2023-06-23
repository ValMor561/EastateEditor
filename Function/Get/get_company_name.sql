CREATE OR REPLACE FUNCTION get_company_name()
RETURNS TABLE (CompanyName text) AS $$
BEGIN
  RETURN QUERY SELECT comp."Name" FROM "Company" comp;
END;
$$ LANGUAGE plpgsql;
