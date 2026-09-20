-- Write your query below
select c.customer_id, c.customer_name
from customers c natural join orders o
group by c.customer_id, c.customer_name
having string_agg(o.product_name, ',') like '%A%'
and string_agg(o.product_name, ',') like '%B%'
and string_agg(o.product_name, ',') not like '%C%'
order by c.customer_name