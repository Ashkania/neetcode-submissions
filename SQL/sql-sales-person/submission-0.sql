-- Write your query below.
select name from sales_person sp
where sp.sales_id not in(
    select sp.sales_id from sales_person sp
    left join orders o on sp.sales_id = o.sales_id
    inner join company c on c.com_id = o.com_id
    and c.name = 'CRIMSON'
)