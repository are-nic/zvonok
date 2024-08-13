SELECT a.* from article a
LEFT JOIN comment c ON a.id = c.article_id
WHERE c.article_id IS NULL;