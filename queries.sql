-- Задания на дом по SQL
-- Студент: Бакун А.И
-- Дата: 29.09.202

-- 1
SELECT название, цена FROM Товар ORDER BY цена DESC LIMIT 1;
-- 2
SELECT название, цена FROM Товар ORDER BY цена ASC LIMIT 1;
-- 3
SELECT название, цена FROM Товар WHERE жанр = 'Фантастика';
-- 4
SELECT название, цена FROM Товар WHERE название LIKE '%о%';
-- 5
SELECT id, дата, клиент, товар_id, количество FROM Заказ;
-- 6
SELECT * FROM Заказ WHERE клиент = 'Иванов Иван Иванович';
-- 7 
SELECT Заказ.дата, Заказ.клиент, Товар.название, Заказ.количество 
FROM Заказ 
JOIN Товар ON Заказ.товар_id = Товар.id;
-- 8
SELECT SUM(Товар.цена * Заказ.количество) 
FROM Заказ 
JOIN Товар ON Заказ.товар_id = Товар.id;
--9 
SELECT клиент, COUNT(*) as Количество_заказов 
FROM Заказ 
GROUP BY клиент;
-- 10
SELECT название, цена 
FROM Товар 
WHERE цена > (SELECT AVG(цена) FROM Товар);