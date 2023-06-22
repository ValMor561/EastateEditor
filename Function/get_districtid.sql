CREATE OR REPLACE FUNCTION get_districtid()
RETURNS TABLE (DistrictID varchar(18)) AS $$
BEGIN
  RETURN QUERY SELECT d."DistrictId" FROM "District" d;
END;
$$ LANGUAGE plpgsql;
