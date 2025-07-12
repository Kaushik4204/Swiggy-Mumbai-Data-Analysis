--Top 50 Highest-Rated Restaurants
SELECT * 
FROM restaurants 
WHERE "Rating" IS NOT NULL
ORDER BY "Rating" DESC
LIMIT 50;

-- Average Cost Per Restaurant
SELECT 
  AVG(CAST(REPLACE(SUBSTR("Cost", 2, INSTR("Cost", ' ') - 2), ',', '') AS INTEGER)) AS average_cost
FROM restaurants
WHERE "Cost" IS NOT NULL;

--Median Cost Per Restaurant
SELECT 
  CAST(REPLACE(SUBSTR("Cost", 2, INSTR("Cost", ' ') - 2), ',', '') AS INTEGER) AS cost_clean
FROM restaurants
WHERE "Cost" IS NOT NULL
ORDER BY cost_clean
LIMIT 1 OFFSET (
  SELECT COUNT(*)/2 FROM restaurants WHERE "Cost" IS NOT NULL
);

--Fastest Delivery Times
SELECT "Name", 
       CAST(REPLACE(SUBSTR("Delivery time", 1, INSTR("Delivery time", ' ') - 1), '−', '') AS INTEGER) AS delivery_time
FROM restaurants
WHERE "Delivery time" LIKE '%MIN%'
ORDER BY delivery_time ASC
LIMIT 50;

--Slowest Delivery Times
SELECT "Name", 
       CAST(REPLACE(SUBSTR("Delivery time", 1, INSTR("Delivery time", ' ') - 1), '−', '') AS INTEGER) AS delivery_time
FROM restaurants
WHERE "Delivery time" LIKE '%MIN%'
ORDER BY delivery_time DESC
LIMIT 50;

--Count of restairant per cuisine
SELECT "Specials", COUNT(*) as count
FROM restaurants
GROUP BY "Specials"
ORDER BY count DESC
LIMIT 10;

--Restaurants Offering 50%+ Discounts
SELECT "Name", "Coupons"
FROM restaurants
WHERE "Coupons" LIKE '%50%' OR "Coupons" LIKE '%60%';

