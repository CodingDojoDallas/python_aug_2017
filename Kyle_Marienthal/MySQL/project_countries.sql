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
