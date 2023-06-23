CREATE OR REPLACE FUNCTION update_real_estate_object(p_id INTEGER, p_address text, p_square integer, p_type text, p_district varchar(18), p_passport integer)
RETURNS VOID AS $$
BEGIN
UPDATE "RealEastateObject"
	SET "Address"=p_address, "Square"=p_square, "ObjectType"=p_type, "DistrictId"=p_district, "OwnerPassportNumber"=p_passport
	WHERE "ObjectId"=p_id;
END;
$$ LANGUAGE plpgsql;	
