CREATE OR REPLACE FUNCTION update_contract(p_id INTEGER, p_date_of_contract date,p_date_of_payment date,
    p_cost_of_object int, p_contact_type varchar(20), p_employee_id integer, p_owner_id integer, p_client_id integer)
RETURNS VOID AS $$
BEGIN
UPDATE "Contract"
	SET "DateOfContract"=p_date_of_contract, "DateOfPayment"=p_date_of_payment, "CostOfObject"=p_cost_of_object, "EmployeeID"=p_employee_id, "ContractType"=p_contact_type, "OwnerPassportNumber"=p_owner_id, "ClientPassportNumber"=p_client_id
	WHERE "ContractID"=p_id;
END;
$$ LANGUAGE plpgsql;	
