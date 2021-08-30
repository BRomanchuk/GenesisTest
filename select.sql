SELECT category_name, avg_cost FROM
  (SELECT category_name, avg(cost) as avg_cost FROM
  adverts INNER JOIN costs ON adverts.advert_id = costs.advert_id
  GROUP BY category_name)
WHERE avg_cost > 500
