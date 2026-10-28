# ez az első konzultáció

felhasznalo_neve = 'Valaki'
felhasznalo_kora = 20 # int(input('Hány éves vagy: '))
felhasznalo_kora /= 2
# felhasznalo_neve *= 2
jegyek = [3, 4, 5]
jegyek += [1]
hallgato = {'Név': 'Józsi', 'Kor': 50}
print('Szia', 'dr.' + felhasznalo_neve, '!', felhasznalo_kora)
print(f'Szia dr. {felhasznalo_neve}! Kora: {felhasznalo_kora}')
print('Szia', 'dr.' + felhasznalo_neve, '!', felhasznalo_kora, sep='-', end='\n\n')

print(hallgato['Név'])
print(jegyek)

print('szöveg'.rjust(50, '.'))
print('szöveg'.ljust(50, '.'))
print('szöveg'.center(50, '.'))
print(str(felhasznalo_kora).center(50, '.'))