CREATE OR REPLACE FUNCTION get_company_name()
RETURNS TABLE (CompanyName varchar(20)) AS $$
BEGIN
  RETURN QUERY SELECT comp."Name" FROM "Company" comp;
END;
$$ LANGUAGE plpgsql;
