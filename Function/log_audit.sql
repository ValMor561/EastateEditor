CREATE OR REPLACE FUNCTION log_audit(username text, event_type text) RETURNS VOID AS $$
BEGIN
  INSERT INTO "audit_log" ("username", "event_type", "event_timestamp")
  VALUES (p_username, p_event_type, NOW());
END;
$$ LANGUAGE plpgsql;
