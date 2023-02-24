carDealer = {
  "brand": ['Suzuki', 'Mercedes Benz', 'Toyota', 'Hyundai', 'Volkswagen', 'Chevrolet', 'Nissan', 'Cadillac', 'Renault', 'Ford', 'Kia', 'Honda', 'Fiat', 'Chrysler', 'Citroen', 'BMW', 'Geely', 'Audi', 'Daewoo', 'Ferrari', 'Infiniti', 'Jaguar', 'Lamborghini', 'Land Rover', 'Lexus', 'Opel', 'Bugatti', 'Hammer', 'Jeep', 'Maseratti'],
  
  "model": ['Baleno Delta AMT', 'SETRA S417HDH', 'Corolla', 'Tucson SUV', 'Taigun', 'Camaro', 'Terrano', 'LYRIQ', 'KWID', 'F-150', 'Seltos', 'Amaze', '500X POP', 'Pacifica', 'C3', 'Z4', 'Emgrand EC7', 'Q5', 'Nexia', 'Roma', 'QX55', 'XF', 'Urus Pearl', 'VELAR', 'LC', 'Corsa', 'Chiron Noire', 'SUV Adventure', 'Compass', 'Ghibli' ],
  
  "price": [11620, 60000, 21550, 42500, 41500, 34600, 41450, 58590, 47500, 35680, 37400, 41500, 27965, 50595, 47500, 41450, 21400, 44570, 36595, 34600, 49150, 47000, 246700, 61500, 94125, 36500, 3250000, 30397, 49125, 78000]
}

print('What are the brands of cars available: ')
for i in carDealer['brand']:
   print(i)
print('\n')

userChoice = input('What brand of car do you want: ')

if(userChoice in (carDealer['brand'])):
    print('Model available -> ' + carDealer['model'][carDealer['brand'].index(userChoice)])
    print('Price of model  -> ' + '$'+ str(carDealer['price'][carDealer['brand'].index(userChoice)]))
else:
    print('Brand of car wanted is not available at the moment')
