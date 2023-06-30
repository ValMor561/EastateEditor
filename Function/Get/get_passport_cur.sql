CREATE  OR  REPLACE  FUNCTION get_passport_curs( )  
RETURNS refcursor AS $$
DECLARE 
 	c_ref refcursor; 
BEGIN 
  OPEN c_ref FOR 
  SELECT ps."PassportNumber", ps."Surname", ps."Name", ps."PassportNumber", ps."CodeOffice", ps."Date", ps."City", ps."Age", ps."Family"
        FROM "PassportClient" ps;
  RETURN c_ref;                                                       
END ;
$$ LANGUAGE plpgsql;