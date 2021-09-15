
CREATE TABLE IF NOT EXISTS post (
    authorPK TEXT NOT NULL,
    content TEXT NOT NULL,
    createdAt TEXT NOT NULL,
    pk TEXT NOT NULL PRIMARY KEY,
    title TEXT NOT NULL,
    FOREIGN KEY(authorPK) REFERENCES user(pk)
);

INSERT INTO post (authorPK, content, createdAt, pk, title)
VALUES ('userpk1', 'post content 1', datetime('now'), 'postpk1', 'post title 1');

INSERT INTO post (authorPK, content, createdAt, pk, title)
VALUES ('userpk1', 'post content 2', datetime('now'), 'postpk2', 'post title 2');

-- UPDATE post
-- SET title='other post title 1', content='other post content 1'
-- WHERE pk == 'postpk1';

-- SELECT authorPK, content, createdAt, pk, title
-- FROM post
-- WHERE pk == 'postpk1'
-- ORDER BY createdAt DESC;

-- DELETE FROM post
-- WHERE pk == 'postpk1';

-- DROP TABLE IF EXISTS post;

-- get all posts made by a user,
-- and sort them by the date they were created
-- SELECT authorPK, content, createdAt, pk, title
-- FROM post
-- WHERE authorPK == 'userpk1'
-- ORDER BY createdAt DESC;
