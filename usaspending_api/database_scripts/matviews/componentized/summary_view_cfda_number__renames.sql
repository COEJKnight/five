--------------------------------------------------------
-- Created using matview_sql_generator.py             --
--    The SQL definition is stored in a json file     --
--    Look in matview_generator for the code.         --
--                                                    --
--         !!DO NOT DIRECTLY EDIT THIS FILE!!         --
--------------------------------------------------------
ALTER MATERIALIZED VIEW IF EXISTS summary_view_cfda_number RENAME TO summary_view_cfda_number_old;
ALTER INDEX IF EXISTS idx_2b3678a9$a8a_unique_pk RENAME TO idx_2b3678a9$a8a_unique_pk_old;
ALTER INDEX IF EXISTS idx_2b3678a9$a8a_action_date RENAME TO idx_2b3678a9$a8a_action_date_old;
ALTER INDEX IF EXISTS idx_2b3678a9$a8a_type RENAME TO idx_2b3678a9$a8a_type_old;
ALTER INDEX IF EXISTS idx_2b3678a9$a8a_pulled_from RENAME TO idx_2b3678a9$a8a_pulled_from_old;

ALTER MATERIALIZED VIEW summary_view_cfda_number_temp RENAME TO summary_view_cfda_number;
ALTER INDEX idx_2b3678a9$a8a_unique_pk_temp RENAME TO idx_2b3678a9$a8a_unique_pk;
ALTER INDEX idx_2b3678a9$a8a_action_date_temp RENAME TO idx_2b3678a9$a8a_action_date;
ALTER INDEX idx_2b3678a9$a8a_type_temp RENAME TO idx_2b3678a9$a8a_type;
ALTER INDEX idx_2b3678a9$a8a_pulled_from_temp RENAME TO idx_2b3678a9$a8a_pulled_from;
