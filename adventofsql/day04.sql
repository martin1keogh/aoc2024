WITH s AS (
    SELECT toy_id
         , (SELECT ARRAY_AGG(t) FROM (SELECT * FROM unnest(new_tags) AS f(t) EXCEPT SELECT * FROM unnest(previous_tags))) AS added_tags
         , (SELECT ARRAY_AGG(t) FROM (SELECT * FROM unnest(new_tags) AS f(t) INTERSECT SELECT * FROM unnest(previous_tags))) AS unchanged_tags
         , (SELECT ARRAY_AGG(t) FROM (SELECT * FROM unnest(previous_tags) AS f(t) EXCEPT SELECT * FROM unnest(new_tags))) AS removed_tags
    FROM toy_production
)
SELECT toy_id
     , cardinality(added_tags) AS added_tags_count
     , cardinality(unchanged_tags) AS unchanged_tags_count
     , cardinality(removed_tags) AS removed_tags_count
FROM s
ORDER BY cardinality(added_tags) DESC NULLS LAST
LIMIT 1
