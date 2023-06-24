CREATE OR REPLACE FUNCTION add_passport(p_surname varchar(20), p_name varchar(20), p_passport integer,  p_code integer, p_birthday date, p_city text, p_age integer, p_family varchar(18))
RETURNS VOID AS $$
BEGIN
INSERT INTO "PassportClient"("PassportNumber", "Date", "CodeOffice", "Family", "Name", "Surname", "City", "Age")
	VALUES (p_passport, p_birthday, p_code, p_family, p_name, p_surname, p_city, p_age);END;
$$ LANGUAGE plpgsql;	
