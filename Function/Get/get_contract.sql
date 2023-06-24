CREATE OR REPLACE FUNCTION get_contract(page_num integer)
RETURNS TABLE (
	contrid integer,
    date_of_contract date,
    date_of_payment date,
    cost_of_object int,
	contact_type varchar(20),
    employee_surname varchar(20),
	owner_surname varchar(20),
    owner_name varchar(20),
    client_surname varchar(20),
    client_name varchar(20)
) AS $$
BEGIN
    RETURN QUERY
		SELECT contr."ContractID", contr."DateOfContract", contr."DateOfPayment", contr."CostOfObject", contr."ContractType", empl."Surname",  pco."Surname", pco."Name", pcc."Surname", pcc."Name" 
        FROM "Contract" contr
        JOIN "Employee" empl ON contr."EmployeeID" = empl."EmployeeID"
        JOIN "PassportClient" pco ON contr."OwnerPassportNumber" = pco."PassportNumber"
        JOIN "PassportClient" pcc ON contr."ClientPassportNumber" = pcc."PassportNumber"
		ORDER BY contr."ContractID" DESC OFFSET (page_num - 1) * 59 LIMIT 59;
END;
$$ LANGUAGE plpgsql;