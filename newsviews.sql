create view bad_days as
	select date_trunc('day', time), max(errors.error) / cast(count(*) as float) * 100 as percent
	from log join
		(select count(*) as error, date_trunc('day', time) as day
			from log
			where status != '200 OK'
			group by day) as errors
	on date_trunc('day', time) = errors.day
	group by date_trunc('day', time)
	order by percent desc;

create view top_articles as
	select articles.title, count(log.path) as hits
	from articles join log
	on log.status = '200 OK'
	and log.method = 'GET'
	and log.path like concat('%', articles.slug)
	group by articles.title
	order by hits desc;

create view top_authors as
	select authors.name, count(log.path) as hits
	from (articles join log on
		log.status = '200 OK' and
		log.method = 'GET' and
		log.path like
		concat('%', articles.slug))
	join authors
	on articles.author = authors.id
	group by authors.name
	order by hits desc;
