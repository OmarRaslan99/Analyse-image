# Puzzle solver
## Démarche utilisée
1. Charger l'image
2. Convertir l'image en niveaux de gris
3. Appliquer un flou gaussien pour réduire le bruit
4. Binariser l'image en utilisant la méthode d'OTSU
5. Appliquer une opération de dilatation pour relier les parties disjointes de chaque pièce
6. Trouver les contours des pièces en utilisant la méthode RETR_EXTERNAL
7. Dessiner un rectangle autour de chaque contour détecté
8. Afficher l'image résultante

## Justification des choix d'algorithmes
Les traitements utilisés ont été choisis pour leur efficacité dans la détection de contours et la séparation des différentes pièces de puzzle.

La conversion en niveaux de gris permet de réduire l'information de l'image et de faciliter la détection de contours. Le flou gaussien permet de réduire le bruit et d'éviter des détections de contours erronées. La binarisation de l'image en utilisant la méthode d'OTSU permet de trouver le seuil de binarisation optimal pour la segmentation de l'image.

L'opération de dilatation permet de relier les parties disjointes de chaque pièce de puzzle en une seule entité. La méthode RETR_EXTERNAL permet de détecter uniquement les contours externes des pièces de puzzle.

Le dessin de rectangles autour de chaque contour détecté permet de visualiser chaque pièce de puzzle et de faciliter leur identification.

## Paramètres des algorithmes
Les paramètres des différents algorithmes ont été fixés par des tests empiriques pour obtenir les meilleurs résultats.

Le flou gaussien a été appliqué avec un noyau de taille (5, 5). L'opération de dilatation a été réalisée avec un noyau de taille (3, 3) et deux itérations. Le seuil de binarisation optimal a été déterminé par la méthode d'OTSU.

## Tentatives et difficultés rencontrées
Plusieurs tentatives ont été réalisées pour obtenir les meilleurs résultats. Les difficultés rencontrées étaient principalement liées à la détection précise des contours de chaque pièce de puzzle.

La première tentative consistait à appliquer une opération de seuillage adaptatif pour binariser l'image. Cependant, cette méthode ne permettait pas de bien distinguer les contours de chaque pièce de puzzle.

Une deuxième tentative consistait à appliquer une opération de gradient morphologique pour détecter les contours de chaque pièce de puzzle. Cette méthode permettait de bien distinguer les contours mais elle ne permettait pas de relier les parties disjointes de chaque pièce. 
(regardez tentative.png)

Une troisième tentative consistait à utiliser la méthode Canny pour détecter les contours de chaque pièce de puzzle. Cette méthode était efficace mais elle détectait des contours erronés.

Finalement, la méthode retenue consiste à appliquer un flou gaussien suivi d'une binarisation en utilisant la méthode d'OTSU. Une opération de dilatation est ensuite appliquée pour relier les parties disjointes de chaque pièce de puzzle. Les contours sont détectés en utilisant la méthode RETR_EXTERNAL et des rectangles sont dessinés autour de chaque contour détecté pour identifier chaque pièce de puzzle.

## Le resultat final
Le résultat final de l'algorithme est l'image originale avec des rectangles verts dessinés autour de chaque contour détecté. Cependant, il y a plusieurs contours pour chaque pièce de puzzle, et plus il y a de couleurs différentes dans une pièce, plus le contour peut ne pas être précis. Cela est dû à l'application de la méthode de seuillage pour binariser l'image, ce qui peut causer une perte de certaines informations de couleur. De plus, l'application d'une opération de dilatation peut relier certaines parties disjointes des pièces, mais cela peut également fusionner des pièces voisines, ce qui peut affecter la précision des contours.
(regardez resultat_final.png)

#### Nom : MOSTAFA
#### Prenom : Omar
#### Numéro étudiant : 11811273
