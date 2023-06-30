CREATE  OR  REPLACE  FUNCTION get_employee_curs( )  
RETURNS refcursor AS $$
DECLARE 
 	c_ref refcursor; 
BEGIN 
  OPEN c_ref FOR 
  SELECT em."EmployeeID", em."Surname", em."Name", com."Name"
        FROM "Employee" em
        JOIN "Company" com ON em."CompanyId" = com."CompanyId";
  RETURN c_ref;                                                       
END ;
$$ LANGUAGE plpgsql;