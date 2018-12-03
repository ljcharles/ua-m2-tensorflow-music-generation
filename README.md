# ua-m2-tensorflow-music-generation
En utilisant, un RNN (réseau de neurones récurrents), je vais générer de la musique du style du groupe ‘The Chainsmokers’ c’est-à-dire de la musique POP.  

Les instructions au fonctionnement de ce projet se trouve dans le fichier Rapport TP1.

## Pour lancer le projet :
### 1) Gérer les dépendances 
Tout d’abord, il faut télécharger le paquet MIDI qui autorise la modification des fichiers .midi dans Python avec la commande suivante :  
```bash
pip install git+https://github.com/vishnubob/python−midi@feature/python3 
```  
Puis il faut s'assurer d'avoir Tensorflow (import tensorflow)  
Si vous n'avez pas Tensorflow pas de panique :)  
Solution 1) Utiliser Anaconda et taper la commande suivante : ```bash conda install tensorflow```   
Solution 2) Télécharger [WinPython 3.6](https://sourceforge.net/projects/winpython/files/WinPython_3.6/3.6.7.0/WinPython64-3.6.7.0Qt5.exe/download") et taper la commande suivante dans le WinPython Command Prompt : ```bash pip install tensorflow```  

### 2) Modifier les chemins d'accès aux fichiers avec des chemins absolus
J’ai utilisé une version de python 🐍  portable (version 3.6) sur Windows avec Tensorflow sur ma clé USB pour les tests. Donc, pour faire fonctionner le projet, il faut modifier les chemins d’accès aux fichiers :

#### Le dossier d'accès à la musique générée
À la ligne 112 du fichier main.py :  𝑛𝑜𝑡𝑒𝑆𝑡𝑎𝑡𝑒𝑀𝑎𝑡𝑟𝑖𝑥𝑇𝑜𝑀𝑖𝑑𝑖 (𝑔𝑒𝑛_𝑠𝑜𝑛𝑔,𝑛𝑎𝑚𝑒 = "𝐸:\𝑊𝑃𝑦3670\𝑃𝑟𝑜𝑗𝑒𝑡\𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑\𝑔𝑒𝑛_𝑠𝑜𝑛𝑔_0")
#### Le dossier d'accès aux musiques 
À la ligne 6 du fichier create_dataset.py : 𝑠𝑜𝑛𝑔𝑠 = 𝑔𝑙𝑜𝑏.𝑔𝑙𝑜𝑏 (𝑟′𝐸:\𝑊𝑃𝑦3670\𝑃𝑟𝑜𝑗𝑒𝑡\𝑢𝑡𝑖𝑙\𝑑𝑎𝑡𝑎\∗.𝑚𝑖𝑑 ∗ ′) 

### 3) Lancer le fichier main.py (python main.py)

### 4) Écouter la musique générée en fichier .midi dans le dossier generated avec le lecteur Windows Media Player de Windows

### 5) Optionnel : Convertir le fichier midi en mp3 avec la commande suivante :
```bash
𝑓𝑓𝑚𝑝𝑒𝑔 − 𝑖 "𝐸:\𝑊𝑃𝑦3670\𝑃𝑟𝑜𝑗𝑒𝑡\𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑\𝑔𝑒𝑛_𝑠𝑜𝑛𝑔_0.𝑚𝑖𝑑" − 𝑣𝑛 − 𝑎𝑟 44100 − 𝑎𝑐 2 − 𝑎𝑏 192𝑘 − 𝑓 𝑚𝑝3 "𝐸:\𝑊𝑃𝑦3670\𝑃𝑟𝑜𝑗𝑒𝑡\𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑\𝑜𝑢𝑡𝑝𝑢𝑡.𝑚𝑝3"
```  

Juste au cas où si ce problème intervient pour vous (Unknown Meta MIDI Event) :  
Voici la solution https://github.com/vishnubob/python-midi/issues/33
