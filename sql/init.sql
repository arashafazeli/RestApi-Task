INSERT INTO beers (id, beer_id, name, price, alcohol_percentage)
VALUES
  (1, 73513513, 'Stockholm Beer', 12.95, 5.0),
  (2, 73513514, 'Oslo Beer', 13.95, 5.5),
  (3, 73513515, 'ipa sweden', 17.5, 8),
  (4, 73513516, 'eriksberg', 18, 7.4)
ON CONFLICT DO NOTHING;