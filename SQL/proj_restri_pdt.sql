--Projection
SELECT * FROM entity --Affiche tout les tuples de la table entity
SELECT DISTINCT * FROM entity --Affiche les tuples uniques, c'est à dire si 2 tuples sont présent en double dans la BD alors un seul sera affiché
SELECT id, name, status FROM entity ; --Affiche les attributs id, name et status de la table entity

--Restriction
SELECT * FROM entity WHERE name = 'Big Data Crunchers Ltd.'; --Affiche tout les attributs des tuples de la table entity dont l'attribut name a pour valeur 'Big Data Crunchers Ltd.'
SELECT * FROM entity WHERE id >= 5000;
SELECT id, name FROM entity WHERE name in ('HUGH POWER LIMITED','Wagadougou', 'Ahbon?', 'Une société') --Affiche les attribut id et name
-- de la table entity pour les tuples dont l'attribut name a pour valeur une des suites de caractère listées
SELECT * FROM entity WHERE (id < 5000 or  name in ('HUGH POWER LIMITED','Wagadougou', 'Ahbon?', 'Une société'))
SELECT address FROM address
WHERE countries NOT('HKG') --Affiche l'attribut address de tout les tuples de la table address dont l'attribut countries n'est pas égale à HKG

--Produit Cartésien
SELECT * FROM entity, address ; --Affiche tout les attributs de toutes les combinaisons possibles entres toutes les lignes des 2 tables
SELECT 'On projette', 'des attributs', "d'aucune table" --Affiche un tuple dont les valeurs et les attributs seront ceux listés après le SELECT

SELECT id * 2, name, status FROM entity ; --On peut appliquer des fonctions aux valeurs des attributs
SELECT ABS( (- id) *2 ) AS calcul_bizarre, name, status FROM entity ; --Grace au mot clé AS on peut renommer une colonne 
SELECT name || '(' || status || ')' AS name_and_status FROM entity ; --On peut ajouter grâce à la fonction || dessuite de caractère ou d'autres attributs
SELECT CURRENT_DATE() > incorporation_date FROM entity ; --CURRENT_DATE renvoit la date actuelle