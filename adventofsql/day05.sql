SELECT production_date
     , toys_produced
     , LAG(toys_produced) OVER by_day                                                            AS previous_day_production
     , toys_produced - LAG(toys_produced) OVER by_day                                            AS production_change
     , 100.0 * (toys_produced - LAG(toys_produced) OVER by_day) / LAG(toys_produced) OVER by_day AS production_change_percentage
FROM toy_production
WINDOW by_day AS (ORDER BY production_date)
ORDER BY 100.0 * (toys_produced - LAG(toys_produced) OVER by_day) / LAG(toys_produced) OVER by_day DESC NULLS LAST
LIMIT 1

