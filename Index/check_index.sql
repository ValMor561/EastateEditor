-- FUNCTION: public.check_index(integer)

-- DROP FUNCTION IF EXISTS public.check_index(integer);

CREATE OR REPLACE FUNCTION check_index(p_count integer)
    RETURNS numeric AS $$
DECLARE
	PK Integer;
	start_time timestamp;
	end_time timestamp;
	average_time numeric(14,8) := 0;
BEGIN
	FOR i IN 1..p_count LOOP
		start_time := clock_timestamp();
		PK := RANDOM() * 90000000 + 10000000 AS INTEGER;
		EXECUTE format('SELECT * FROM "PassportClient" WHERE "PassportNumber" = %L', PK);
		end_time := clock_timestamp();
		average_time := average_time + extract(EPOCH from end_time - start_time);
	END LOOP;
																 
	average_time := average_time / p_count;															 
	
	RAISE NOTICE 'Среднее время выполнения запроса: %', average_time;
	RETURN average_time;
END;
$$ LANGUAGE plpgsql;
