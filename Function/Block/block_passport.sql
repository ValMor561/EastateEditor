CREATE OR REPLACE FUNCTION block_passport(p_id INTEGER)
RETURNS VOID AS $$
BEGIN
PERFORM * FROM "PassportClient" WHERE "PassportNumber"=p_id FOR UPDATE;
END;
$$ LANGUAGE plpgsql;	
