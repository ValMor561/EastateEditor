CREATE OR REPLACE FUNCTION get_real_eastate(page_num integer)
RETURNS TABLE (
	objectid integer,
    address text,
    square integer,
    object_type text,
    district_name text,
    city text,
    owner_surname varchar(20),
    owner_name varchar(20)
) AS $$
BEGIN
    RETURN QUERY
		SELECT reo."ObjectId", reo."Address", reo."Square", reo."ObjectType", d."Name", d."City", pc."Surname", pc."Name"
        FROM "RealEastateObject" reo
        JOIN "District" d ON reo."DistrictId" = d."DistrictId"
        JOIN "PassportClient" pc ON reo."OwnerPassportNumber" = pc."PassportNumber"
        ORDER BY reo."ObjectId" DESC OFFSET (page_num - 1) * 59 LIMIT 59;
END;
$$ LANGUAGE plpgsql;