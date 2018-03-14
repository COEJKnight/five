--------------------------------------------------------
-- Created using matview_sql_generator.py             --
--    The SQL definition is stored in a json file     --
--    Look in matview_generator for the code.         --
--                                                    --
--         !!DO NOT DIRECTLY EDIT THIS FILE!!         --
--------------------------------------------------------
DROP MATERIALIZED VIEW IF EXISTS summary_view_naics_codes_temp CASCADE;
DROP MATERIALIZED VIEW IF EXISTS summary_view_naics_codes_old CASCADE;

CREATE MATERIALIZED VIEW summary_view_naics_codes_temp AS
SELECT
  MD5(array_to_string(sort(array_agg("transaction_normalized"."id"::int)), ' ')) AS pk,
  "transaction_normalized"."action_date",
  "transaction_normalized"."fiscal_year",
  "transaction_normalized"."type",
  "transaction_fpds"."pulled_from",
  "transaction_fpds"."naics" AS naics_code,
  "transaction_fpds"."naics_description",
  SUM(COALESCE("transaction_normalized"."federal_action_obligation", 0))::NUMERIC(20, 2) AS "federal_action_obligation",
  0::NUMERIC(20, 2) AS "original_loan_subsidy_cost",
  COUNT(*) counts
FROM
  "transaction_normalized"
INNER JOIN
  "transaction_fpds" ON ("transaction_normalized"."id" = "transaction_fpds"."transaction_id")
WHERE
  "transaction_normalized".action_date >= '2007-10-01'
GROUP BY
  "transaction_normalized"."action_date",
  "transaction_normalized"."fiscal_year",
  "transaction_normalized"."type",
  "transaction_fpds"."pulled_from",
  "transaction_fpds"."naics",
  "transaction_fpds"."naics_description";

CREATE UNIQUE INDEX idx_1b698194$ca7_unique_pk_temp ON summary_view_naics_codes_temp USING BTREE("pk") WITH (fillfactor = 97);
CREATE INDEX idx_1b698194$ca7_action_date_temp ON summary_view_naics_codes_temp USING BTREE("action_date" DESC NULLS LAST) WITH (fillfactor = 97);
CREATE INDEX idx_1b698194$ca7_type_temp ON summary_view_naics_codes_temp USING BTREE("type") WITH (fillfactor = 97);
CREATE INDEX idx_1b698194$ca7_naics_temp ON summary_view_naics_codes_temp USING BTREE("naics_code") WITH (fillfactor = 97) WHERE "naics_code" IS NOT NULL;
CREATE INDEX idx_1b698194$ca7_pulled_from_temp ON summary_view_naics_codes_temp USING BTREE("pulled_from") WITH (fillfactor = 97) WHERE "pulled_from" IS NOT NULL;

ALTER MATERIALIZED VIEW IF EXISTS summary_view_naics_codes RENAME TO summary_view_naics_codes_old;
ALTER INDEX IF EXISTS idx_1b698194$ca7_unique_pk RENAME TO idx_1b698194$ca7_unique_pk_old;
ALTER INDEX IF EXISTS idx_1b698194$ca7_action_date RENAME TO idx_1b698194$ca7_action_date_old;
ALTER INDEX IF EXISTS idx_1b698194$ca7_type RENAME TO idx_1b698194$ca7_type_old;
ALTER INDEX IF EXISTS idx_1b698194$ca7_naics RENAME TO idx_1b698194$ca7_naics_old;
ALTER INDEX IF EXISTS idx_1b698194$ca7_pulled_from RENAME TO idx_1b698194$ca7_pulled_from_old;

ALTER MATERIALIZED VIEW summary_view_naics_codes_temp RENAME TO summary_view_naics_codes;
ALTER INDEX idx_1b698194$ca7_unique_pk_temp RENAME TO idx_1b698194$ca7_unique_pk;
ALTER INDEX idx_1b698194$ca7_action_date_temp RENAME TO idx_1b698194$ca7_action_date;
ALTER INDEX idx_1b698194$ca7_type_temp RENAME TO idx_1b698194$ca7_type;
ALTER INDEX idx_1b698194$ca7_naics_temp RENAME TO idx_1b698194$ca7_naics;
ALTER INDEX idx_1b698194$ca7_pulled_from_temp RENAME TO idx_1b698194$ca7_pulled_from;

ANALYZE VERBOSE summary_view_naics_codes;
GRANT SELECT ON summary_view_naics_codes TO readonly;
