# TEAM
wahl eines teams "Instinct"/"Mystic"/"Valor"
- nur eines der drei teams soll zur wahl stehen. eine änderund ist später
  nur durch einen Moderato möglich, um zu verhindern das man die absprachen
  der anderen teams "belauschen" kann, und dann zurück wechselt. auch eine
  mehrfachwahl soll nicht möglich sein.
- realisierung über befehl im chat
- die anderen teams (harmony, rocket) werden eventuell später implementiert)
- help sollte überdacht werden, wie diese am besten in das ganze programm
  am saubersten mit durchgezogen werden kann.
```
.team [instinct|mystic|valor|harmony|rocket|help]
```

# RESEARCH *(Feldforschung)*
Die löung über bots erlaubt korrekturen an Meldungen, ohne das der ersteller der
feldforschung diese in seinem beitrag ändern, bzw gelöscht und neu geschrieben
werden muss
- Möglichkeit 1
  über einen Kompletten Befehl im Chat der alle optionen enthält
```
.res .research .res .forschung .f [auftrag|update]
```

# RARE*-spawns*
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

spaetere inplementierung

`.nest`

`.raid .r [update <id>|del] <pokemon> <schlüpft> <start> <arena>`

`.exraid .ex [update <id>|del] <datum> <schlüpft>`

`.update ID Pokemon/Zeit1/Zeit2/Ort`


*discord.py@rewrite*
`pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip`
