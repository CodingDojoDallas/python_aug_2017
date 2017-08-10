SELECT 
	languages.id as language_id,
	languages.language,
	languages.percentage,
    countries.id as country_id,
    countries.name
FROM languages
JOIN countries ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;



SELECT
	count(countries.id) as num_cities,
	countries.id as country_pk,
	countries.name
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id;



SELECT
	cities.id as city_pk,
    cities.name,
    cities.population,
    countries.id as country_pk,
    countries.name as country_name
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;


SELECT
	languages.id as language_pk,
    languages.language, 
    languages.percentage,
    countries.id as country_pk,
    countries.name
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT 
	countries.id,
	countries.name,
    countries.surface_area,
    countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;


SELECT
	countries.id,
    countries.name,
    countries.life_expectancy,
    countries.government_form,
    countries.capital
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy'
AND countries.life_expectancy > 75
AND countries.capital > 200
ORDER BY countries.capital DESC;



SELECT
	countries.id as country_pk,
	countries.name,
    cities.id as city_id,
    cities.name,
    cities.district,
    cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' 
AND cities.district = 'Buenos Aires'
AND cities.population > 500000;


SELECT
    countries.region,
    COUNT(countries.region) as num_countries
FROM countries
GROUP BY countries.region;