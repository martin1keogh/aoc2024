WITH u AS (
    SELECT *
    FROM letters_a
    UNION ALL
    SELECT *
    FROM letters_b
)
SELECT STRING_AGG(CHR(value), '' ORDER BY id)
FROM u
WHERE value BETWEEN 65 AND 90
   OR value BETWEEN 97 AND 122
   OR CHR(value) IN (' ', '!', '"', $$'$$, '(', ')', ',', '-', '.', ':', ';', '?')

