CREATE OR REPLACE FUNCTION public.check_user_auth(p_login text,	p_password text) 
RETURNS boolean AS $$
BEGIN
  RETURN EXISTS(SELECT 1 FROM "Users" WHERE "login" = $1 AND "password" = $2);
END;
$$ LANGUAGE plpgsql;
