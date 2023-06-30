CREATE  OR  REPLACE  FUNCTION get_reo_curs( )  
RETURNS refcursor AS $$
DECLARE 
 	c_ref refcursor; 
BEGIN 
  OPEN c_ref FOR 
  SELECT reo."ObjectId", reo."Address", reo."Square", reo."ObjectType", d."Name", d."City", pc."Surname", pc."Name"
        FROM "RealEastateObject" reo
        JOIN "District" d ON reo."DistrictId" = d."DistrictId"
        JOIN "PassportClient" pc ON reo."OwnerPassportNumber" = pc."PassportNumber";
  RETURN c_ref;                                                       
END ;
$$ LANGUAGE plpgsql;