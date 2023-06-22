CREATE OR REPLACE FUNCTION get_employee_number()
RETURNS TABLE (EmployeeId integer) AS $$
BEGIN
  RETURN QUERY SELECT empl."EmployeeID" FROM "Employee" empl;
END;
$$ LANGUAGE plpgsql;
