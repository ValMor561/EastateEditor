CREATE OR REPLACE FUNCTION get_passport_client(page_num integer)
RETURNS TABLE (
	psid integer,
    surname varchar(20),
    firstname varchar(20),
	passport integer,
	code integer, 
	birthday date,
	city text,
	age integer,
	family_stat varchar(18)
) AS $$
BEGIN
    RETURN QUERY
		SELECT ps."PassportNumber", ps."Surname", ps."Name", ps."PassportNumber", ps."CodeOffice", ps."Date", ps."City", ps."Age", ps."Family"
        FROM "PassportClient" ps
        OFFSET (page_num - 1) * 59 LIMIT 59;
END;
$$ LANGUAGE plpgsql;