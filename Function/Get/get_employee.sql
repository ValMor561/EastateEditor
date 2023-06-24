CREATE OR REPLACE FUNCTION get_employee(page_num integer)
RETURNS TABLE (
	employeetid integer,
    surname varchar(20),
    firsname varchar(20),
	companyname text
) AS $$
BEGIN
    RETURN QUERY
		SELECT em."EmployeeID", em."Surname", em."Name", com."Name"
        FROM "Employee" em
        JOIN "Company" com ON em."CompanyId" = com."CompanyId"
        ORDER BY em."EmployeeID" DESC OFFSET (page_num - 1)* 59 LIMIT 59;
END;
$$ LANGUAGE plpgsql;