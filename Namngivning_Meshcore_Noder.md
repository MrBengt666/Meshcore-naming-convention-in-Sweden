---
title: "Project Documentation"
date: "$BUILD_DATE$"
---

Rekommendationer för namngivning av noder i Meshcore-nät
===

frav\_se\*, PappaNiklas\*, haxdoggy\*, DanielPaulsson\*, Burt Persson — \* SysOps för http://had.meshmapper.net/

Kontakt: Discord SWEDEN-MESH #halland — https://discord.com/channels/1359596001240944660/1467977832557973635

En enhetlig namnstruktur underlättar felsökning och samordning. En gemensam konvention gör det möjligt att direkt från nodnamnet utläsa område, kommun och placering utan att konsultera extern dokumentation. **OBS! Detta är rekommendationer!**

---

## Namnstruktur

```
[SE]-[IATA|KOMMUN]-[BESKRIVNING]-[PKID]
```

Alla fält obligatoriska. Versaler genomgående. Inga svenska tecken. Bindestreck (`-`) som enda avskiljare. Max 22 tecken totalt (inkl. bindestreck).

## Exempel

```
SE-HAD-ARNECOMP-AB12
SE-BST-KATTVREP1-EF34
SE-LAH-HALLONV1-BF12
```

---

## Fältbeskrivning

| **Fält** | **Längd** | **Beskrivning** |
|---|---|---|
| **[SE]** | 2 (fast) | Landskod enligt ISO 3166-1 alpha-2. Skall vara SE för noder i Sverige |
| **[IATA\|KOMMUN]** | 3 (fast) | IATA-kod för närmaste flygplats (Meshmapper-område), t.ex. `ARN`, `GOT` — eller förkortning för kommun som ej sammanfaller med svensk IATA-kod, t.ex. `BST`, `MAL`. Båda tre bokstäver. Se appendix för rekommenderade förkortningar för kommun. |
| **[BESKRIVNING]** | max 10 | Placering, ägare eller adress. Se nodtyper nedan. |
| **[PKID]** | 4 (fast) | Fyra första tecknen i nodens publika nyckel, t.ex. `A3FX` |

## Rekommendationer per nodtyp

| **Nodtyp** | **[BESKRIVNING]** |
|---|---|
| **Repeater** | Fysisk placering, byggnadsnamn eller höjdläge |
| **Room Server** | Fysisk placering eller byggnadsnamn |
| **Companion** | Innehavarens namn eller anropssignal |

---

*Kommunkoder: Se Appendix. IATA-koder: Se Appendix samt Meshmapper.*


