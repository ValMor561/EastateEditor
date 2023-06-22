CREATE OR REPLACE FUNCTION delete_employee(p_id INTEGER)
RETURNS VOID AS $$
BEGIN
	UPDATE "Contract" SET "EmployeeID" = NULL
	WHERE "EmployeeID" IN (SELECT "EmployeeID" 
									FROM "Employee" 
									WHERE "EmployeeID" = p_id);
    DELETE FROM "Employee" WHERE "EmployeeID" = p_id;
END;
$$ LANGUAGE plpgsql;