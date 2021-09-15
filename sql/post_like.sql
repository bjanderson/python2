
CREATE TABLE IF NOT EXISTS post_like (
    postPK TEXT NOT NULL,
    userPK TEXT NOT NULL,
    FOREIGN KEY(postPK) REFERENCES post(pk) ON DELETE CASCADE,
    FOREIGN KEY(userPK) REFERENCES user(pk),
    PRIMARY KEY(postPK, userPK)
);

INSERT INTO post_like (postPK, userPK)
VALUES ('postpk1', 'userpk1');

INSERT INTO post_like (postPK, userPK)
VALUES ('postpk1', 'userpk2');

INSERT INTO post_like (postPK, userPK)
VALUES ('postpk1', 'userpk3');

INSERT INTO post_like (postPK, userPK)
VALUES ('postpk2', 'userpk1');

SELECT postPK, userPK FROM post_like;

-- DELETE FROM post_like
-- WHERE postPK == 'postpk1' AND userPK == 'userpk1';

-- DROP TABLE IF EXISTS post_like;

-- count how many likes all posts have
SELECT postPK, COUNT(DISTINCT userPK) as num_likes
FROM post_like
GROUP BY postPK;

-- count how many likes a post has
SELECT postPK, COUNT(DISTINCT userPK) as num_likes
FROM post_like
WHERE postPK = 'postpk1';
