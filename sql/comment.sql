
CREATE TABLE IF NOT EXISTS comment (
    comment TEXT NOT NULL,
    commenterPK TEXT NOT NULL,
    createdAt TEXT NOT NULL,
    parentCommentPK TEXT,
    pk TEXT NOT NULL PRIMARY KEY,
    postPK TEXT NOT NULL,
    FOREIGN KEY(commenterPK) REFERENCES user(pk),
    FOREIGN KEY(parentCommentPK) REFERENCES comment(pk),
    FOREIGN KEY(postPK) REFERENCES post(pk)
);

INSERT INTO comment (comment, commenterPK, createdAt, parentCommentPK, pk, postPK)
VALUES ('comment 1', 'userpk1', datetime('now'), null, 'commentpk1', 'postpk1');

INSERT INTO comment (comment, commenterPK, createdAt, parentCommentPK, pk, postPK)
VALUES ('comment 2', 'userpk2', datetime('now'), 'commentpk1', 'commentpk2', 'postpk1');

INSERT INTO comment (comment, commenterPK, createdAt, parentCommentPK, pk, postPK)
VALUES ('comment 3', 'userpk1', datetime('now'), null, 'commentpk3','postpk1');

-- UPDATE comment
-- SET comment='other comment 1'
-- WHERE pk == 'commentpk1';

-- SELECT comment, commenterPK, createdAt, parentCommentPK, pk, postPK
-- FROM comment
-- WHERE pk == 'commentpk1';

-- DELETE FROM comment
-- WHERE pk == 'commentpk1';

-- DROP TABLE IF EXISTS comment;

-- get all comments for a post,
-- and sort them by the date they were created
-- SELECT comment, commenterPK, createdAt, parentCommentPK, pk, postPK
-- FROM comment
-- WHERE postPK == 'postpk1'
-- ORDER BY createdAt DESC;
