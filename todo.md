# TEAM
wahl eines teams "Instinct"/"Mystic"/"Valor"
- es soll nur die Wahl eines der Teams möglich sein, aber nicht mehrere.
- eine Änderund ist später nur durch einen Moderator möglich, um zu verhindern
  das man die Absprachen der anderen Teams "belauschen" kann, und dann zurück
  wechselt.
- Mehrfachwahl soll nicht möglich sein.
- realisierung über befehl im chat
- die anderen teams (harmony, rocket) werden eventuell später implementiert)
- help sollte überdacht werden, wie diese am besten in das ganze programm
  am saubersten mit durchgezogen werden kann.
```
.team [instinct|mystic|valor|harmony|rocket|help]
```

# RESEARCH *(Feldforschung)*
Die Lösung über Bots erlaubt korrekturen an Meldungen ohne das der Ersteller des Posts
diese vornehmen muss, da dafür der Bot einspringt. Somit kann anderen usern die
Möglichkeit gegeben werden Korrekturen an bestehenden Posts vorzunehmen.

Mögliche realisierungen
1. kompletter Befehl im Chat der alle Optionen enthält
2. Initialisierender Chatbefehl der Member durch Auswahlmöglichkeiten zur erstellung
   Posts verhilft.
```
.res .research .res .forschung .f [auftrag|update]
```

# RARE *-(spawns)*
Meldung Seltener Pokémon (Ditto, 100%IV,...)
```
.rare [pkm|update|del] <tarnung> <wp> <maps> <time>
```

# SERVERINFO
Informationen über den Server.
- Member: gesamtzahl der Member abzüglich der 'BOT'-Accounts.
  - in seperaten listen die anzahlen der Teams Instinct, Mystic & Valor
  - auch jene beziffern, die in keinem der 3 team sind (zur übersicht)
```
.server [info]
```

# spaetere inplementierung

`.nest`

`.raid .r [update <id>|del] <pokemon> <schlüpft> <start> <arena>`

`.exraid .ex [update <id>|del] <datum> <schlüpft>`

`.update ID Pokemon/Zeit1/Zeit2/Ort`

# Implementierung

* eine mögliche erweiterung wäre es, einen fertigen feldforschungspost in weitere
gruppen posten zu lassen (WhatsApp, Telegram)
