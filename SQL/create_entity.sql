CREATE TABLE entity ( --Création d'une table entity
    id INTEGER,
    name TEXT NOT NULL,  --La valeur de l'attribut name doit être non NULL, donc renseignée
    jurisdiction TEXT,
    jurisdiction_description TEXT,
    company_type TEXT,
    id_address INTEGER,
    incorporation_date DATE,
    inactivation_date DATE,
    status TEXT,
    service_provider TEXT,
    country_codes TEXT,
    countries TEXT,
    source TEXT,
    PRIMARY KEY(id), --On definit la clé primaire comme l'attribut id
    FOREIGN KEY(id_address) REFERENCES address(id) --On déclare que l'attribut id_address de la table entity fait réference ) la colonne id de la table adress
)