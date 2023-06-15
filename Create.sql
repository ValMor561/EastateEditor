CREATE FUNCTION check_user_auth(login text, password text) RETURNS boolean AS $$
BEGIN
  RETURN EXISTS(SELECT 1 FROM "Users" WHERE "login" = $1 AND "password" = $2);
END;
$$ LANGUAGE plpgsql;
