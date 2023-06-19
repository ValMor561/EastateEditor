CREATE OR REPLACE FUNCTION get_employee(page_num integer)
RETURNS TABLE (
	employeetid integer,
    surname varchar(20),
    firsname varchar(20),
	companyname varchar(20)
) AS $$
BEGIN
    RETURN QUERY
		SELECT em."EmployeeID", em."Surname", em."Name", com."Name"
        FROM "Employee" em
        JOIN "Company" com ON em."CompanyId" = com."CompanyId"
        ORDER BY em."EmployeeID" OFFSET (page_num - 1)* 55 LIMIT 55;
END;
$$ LANGUAGE plpgsql;