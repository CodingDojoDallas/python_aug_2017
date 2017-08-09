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

SELECT
	actor.actor_id,
    actor.first_name,
    actor.last_name,
    film.title,
    film.film_id,
    film.description,
    film.release_year
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5;

SELECT
	customer.first_name,
    customer.last_name,
    customer.email,
    customer.address_id,
    customer.store_id,
    city.city_id
FROM customer
join address ON customer.address_id = address.address_id
join city ON city.city_id = address.city_id
where customer.store_id = 1 and city.city_id in (1,42,312,459);

SELECT
	film.title,
    film.description,
    film.release_year,
    film.rating,
    film.special_features
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
where film.rating = 'G' and actor.actor_id = 15 and film.special_features like '%behind the scenes%';

SELECT
	film_actor.film_id,
	actor.first_name,
    actor.last_name,
    actor.last_update
from actor
join film_actor on actor.actor_id = film_actor.actor_id
where film_id = 369;

select
	film.rental_rate,
	film.title,
    film.description,
    film.release_year,
    film.rating,
    film.special_features,
    category.name    
from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where film.rental_rate = 2.99 and category.name = 'drama';

select
	film.title,
    film.description,
    film.release_year,
    film.rating,
    film.special_features,
    category.name,
    actor.first_name,
    actor.last_name
from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
where category.name = 'action' and actor.first_name = 'Sandra' and actor.last_name = 'Kilmer'