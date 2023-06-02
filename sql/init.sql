INSERT INTO beers (id, beer_id, name, price, alcohol_percentage)
VALUES
  (1, 73513513, 'Stockholm Beer', 12.95, 5.0),
  (2, 73513514, 'Oslo Beer', 13.95, 5.5),
  (3, 73513515, 'Ipa sweden', 17.5, 8),
  (4, 73513516, 'Eriksberg', 18.3, 7.4),
  (5, 73513517, 'Estrella', 17, 6.6),
  (6, 73513518, 'Flat tire', 22.5, 9),
  (7, 73513519, 'Corona', 20, 6.8),
  (8, 73513520, 'Marisatd', 21, 8),
  (9, 73513521, 'Heiniken', 14, 10.5),
  (10, 73513522, 'Falcon', 9, 3.5)
ON CONFLICT DO NOTHING;