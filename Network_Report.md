# 🛡️ Rapport global de sécurité réseau

## 1. Menace critique : attaque SSH ciblée
L’outil a identifié un schéma d’attaque multi-étapes provenant de `192.168.190.130` :
- 🟠 **Test de connexion** : le port `192.168.190.130.50019` a généré **4 paquets** (vérification de service).
- 🔴 **Assaut principal** : le port `192.168.190.130.50245` a généré **60 paquets**. Activité de force brute confirmée.
- 🟠 **Test de connexion** : le port `BP-Linux8.43717` a généré **6 paquets** (vérification de service).
- 🟠 **Test de connexion** : le port `BP-Linux8.34621` a généré **6 paquets** (vérification de service).
- 🟡 **Sonde discrète** : le port `192.168.190.130.50374` a généré **2 paquets**.

## 2. Autres anomalies détectées
- ⚠️ **Scan de ports** : l’hôte a sondé **135** ports différents. Activité de reconnaissance détectée.
- ⚠️ **Flood ICMP** : 84 paquets Ping détectés. Risque potentiel de saturation réseau.
- ⚠️ **Volume de trafic élevé** : 11016 paquets analysés au total. Risque possible de déni de service (DoS).

## 3. Échantillon de trafic et interprétation
| Horodatage | Source | Signification du drapeau | Résumé technique |
| :--- | :--- | :--- | :--- |
| 15:34:04.766656 | BP-Linux8.ssh | **Transfert de données (PUSH-ACK)** | Flags [P.], seq 2243505564:2243505672, ack 1972915080, ... |
| 15:34:04.766694 | BP-Linux8.ssh | **Transfert de données (PUSH-ACK)** | Flags [P.], seq 108:144, ack 1, win 312, options [nop,n... |
| 15:34:04.766723 | BP-Linux8.ssh | **Transfert de données (PUSH-ACK)** | Flags [P.], seq 144:252, ack 1, win 312, options [nop,n... |
| 15:34:04.766744 | BP-Linux8.ssh | **Transfert de données (PUSH-ACK)** | Flags [P.], seq 252:288, ack 1, win 312, options [nop,n... |
| 15:34:04.785366 | 192.168.190.130.50019 | **Accusé de réception (ACK)** | Flags [.], ack 108, win 7319, options [nop,nop,TS val 3... |
| 15:34:04.785384 | 192.168.190.130.50019 | **Accusé de réception (ACK)** | Flags [.], ack 144, win 7318, options [nop,nop,TS val 3... |
| 15:34:04.785406 | 192.168.190.130.50019 | **Accusé de réception (ACK)** | Flags [.], ack 252, win 7316, options [nop,nop,TS val 3... |
| 15:34:04.785454 | 192.168.190.130.50019 | **Accusé de réception (ACK)** | Flags [.], ack 288, win 7320, options [nop,nop,TS val 3... |
| 15:34:05.768334 | BP-Linux8.58466 | **Autre protocole** | 16550+ PTR? 130.190.168.192.in-addr.arpa. (46)... |
| 15:34:05.769075 | ns1.lan.rt.domain | **Autre protocole** | 16550 NXDomain 0/1/0 (112)... |
| 15:34:06.669393 | 192.168.190.130.50245 | **Transfert de données (PUSH-ACK)** | Flags [P.], seq 1601828178:1601828214, ack 1851233244, ... |
| 15:34:06.669906 | BP-Linux8.ssh | **Transfert de données (PUSH-ACK)** | Flags [P.], seq 1:37, ack 36, win 291, options [nop,nop... |
| 15:34:06.679262 | BP-Linux8.53220 | **Autre protocole** | 54801+ A? lacampora.org. (31)... |
| 15:34:06.679971 | ns1.lan.rt.domain | **Autre protocole** | 54801 1/0/0 A 184.107.43.74 (47)... |
| 15:34:06.681188 | BP-Linux8.ssh | **Transfert de données (PUSH-ACK)** | Flags [P.], seq 37:153, ack 36, win 291, options [nop,n... |
| 15:34:06.681222 | BP-Linux8.ssh | **Transfert de données (PUSH-ACK)** | Flags [P.], seq 153:189, ack 36, win 291, options [nop,... |
| 15:34:06.681248 | 190-0-175-100.gba.solunet.com.ar.2465 | **Requête de connexion (SYN)** | Flags [S], seq 326991629:326991749, win 512, length 120... |
| 15:34:06.681274 | 190-0-175-100.gba.solunet.com.ar.2466 | **Requête de connexion (SYN)** | Flags [S], seq 920517760:920517880, win 512, length 120... |
| 15:34:06.681294 | 190-0-175-100.gba.solunet.com.ar.2467 | **Requête de connexion (SYN)** | Flags [S], seq 556803824:556803944, win 512, length 120... |
| 15:34:06.681312 | 190-0-175-100.gba.solunet.com.ar.2468 | **Requête de connexion (SYN)** | Flags [S], seq 1921632185:1921632305, win 512, length 1... |
| 15:34:06.681328 | 190-0-175-100.gba.solunet.com.ar.2469 | **Requête de connexion (SYN)** | Flags [S], seq 1170972654:1170972774, win 512, length 1... |
| 15:34:06.681345 | 190-0-175-100.gba.solunet.com.ar.2470 | **Requête de connexion (SYN)** | Flags [S], seq 754504426:754504546, win 512, length 120... |
| 15:34:06.681362 | 190-0-175-100.gba.solunet.com.ar.2471 | **Requête de connexion (SYN)** | Flags [S], seq 669863147:669863267, win 512, length 120... |
| 15:34:06.681379 | 190-0-175-100.gba.solunet.com.ar.2472 | **Requête de connexion (SYN)** | Flags [S], seq 1036593434:1036593554, win 512, length 1... |
| 15:34:06.681396 | 190-0-175-100.gba.solunet.com.ar.2473 | **Requête de connexion (SYN)** | Flags [S], seq 473640609:473640729, win 512, length 120... |
| 15:34:06.681413 | 190-0-175-100.gba.solunet.com.ar.2474 | **Requête de connexion (SYN)** | Flags [S], seq 294639309:294639429, win 512, length 120... |
| 15:34:06.681430 | 190-0-175-100.gba.solunet.com.ar.2475 | **Requête de connexion (SYN)** | Flags [S], seq 2003734750:2003734870, win 512, length 1... |
| 15:34:06.681446 | 190-0-175-100.gba.solunet.com.ar.2476 | **Requête de connexion (SYN)** | Flags [S], seq 943277646:943277766, win 512, length 120... |
| 15:34:06.681463 | 190-0-175-100.gba.solunet.com.ar.2477 | **Requête de connexion (SYN)** | Flags [S], seq 612921749:612921869, win 512, length 120... |
| 15:34:06.681480 | 190-0-175-100.gba.solunet.com.ar.2478 | **Requête de connexion (SYN)** | Flags [S], seq 1079269685:1079269805, win 512, length 1... |
| 15:34:06.681497 | 190-0-175-100.gba.solunet.com.ar.2479 | **Requête de connexion (SYN)** | Flags [S], seq 1427118982:1427119102, win 512, length 1... |
| 15:34:06.681514 | 190-0-175-100.gba.solunet.com.ar.2480 | **Requête de connexion (SYN)** | Flags [S], seq 1481846896:1481847016, win 512, length 1... |
| 15:34:06.681531 | 190-0-175-100.gba.solunet.com.ar.2481 | **Requête de connexion (SYN)** | Flags [S], seq 807245684:807245804, win 512, length 120... |
| 15:34:06.681548 | 190-0-175-100.gba.solunet.com.ar.2482 | **Requête de connexion (SYN)** | Flags [S], seq 29032482:29032602, win 512, length 120: ... |
| 15:34:06.681564 | 190-0-175-100.gba.solunet.com.ar.2483 | **Requête de connexion (SYN)** | Flags [S], seq 2121432424:2121432544, win 512, length 1... |
| 15:34:06.681581 | 190-0-175-100.gba.solunet.com.ar.2484 | **Requête de connexion (SYN)** | Flags [S], seq 266983944:266984064, win 512, length 120... |
| 15:34:06.681597 | 190-0-175-100.gba.solunet.com.ar.2485 | **Requête de connexion (SYN)** | Flags [S], seq 780253659:780253779, win 512, length 120... |
| 15:34:06.681614 | 190-0-175-100.gba.solunet.com.ar.2486 | **Requête de connexion (SYN)** | Flags [S], seq 426927737:426927857, win 512, length 120... |
| 15:34:06.681630 | 190-0-175-100.gba.solunet.com.ar.2487 | **Requête de connexion (SYN)** | Flags [S], seq 2059846495:2059846615, win 512, length 1... |
| 15:34:06.681647 | 190-0-175-100.gba.solunet.com.ar.2488 | **Requête de connexion (SYN)** | Flags [S], seq 485695892:485696012, win 512, length 120... |
