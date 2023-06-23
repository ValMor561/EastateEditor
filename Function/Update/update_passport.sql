CREATE OR REPLACE FUNCTION update_passport(p_id INTEGER, p_surname varchar(20), p_name varchar(20), p_passport integer,  p_code integer, p_birthday date, p_city text, p_age integer, p_family varchar(18))
RETURNS VOID AS $$
BEGIN
UPDATE "PassportClient"
	SET "Surname"=p_surname, "Name"=p_name, "PassportNumber"=p_passport, "Date"=p_birthday, "CodeOffice"=p_code, "Family"=p_family,  "City"=p_city, "Age"=p_age
	WHERE "PassportNumber"=p_id;
END;
$$ LANGUAGE plpgsql;	
