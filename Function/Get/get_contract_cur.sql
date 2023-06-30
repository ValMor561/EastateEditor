CREATE  OR  REPLACE  FUNCTION get_contract_curs( )  
RETURNS refcursor AS $$
DECLARE 
 	c_ref refcursor; 
BEGIN 
  OPEN c_ref FOR 
  SELECT contr."ContractID", contr."DateOfContract", contr."DateOfPayment", contr."CostOfObject", contr."ContractType", ROW(empl."Surname", empl."Name")::employee_sn,  pco."Surname", pco."Name", pcc."Surname", pcc."Name" 
        FROM "Contract" contr
        JOIN "Employee" empl ON contr."EmployeeID" = empl."EmployeeID"
        JOIN "PassportClient" pco ON contr."OwnerPassportNumber" = pco."PassportNumber"
        JOIN "PassportClient" pcc ON contr."ClientPassportNumber" = pcc."PassportNumber";
RETURN c_ref;                                                       
END ;
$$ LANGUAGE plpgsql;