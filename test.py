
# author : Omar MOSTAFA 
# numéro étudiant : 11811273

###  voici mes tentatives pour arriver au meilleur resultat :  ###            #! LE CODE FINAL TOUT EN BAS DECOMMENTÉ !#
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
## version 1 ##
#################################################################################################################################################
# import cv2
# import numpy as np

# # charger l'image
# image = cv2.imread('./puzzle.jpg')

# # convertir en échelle de gris
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# ## Ensuite, nous pouvons appliquer un filtre pour améliorer l'image :
# # Appliquer un filtre Gaussien pour réduire le bruit
# blur = cv2.GaussianBlur(gray, (5,5), 0)


# ## Ensuite, nous pouvons utiliser l'algorithme de segmentation Otsu pour segmenter l'image :
# # Segmenter l'image en utilisant l'algorithme d'Otsu
# ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# ## Ensuite, nous pouvons appliquer la morphologie mathématique pour supprimer les petites régions indésirables dans l'image :
# # Appliquer la morphologie mathématique pour éliminer les petites régions
# kernel = np.ones((3,3), np.uint8)
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)


# ## Ensuite, nous pouvons utiliser l'analyse en composantes connexes pour détecter les différentes pièces :
# # Détecter les contours
# contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # Dessiner les contours
# for i, contour in enumerate(contours):
#     # Ignorer les contours de petite taille
#     if cv2.contourArea(contour) < 100:
#         continue
#     # Dessiner le contour
#     cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)


# ## Enfin, nous pouvons afficher l'image résultante :
# # Afficher l'image résultante
# cv2.imshow('Resultat', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#################################################################################################################################################
## version 2 ##
#################################################################################################################################################
# import cv2
# import numpy as np

# # Chargement de l'image
# image = cv2.imread('puzzle.jpg')

# # Conversion de l'image en niveau de gris
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Réduction du bruit de l'image en appliquant un flou gaussien
# blur = cv2.GaussianBlur(gray, (5, 5), 0)

# # Création d'un masque binaire initial
# mask = np.zeros(blur.shape, dtype=np.uint8)

# # Définition des points de départ pour le contour actif
# points = np.array([[150, 100], [200, 50], [250, 100], [250, 200], [200, 250], [150, 200]], dtype=np.int32)

# # Création du contour actif
# snake = cv2.SnakeImage(gray, points, alpha=0.5, beta=0.1, gamma=0.01)

# # Itération de la méthode de contour actif pour ajuster le contour
# for i in range(100):
#     snake = cv2.SnakeImage(gray, snake, alpha=0.5, beta=0.1, gamma=0.01)

# # Dessin du contour sur le masque binaire
# cv2.drawContours(mask, [np.int32(snake)], 0, (255, 255, 255), -1)

# # Application d'une morphologie mathématique pour améliorer le masque binaire
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# # Application du masque binaire à l'image d'origine pour isoler les pièces de puzzle
# result = cv2.bitwise_and(image, image, mask=mask)

# # Affichage de l'image résultante
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#################################################################################################################################################
## version 3 ##
#################################################################################################################################################
# import cv2
# import numpy as np

# # Chargement de l'image et conversion en niveaux de gris
# image = cv2.imread("./puzzle.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Seuillage adaptatif pour binariser l'image
# thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# # Ajout de deux pixels de bordure au masque initial
# h, w = image.shape[:2]
# mask = np.zeros((h+2, w+2), np.uint8)

# # choix du point de départ pour le remplissage
# seed = (0, 0)

# # Remplissage de la région à l'aide de la méthode de remplissage par diffusion (flood-fill)
# cv2.floodFill(thresh, mask, seed, 255, 10, 10)

# # Suppression des pixels de bordure ajoutés précédemment
# region_mask = mask[1:-1, 1:-1]

# # Application d'une morphologie de fermeture pour améliorer la forme des pièces
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
# closed_mask = cv2.morphologyEx(region_mask, cv2.MORPH_CLOSE, kernel)

# # Identification des contours
# contours, _ = cv2.findContours(closed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Détection des pièces individuelles et dessin des contours
# for i, contour in enumerate(contours):
#     # Calcule le rectangle englobant minimum (minimum bounding rectangle)
#     rect = cv2.minAreaRect(contour)
#     box = np.int0(cv2.boxPoints(rect))

#     # Dessin des contours
#     cv2.drawContours(image, [box], 0, (0, 255, 0), 2)

# # # Affichage de l'image résultante
# # cv2.imshow("Résultat", image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# # Trouver les contours sur le masque

# contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Dessiner les contours sur l'image originale
# cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# # Afficher l'image avec les contours
# cv2.imshow("Contours", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#################################################################################################################################################
## version 4 ##
#################################################################################################################################################
# import cv2
# import numpy as np

# # Chargement de l'image
# image = cv2.imread('puzzle.jpg')

# # Définition des paramètres de segmentation
# seed_points = [(50, 50), (200, 200), (400, 400)] # Points de départ pour la croissance de région
# thresholds = [(50, 50, 50), (100, 100, 100), (150, 150, 150)] # Seuils de similarité pour chaque région

# # Création du masque binaire
# mask = np.zeros(image.shape[:2], dtype=np.uint8)

# # Itération sur chaque région pour appliquer la croissance de région
# for i in range(len(seed_points)):
#     # Définition du point de départ pour la croissance de région
#     seed = seed_points[i]

#     # Définition du seuil de similarité pour la région
#     threshold = thresholds[i]

#     # Création d'un masque binaire pour la région
#     region_mask = np.zeros(image.shape[:2], dtype=np.uint8)

#     # Application de la croissance de région pour la région
#     cv2.floodFill(image, region_mask, seed, 255, threshold, threshold)

#     # Ajout du masque binaire de la région au masque binaire global
#     mask |= region_mask

# # Application d'une morphologie mathématique pour améliorer le masque binaire
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# # Application du masque binaire à l'image d'origine pour isoler les pièces de puzzle
# result = cv2.bitwise_and(image, image, mask=mask)

# # Affichage de l'image résultante
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#################################################################################################################################################
## version 5 ##
#################################################################################################################################################
# import cv2
# import numpy as np

# # chargement de l'image
# image = cv2.imread('puzzle.jpg')

# # conversion en niveaux de gris
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # binarisation
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# # recherche des contours
# contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

# # calcul du contour le plus grand
# max_contour = max(contours, key=cv2.contourArea)

# # création d'un masque pour la région d'intérêt
# region_mask = np.zeros_like(thresh)
# cv2.drawContours(region_mask, [max_contour], 0, 255, -1)

# # extraction de la région d'intérêt
# roi = cv2.bitwise_and(image, image, mask=region_mask)

# # calcul de la couleur moyenne de la région d'intérêt
# mean_color = cv2.mean(image, mask=region_mask)[:3]
# print("Couleur moyenne de la région d'intérêt :", mean_color)

# # affichage des résultats
# cv2.imshow('image', image)
# cv2.imshow('thresh', thresh)
# cv2.imshow('roi', roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#################################################################################################################################################
## version 6 ##
#################################################################################################################################################
# import cv2
# import numpy as np

# # Charger l'image
# img = cv2.imread("puzzle.jpg")

# # Convertir en niveaux de gris
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Seuillage adaptatif
# thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# # Dilater l'image pour connecter les pièces de puzzle
# kernel = np.ones((3,3),np.uint8)
# dilation = cv2.dilate(thresh,kernel,iterations = 1)

# # Trouver les contours
# contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Dessiner les contours
# for contour in contours:
#     area = cv2.contourArea(contour)
#     if area > 1000:  # filtrer les petits contours
#         # Approximation de contours
#         epsilon = 0.02*cv2.arcLength(contour,True)
#         approx = cv2.approxPolyDP(contour,epsilon,True)
#         # Dessiner le contour
#         cv2.drawContours(img, [approx], 0, (0,255,0), 2)

# # Afficher l'image
# cv2.imshow("Contours", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################

### code final ###
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

import cv2
import numpy as np

# Charger l'image
image = cv2.imread("puzzle.jpg")

# Convertir en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un flou gaussien
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Binariser l'image
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Appliquer une opération de dilatation pour relier les parties disjointes de chaque pièce
kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations=2)

# Trouver les contours des pièces
contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner un rectangle autour de chaque contour détecté
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Afficher l'image résultante
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
