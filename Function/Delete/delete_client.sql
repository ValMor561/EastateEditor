CREATE OR REPLACE FUNCTION delete_client(p_id INTEGER)
RETURNS VOID AS $$
BEGIN
	UPDATE "Contract" SET "OwnerPassportNumber" = NULL
	WHERE "OwnerPassportNumber" IN (SELECT "PassportNumber" 
									FROM "PassportClient" 
									WHERE "PassportNumber" = p_id);
	UPDATE "Contract" SET "ClientPassportNumber" = NULL
	WHERE "OwnerPassportNumber" IN (SELECT "PassportNumber" 
									FROM "PassportClient" 
									WHERE "PassportNumber" = p_id);
	UPDATE "RealEastateObject" SET "OwnerPassportNumber" = NULL
	WHERE "OwnerPassportNumber" IN (SELECT "PassportNumber" 
									FROM "PassportClient" 
									WHERE "PassportNumber" = p_id);
    DELETE FROM "PassportClient" WHERE "PassportNumber" = p_id;
END;
$$ LANGUAGE plpgsql;