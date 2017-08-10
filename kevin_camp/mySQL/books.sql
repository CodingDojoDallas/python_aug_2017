USE books;
SELECT * FROM books;
INSERT INTO books (title, author, created_at, updated_at) VALUES ('A Confederacy of Dunces', 'John Kennedy Toole', NOW(), NOW());
SELECT * FROM books;
INSERT INTO books (title, author, created_at, updated_at) VALUES ('Cat in the Hat', 'Dr.Suess', NOW(), NOW());
SELECT * FROM books;
DELETE FROM books WHERE id = 2;
SELECT * FROM books;