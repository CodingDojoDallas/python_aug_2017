SELECT 
	customer.customer_id,
	customer.first_name,
    customer.last_name,
    customer.email,
    address.address,
    address.city_id
FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE address.city_id = 312;

SELECT
	category.name,
    category.category_id,
    film_category.category_id,
    film.film_id,
    film.title,
    film.description,
    film.release_year,
    film.rating,
    film.special_features
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

