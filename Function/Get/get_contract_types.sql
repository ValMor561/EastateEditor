CREATE OR REPLACE FUNCTION get_contract_types()
RETURNS TABLE (ContactTypes varchar(20)) AS $$
BEGIN
  RETURN QUERY SELECT DISTINCT contr."ContractType" FROM "Contract" contr;
END;
$$ LANGUAGE plpgsql;
