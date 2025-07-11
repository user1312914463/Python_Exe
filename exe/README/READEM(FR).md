Compilateur Python vers exe

Introduction:
Python to exe compiler est un outil simple et facile à utiliser qui permet aux utilisateurs de compiler des scripts Python en exécutables indépendants (exe). L'outil fournit une interface utilisateur graphique intuitive (Gui) qui facilite le choix des fichiers Python, des répertoires de sortie, des fichiers d'icônes et définit les options de compilation. Dans le même temps, un mécanisme de vérification des clés a été ajouté pour assurer la sécurité et autoriser l'utilisation de l'outil.
Caractéristiques fonctionnelles
Vérification de la clé: Avant d'utiliser l'outil, vous devez entrer une clé valide pour la vérification, en vous assurant que seuls les utilisateurs autorisés peuvent l'utiliser.
Interface utilisateur graphique: fournit une interface graphique intuitive pour faciliter la sélection des fichiers et la configuration des options de compilation.
Paramètres des options de compilation: plusieurs options de compilation telles que le mode fichier unique, le mode fenêtre, le mode débogage sont prises en charge.
Configuration de l'enregistrement et du chargement: les utilisateurs peuvent enregistrer et charger les paramètres compilés pour une utilisation ultérieure.
Sortie du journal en temps réel: pendant le processus de compilation, le journal de compilation est publié en temps réel, ce qui facilite le suivi de la progression de la compilation par l'utilisateur.

Installation et dépendances
Dépendances:
Python 3.x
Pyinstaller: utilisé pour compiler des scripts Python en fichiers exe.
Étapes d'installation
Assurez - vous que Python 3.x est déjà installé et peut être téléchargé et installé à partir du site officiel de Python.
Installez pyinstaller: Ouvrez le terminal de ligne de commande et exécutez la commande suivante:
pip install pyinstaller

Cloner ou télécharger ce code projet localement.

Méthode d'utilisation (lancer le programme):
Ouvrez le terminal de ligne de commande et accédez au Répertoire racine du projet.
Exécutez la commande suivante pour démarrer le programme:
python main.py

Vérification des clés:
Lorsque vous démarrez le programme pour la première fois, une fenêtre de vérification de clé apparaît.
Entrez une clé valide et cliquez sur le bouton "valider" pour valider.
Si la vérification réussit, le programme démarre automatiquement; Si la vérification échoue, une invite correspondante est donnée en fonction du nombre de tentatives restantes et le nombre d'erreurs dépassant la limite Verrouille le fichier clé.

Paramètres de compilation:
Fichiers Python: cliquez sur le bouton "parcourir..." pour sélectionner les fichiers Python à compiler.
Répertoire de sortie: cliquez sur le bouton "parcourir..." pour sélectionner le Répertoire de sortie du fichier exe compilé.
Fichier d'icônes (facultatif): cliquez sur le bouton "parcourir..." pour sélectionner le fichier d'icônes (avec l'extension.Ico) que vous souhaitez définir pour le fichier exe.
Options de compilation:
Mode fichier unique: Empaquetez toutes les dépendances dans un fichier exe séparé.
Mode fenêtre (sans console): le fichier exe compilé s'exécute sans afficher la fenêtre de la console.
Mode de débogage: activer le mode de débogage pour faciliter le processus de compilation de débogage.
Nettoyer les fichiers temporaires: nettoie les fichiers temporaires une fois la compilation terminée.
Encodage de la console: Sélectionnez le format d'encodage de la sortie de la console.
Sauvegarder et charger les paramètres
Enregistrer les paramètres: cliquez sur le bouton "enregistrer les paramètres" pour enregistrer les paramètres de compilation actuels dans le fichier Py - to - Exe - config.json.
Charger les paramètres: cliquez sur le bouton "charger les paramètres" pour charger les paramètres compilés précédemment enregistrés à partir du fichier Py - to - Exe - config.json.
Commencer la compilation
Une fois les paramètres de compilation terminés, appuyez sur le bouton "démarrer la compilation" et le programme commencera le processus de compilation.
Pendant la compilation, le journal de compilation est affiché en temps réel dans la zone Journal, tandis que la barre de progression affiche la progression de la compilation.
Une fois la compilation terminée, la boîte d'invite correspondante apparaît pour informer le résultat de la compilation.

Structure du fichier:
plaintext:
exe/
█ - - main.py █ point d'entrée du programme
► - - key @ verification.py ► module de vérification des clés
├ - - Compiler @ gui.py \ Editor traduire le module d'interface
├ - - compilation @ engine.py \ compile le module du moteur
├ - - config-manager.py \ module de gestion de configuration
- ressources /
│└ - - keys.json \ \ fichier de configuration de la clé
├ - - Py - to - Exe - config.json ├ compiler les paramètres pour enregistrer le fichier

! ATTENTION!
Assurez - vous que la clé saisie est valide, sinon vous risquez de ne pas utiliser l'outil correctement.
Le processus de compilation peut prendre un certain temps, en fonction de la complexité du script Python et des performances du système.
Si vous rencontrez des problèmes lors de la compilation, vérifiez la sortie du journal pour la vérifier en fonction des informations d'erreur.
Contributions et feedback
Si vous avez trouvé un bug ou si vous avez des suggestions d'amélioration, ajoutez QQ: 1312914463. Vous êtes également invités à partager votre expérience d'utilisation et à proposer de nouvelles fonctionnalités.