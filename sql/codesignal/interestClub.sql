-- https://app.codesignal.com/arcade/db/specialties/nhGPHWsjFoLb3A4AJ/solutions?solutionId=t8Zgue33qhDWdkjmB

CREATE PROCEDURE solution()
    SELECT name
    FROM people_interests
    WHERE interests && interests LIKE "%reading%" AND interests && interests LIKE "%drawing%"
    ORDER BY name