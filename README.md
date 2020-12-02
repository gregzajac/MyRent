# MyRent
Aplikacja stworzona w Django, umożliwiająca zarządzanie wynajmem mieszkań, realizuje poniższe UseCases. Działająca aplikacja znajduje się [tutaj](https://gz-myrent-django.herokuapp.com/).
### Przykładowe dane właściciela i najemcy:
```buildoutcfg
# właściciel
login: gzadmin 
hasło: gzadmin

# najemca
login: jkowalski
hasło: 123jk123
```

### UseCases

1. Jako właściciel chcę móc dodawać nowe mieszkanie oraz modyfikować lub usuwać istniejące. Mieszkanie powinno zawierać adres i dodatkowy opis dla potencjalnych najemców.
2. Jako właściciel chcę móc dodać/usunąć zdjęcia do danego mieszkania (wiele zdjęć do jednego mieszkania).
3. Jako właściciel chcę móc zaznaczyć, czy dane mieszkanie jest do wynajęcia. Mieszkania nieodznaczone nie powinny pokazywać się na liście dostępnych mieszkań na stronie internetowej.
4. Jako właściciel chcę móc dodać umowę najmu na dane mieszkanie z danym najemcą. Umowa najmu powinna posiadać datę podpisania, okres najmu (od, do), kwota najmu (miesięczne opłaty), termin dokonywania opłat (dzień miesiąca) oraz miejsce na dodatkowe informacje o umowie.
5. Jako właściciel chcę trzymać podstawowe informacje o najemcach (imię, nazwisko, telefon, email, miejsce na dodatkowe informacje)
6. Jako właściciel chcę modyfikować zawartość umowy lub usunąć daną umowę.
7. Jako właściciel chcę prowadzić rozliczenia na danej umowie (dodawać/modyfikować/usuwać naliczenia oraz operacje finansowe) oraz widzieć saldo rozliczeń.
8. Jako właściciel chcę móc generować wszystkie zaległe naliczenia na danej umowiej, jedno naliczenie na miesiąc (jeżeli najem nie rozpoczyna się od 1-ego danego miesiąca, pierwsze naliczenie powinno pojawić się w kolejnym miesiącu). Ostatnie naliczenie powinno być w miesiącu generowania (najpóźniej w miesiącu końca najmu).
9. Jako najemca chcę widzieć wszytkie swoje umowy i rozliczenia (także na umowach historycznych).
10. Jako najemca chcę móc zmienić hasło
11. Jako dowolny użytkownić chcę móc przeglądać listę mieszkań wraz z ich zdjęciami oraz widzieć dane kontaktowe właściciela.