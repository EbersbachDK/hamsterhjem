# Hamsterhjem

Pas din hamster, og byg buret selv. Et lille dansk hamster-simulatorspil i én HTML-fil – vælg race, lær hamsterens personlighed at kende, hold den mæt, ren og glad, og indret buret efter dyrevelfærdsanbefalingerne.

**Spil:** https://ebersbachdk.github.io/hamsterhjem/

- Virker på computer, iPad og telefon (touch: tryk for at kæle, træk for at flytte ting i "Byg bur")
- Kan lægges på hjemmeskærmen (Safari → Del → Føj til hjemmeskærm) og spilles offline
- Spillet gemmes automatisk i browseren

## Udvikling

- Hele spillet er `index.html`. Versionen står kun i `APP_VERSION` – hæv den ved hver udgivelse, så service workeren henter den nye udgave.
- Ikoner: `py tools/make_icons.py` (kræver Pillow) → `icons/`
- Skrifttyper (Bricolage Grotesque, Figtree – SIL Open Font License) ligger lokalt i `fonts/`, så spillet virker offline.
- Lokal test: `py -m http.server 8765` og åbn http://127.0.0.1:8765/
