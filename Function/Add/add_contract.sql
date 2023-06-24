CREATE OR REPLACE FUNCTION add_contract(p_date_of_contract date,p_date_of_payment date,
    p_cost_of_object int, p_contact_type varchar(20), p_employee_id integer, p_owner_id integer, p_client_id integer)
RETURNS VOID AS $$
BEGIN
INSERT INTO public."Contract"(
	"DateOfContract", "DateOfPayment", "CostOfObject", "EmployeeID", "ContractType", "OwnerPassportNumber", "ClientPassportNumber")
	VALUES (p_date_of_contract, p_date_of_payment, p_cost_of_object, p_employee_id, p_contact_type, p_owner_id, p_client_id);
END;
$$ LANGUAGE plpgsql;	
