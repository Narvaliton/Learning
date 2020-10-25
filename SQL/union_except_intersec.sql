--UNION permet ici d'afficher tout les tuples des 2 tables intermediary ET entity
SELECT name, id_address FROM intermediary
UNION
SELECT name, id_address FROM entity

--EXCEPT permet ici d'afficher tout les tuples de la table entity n'étant pas présent dans la table intermediary
SELECT name, id_address FROM entity
EXCEPT
SELECT name, id_address FROM intermediary

