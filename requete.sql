-- Afficher les noms et descriptions de tous les produits
SELECT `nom_p`, `descrip_p` FROM `produits`;

-- Afficher tous les meubles qui sont abandonnés
SELECT * FROM `produits` WHERE abandon_p = 1;

-- Effacer le Bo Meuble de brest
DELETE FROM `clients` WHERE `raison_c`='Bo Meuble' AND `ville_c`='Brest';

-- Il y a une erreur sur le nom du meuble Apfelgluk, il faut le réécrire Apfelgluck
UPDATE `produits` SET `nom_p`='Apfelgluck' WHERE `nom_p`='Apfelgluk';

-- Ajouter un nouveau client : Tout à la maison, Place Terreaux, Lyon
INSERT INTO `clients`(`raison_c`, `adresse_c`, `ville_c`, `pays_c`) VALUES ('Tout à la maison', 'Place Terreaux', 'Lyon', 'France');

-- Ajouter une nouvelle facture pour le tout à la maison de Lyon, enregistré le 28/08/2018, à 18h. La commande est composé de 18 Naess
INSERT INTO `factures`(`date_f`, `c_id`, `numero_f`)
SELECT '2018-08-28 18:00:00', id_c, 'MSQ232'
FROM clients
WHERE raison_c = 'Tout à la maison' AND ville_c = 'Lyon';
INSERT INTO `commandes`(`id_p`, `quantite_co`, `id_f`)
SELECT id_p, 18, id_f
FROM produits, factures
WHERE nom_p = 'Naess' AND numero_f = 'MSQ232';

-- Retrouver tous les meubles achetés par le Bo Meuble de Paris
SELECT *
FROM `produits`
WHERE id_p IN
    (SELECT id_p
    FROM commandes
    WHERE id_f IN
        (SELECT id_f
        FROM factures
        WHERE c_id IN
            (SELECT id_c
            FROM clients
            WHERE raison_c = "Bo Meuble" AND ville_c = "Paris")
        )
    );

-- Retrouver toutes les factures enregistrée depuis le 1er juillet 2018
SELECT `numero_f`, `date_f`  FROM `factures` WHERE `date_f` < '2018-07-01';