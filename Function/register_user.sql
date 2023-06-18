CREATE OR REPLACE FUNCTION public.register_user(p_login text,p_password text)
RETURNS boolean AS $$
DECLARE
    user_exists INTEGER;
BEGIN
    -- проверяем, есть ли уже пользователь с таким же именем
    SELECT COUNT(*) INTO user_exists FROM "Users" WHERE "login" = $1;
    IF user_exists > 0 THEN
        RETURN false; -- пользователь уже существует
    ELSE
        -- добавляем нового пользователя в базу данных
        INSERT INTO "Users" ("login", "password") VALUES ($1, $2);
        RETURN true; -- пользователь успешно зарегистрирован
    END IF;
END;
$$ LANGUAGE plpgsql;
