CREATE OR REPLACE FUNCTION delete_contract(p_id INTEGER)
RETURNS VOID AS $$
BEGIN
    DELETE FROM "Contract" WHERE "ContractID" = p_id;
END;
$$ LANGUAGE plpgsql;