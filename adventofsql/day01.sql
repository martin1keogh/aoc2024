SELECT name
     , wishes ->> 'first_choice'
     , wishes ->> 'second_choice'
     , (wishes -> 'colors') ->> 0
     , JSONB_ARRAY_LENGTH((wishes -> 'colors')::JSONB)
     , CASE difficulty_to_make
           WHEN 1 THEN 'Simple Gift'
           WHEN 2 THEN 'Moderate Gift'
           ELSE 'Complex Gift'
      END
     , CASE category
           WHEN 'outdoor' THEN 'Outside Workshop'
           WHEN 'educational' THEN 'Learning Workshop'
           ELSE 'General Workshop'
      END
FROM children
CROSS JOIN LATERAL (
    SELECT *
    FROM wish_lists
    WHERE children.child_id = wish_lists.child_id
--     ORDER BY submitted_date DESC
--     LIMIT 1
)
CROSS JOIN LATERAL (
    SELECT *
    FROM toy_catalogue
    WHERE wishes ->> 'first_choice' = toy_name
)
ORDER BY name
LIMIT 5
;

