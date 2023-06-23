CREATE OR REPLACE FUNCTION update_employee(p_id INTEGER, p_surname varchar(20), p_firsname varchar(20), p_companyname varchar(20))
RETURNS VOID AS $$
BEGIN
UPDATE "Employee"
	SET "Surname"=p_surname, "Name"=p_firsname, "CompanyId" = (SELECT "CompanyId" from "Company" where "Name" = p_companyname)
	WHERE "EmployeeID"=p_id;
END;
$$ LANGUAGE plpgsql;	
