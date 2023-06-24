CREATE OR REPLACE FUNCTION add_employee(p_surname varchar(20), p_firsname varchar(20), p_companyname varchar(20))
RETURNS VOID AS $$
DECLARE 
	company_id integer;
BEGIN
	SELECT "CompanyId" INTO company_id from "Company" where "Name" = p_companyname;
INSERT INTO "Employee"
	 ("Surname", "Name", "CompanyId") 
	VALUES (p_surname, p_firstname, company_id);
END;
$$ LANGUAGE plpgsql;	
