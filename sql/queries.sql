-- get the user info with their password
SELECT
    user.email,
    user.name,
    password.password,
    user.pk
FROM user
INNER JOIN password
    ON user.pk == password.userPK;

-- get the user's password given their email
SELECT password.password
FROM user
INNER JOIN password
    ON user.pk == password.userPK
WHERE user.email == 'user_1@email.tld';
