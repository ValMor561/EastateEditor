CREATE OR REPLACE FUNCTION add_real_estate_object(p_address text, p_square integer, p_type text, p_district varchar(18), p_passport integer)
RETURNS VOID AS $$
BEGIN
INSERT INTO "RealEastateObject"("Address", "Square", "ObjectType", "DistrictId", "OwnerPassportNumber")
	VALUES (p_address, p_square, p_type, p_district, p_passport);
END;
$$ LANGUAGE plpgsql;	
