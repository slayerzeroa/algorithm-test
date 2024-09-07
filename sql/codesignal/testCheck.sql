-- https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/NEmMmhyncr4X4ZHbh

CREATE PROCEDURE solution()
    SELECT id, IF (given_answer IS NULL, 'no answer', IF (given_answer=correct_answer, 'correct', 'incorrect')) AS checks
    FROM answers
    ORDER BY id;