CREATE OR REPLACE FUNCTION block_employee(p_id INTEGER)
RETURNS VOID AS $$
BEGIN
PERFORM * FROM "Employee" WHERE "EmployeeID"=p_id FOR UPDATE;
END;
$$ LANGUAGE plpgsql;	
