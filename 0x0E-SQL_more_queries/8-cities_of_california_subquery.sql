-- select data in califonia
SELECT * FROM cities WHERE state.id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
