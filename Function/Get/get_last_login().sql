CREATE FUNCTION get_last_login_username()
RETURNS TEXT AS $$
DECLARE
  p_username TEXT;
BEGIN
  SELECT "username" into p_username   FROM "audit_log" 
  WHERE "event_type" = 'Вход'
  ORDER BY "id" DESC
  LIMIT 1;
  RETURN p_username;
END;
$$ LANGUAGE plpgsql;
