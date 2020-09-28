print('Hello You!, ik ben Daan')
print('Wie ben jij?')
naam = input()
print('Hello ' + naam)

print('Voor ik naar het ma ging heb ik een aantal maanden een HBO gedaan, welke?')
print('A. HBO ICT bij HVA')
print('B. HBO bedrijfseconomie HVA')
print('C. HBO life science & chemistry Inholland Amsterdam')
q1_ans = input('jouw antwoord:')
if q1_ans == 'C' or q1_ans == 'c':
	print('Correct')
else:
	print('Incorrect')

print()

print('Voor ik die HBO had gedaan zat ik op de middelbare school, welke school?')
print('A. RSG Enkhuizen')
print('B. Martinuscollege Grootebroek')
print('C. Clusiuscollege Hoorn')
q2_ans = input('jouw antwoord:')
if q2_ans == 'A' or q2_ans == 'a':
	print('Correct')
else:
	print('Incorrect')

print()

print('Welke route wil ik bij het ma volgen?')
print('A. Game Artist')
print('B. Game developer')
print('C. Software developer')
q3_ans = input('jouw antwoord:')
if q3_ans == 'B' or q3_ans == 'b':
	print('Correct')
else:
	print('Incorrect')

print()

print('Wat is mijn favoriete spel?')
print('A. Forza Horizon 4')
print('B. Rocket League')
q4_ans = input('Jouw antwoord:')
if q4_ans == 'A' or q4_ans == 'a':
        print('Incorrect, maar het is wel mijn tweede favoriet!')
        print()
        print('Wat is mijn favoriete auto in Forza Horizon 4?')
        print('A. Lamborghini Centenario LP 770-4')
        print('B. Mercedes-Benz C 63 AMG Coupé Black Series')
        print('C. Nissan Skyline GT-R V-Spec II')
        q4.1_ans = input('Jouw antwoord:')
        if q4.1_ans == 'B' or q4.1_ans == 'b':
                print('Correct')
        else:
                print('Incorrect')
elif q4_ans == 'B' or q4_ans == 'b':
        print('Correct')
        print()
        print('Wat is mijn favoriete auto in Rocket League?')
        print('A. Octane')
        print('B. Fennec')
        print('C. Merc')
        print('D. Dominus')
        print('E. Breakout')
        print('F. Batmobile')
        q4.2_ans = input('Jouw antwoord:')
        if q4.2_ans == 'D' or q4.2_ans == 'd':
                print('Correct')
        else:
                print('Incorrect')

