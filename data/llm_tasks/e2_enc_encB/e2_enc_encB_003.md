# Task: encode logic-grid puzzles as solver constraints

Translate each puzzle below into constraints in a small Python DSL. A program will check your
constraints with a SAT/SMT solver, so they must say exactly what each clue says - no more, no less.

The DSL:
- pos('value') is the house number (an integer from 1 to N) of the given value. Use the value names
  exactly as they appear in the puzzle header (case does not matter).
- The basic rules (every value is in exactly one house; values of the same category are in different
  houses) are added automatically. Do not encode them.
- Encode each numbered clue as ONE Python boolean expression using pos(...), integer constants,
  == != < <= > >= + -, and the functions Abs(x), And(a, b, ...), Or(a, b, ...), Not(a), Implies(a, b).
- Do not use Python's and/or/not/in, chained comparisons such as 1 < x < 3, or abs().

Examples (from other puzzles):
- "The baker keeps the parrot."            ->  pos('baker') == pos('parrot')
- "The violinist lives in the fourth house." ->  pos('violinist') == 4
- "The person who reads poetry lives next to the person who drinks lemonade."
                                            ->  Abs(pos('poetry') - pos('lemonade')) == 1

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_enc_encB/e2_enc_encB_003.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/2/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- country: Cuba, Spain, Iran, Chad, Italy
- vehicle: Taxi, Bus, Ferry, Tram, Bike
- dessert: Pie, Tart, Gelato, Cake, Flan
- hobby: Dance, Poetry, Hiking, Drawing, Baking

Clues:
1. The Cuban and the Italian live in the two end houses, one at each end.
2. The Spaniard lives directly right of the Cuban.
3. The Chadian lives directly left of the Italian.
4. The Iranian takes the ferry.
5. The Italian rides the bike.
6. The tram rider is either the Cuban or the Chadian.
7. The taxi passenger lives directly left of the bus rider.
8. The gelato eater takes the ferry.
9. The cake eater rides the tram.
10. The flan eater is the Italian.
11. The tart eater lives directly right of the pie eater.
12. The person who enjoys baking eats flan.
13. The hiking fan eats gelato.
14. The poetry lover rides the bus.
15. The drawing fan is the Chadian.

## Puzzle zebra/2/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: Green, Black, White, Red, Blue
- pet: Rabbit, Cat, Snake, Owl, Dog
- drink: Tea, Wine, Cola, Beer, Water
- sport: Rugby, Judo, Golf, Tennis, Boxing

Clues:
1. The golf player lives in the middle house.
2. The white house belongs to the golf player.
3. The red house is directly right of the white house.
4. The blue house is next to the red house.
5. The green house is somewhere to the left of the black house.
6. The dog owner lives in the blue house.
7. The snake owner drinks cola.
8. The cola drinker is the golf player.
9. The owl owner lives directly right of the snake owner.
10. The cat owner lives in the black house.
11. The beer drinker lives directly right of the cola drinker.
12. The water drinker owns the dog.
13. The wine drinker lives next to the cola drinker.
14. The tennis player drinks beer.
15. The boxer owns the dog.
16. The judo player drinks wine.

## Puzzle zebra/1/g5

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, ivory, yellow, blue
- pet: dog, snail, fox, horse, zebra
- drink: tea, coffee, milk, juice, water
- snack: chips, nuts, cake, popcorn, cookies

Clues:
1. The milk drinker lives in the middle house.
2. The red house belongs to the chips eater.
3. The chips eater drinks milk.
4. The green house is directly right of the ivory house.
5. The coffee drinker lives in the green house.
6. The yellow house is not next to the red house.
7. The tea drinker lives in the blue house.
8. The water drinker lives in the yellow house, directly left of the tea drinker.
9. The nut eater drinks water.
10. The cookie eater drinks tea.
11. The cake eater lives in the ivory house.
12. The dog's owner drinks coffee.
13. The snail lives in the red house.
14. The zebra lives directly right of the snail.
15. The fox lives somewhere to the left of the horse.

## Puzzle zebra/3/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Alice, Bob, Carol, Dave, Eve
- flower: rose, tulip, lily, daisy, orchid
- instrument: piano, violin, flute, drums, guitar
- drink: tea, coffee, cocoa, soda, juice

Clues:
1. Alice lives in the middle house.
2. Bob lives at one end of the row.
3. Carol lives somewhere left of Alice.
4. Dave lives directly right of Alice.
5. There is exactly one house between Eve and Dave.
6. Alice grows daisies.
7. The orchid grower lives directly right of the daisy grower.
8. Bob grows lilies.
9. The tulip grower lives somewhere left of the rose grower.
10. The flute player grows lilies.
11. The violin player grows daisies.
12. The guitarist lives next to the flute player.
13. The drummer does not live next to the violin player.
14. The juice drinker plays the violin.
15. The coffee drinker plays the flute.
16. The orchid grower drinks soda.
17. The tea drinker is not the drummer.

## Puzzle zebra/2/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: Yellow, Green, Red, White, Blue
- pet: Fish, Dog, Bird, Cat, Horse
- drink: Milk, Tea, Coffee, Water, Juice
- job: Chef, Teacher, Doctor, Pilot, Baker

Clues:
1. The red house is in the middle of the row.
2. The green house is directly left of the red house.
3. The blue house is next to the white house.
4. The white house is somewhere to the left of the blue house.
5. The fish owner lives in the yellow house.
6. The bird owner lives in the red house.
7. The dog owner lives directly left of the bird owner.
8. The horse owner lives in the blue house.
9. The coffee drinker lives in the red house.
10. The tea drinker owns the dog.
11. The milk drinker owns the fish.
12. The water drinker lives directly left of the juice drinker.
13. The doctor drinks coffee.
14. The pilot owns the cat.
15. The baker drinks juice.
16. The teacher lives somewhere to the right of the chef.

## Puzzle zebra/0/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- team: Hawks, Lions, Bears, Wolves, Eagles
- colour: lime, gold, cyan, rose, slate
- role: goalie, winger, centre, sweeper, striker
- drink: water, juice, cola, tea, milk

Clues:
1. The Eagles live in the middle house.
2. There is exactly one house between the Bears and the Hawks.
3. The Bears live somewhere to the left of the Hawks.
4. The Wolves do not live next to the Hawks.
5. The slate shirts belong to the Eagles.
6. The gold shirts are directly right of the slate shirts.
7. The lime shirts are next to the slate shirts.
8. The cyan shirts do not belong to the Wolves.
9. The centre plays for the Eagles.
10. The goalie plays for the Bears.
11. The winger lives directly right of the centre.
12. The striker lives somewhere to the left of the sweeper.
13. The centre drinks juice.
14. The Bears drink tea.
15. The milk drinker is the winger.
16. The cola drinker lives somewhere to the left of the water drinker.

## Puzzle zebra/3/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, Finn, German, Swede
- car: Audi, Fiat, Mazda, Saab, Volvo
- hobby: chess, golf, rowing, tennis, fencing
- snack: nuts, chips, olives, popcorn, pretzels

Clues:
1. The Brit lives in the middle house.
2. The Dane lives at one end of the row.
3. The Swede lives next to the Brit.
4. The German does not live next to the Brit.
5. The Finn lives directly right of the Brit.
6. The Dane lives somewhere left of the German.
7. The Saab owner is the Finn.
8. The Mazda owner lives directly right of the Saab owner.
9. The Audi owner lives in the middle house.
10. The Swede does not drive the Fiat.
11. The golfer drives the Fiat.
12. The Finn is a rower.
13. The tennis player lives directly left of the rower.
14. The fencer lives next to the rower.
15. The chips eater is the tennis player.
16. The olives eater lives at one end of the row.
17. The olives eater lives somewhere left of the nuts eater.
18. The popcorn eater is the Finn.
19. The pretzels eater is not the chess player.

## Puzzle zebra/1/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, blue, green, yellow, white
- pet: dog, cat, bird, fish, horse
- drink: tea, coffee, milk, juice, water
- job: doctor, teacher, chef, pilot, artist

Clues:
1. The red house is directly right of the green house.
2. The white house is directly right of the red house.
3. The yellow house is the fifth house.
4. The blue house is not the first house.
5. The cat lives in the green house.
6. The dog lives in the red house.
7. The fish lives in the white house.
8. The bird does not live in the blue house.
9. The person in the green house drinks water.
10. The tea drinker owns the dog.
11. The milk drinker owns the fish.
12. The coffee drinker lives in the blue house.
13. The pilot drinks water.
14. The artist lives directly right of the pilot.
15. The doctor drinks milk.
16. The chef lives somewhere to the right of the doctor, but not in the yellow house.

## Puzzle zebra/1/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Alice, Bob, Carol, David, Eve
- flower: rose, tulip, lily, daisy, orchid
- instrument: piano, violin, flute, drums, harp
- city: Paris, Rome, Oslo, Lima, Cairo

Clues:
1. Carol lives at one end of the row and Bob lives at the other end, with Carol to the left of Bob.
2. Eve lives directly right of Carol.
3. Alice lives in the middle house.
4. Carol grows daisies.
5. The rose grower lives directly right of the daisy grower.
6. The lily grower lives directly left of Bob.
7. Alice does not grow tulips.
8. The harpist lives in the daisy house.
9. The pianist lives directly right of the harpist.
10. The drummer grows orchids.
11. Bob does not play the flute.
12. The person from Lima plays the harp.
13. The person from Oslo plays the piano.
14. The person from Paris is Alice.
15. The person from Rome lives somewhere to the right of the person from Cairo.

## Puzzle zebra/0/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nation: Dane, Finn, Greek, Irish, Pole
- sport: chess, golf, rowing, tennis, judo
- fruit: apple, pear, plum, fig, lime
- car: Audi, Fiat, Ford, Mini, Opel

Clues:
1. The Irish person lives in the middle house.
2. The Dane lives in one of the two end houses.
3. The Greek lives directly right of the Finn.
4. The Pole lives directly left of the Irish person.
5. The chess player is the Irish person.
6. The judo player lives next to the chess player.
7. The Pole does not play judo.
8. The tennis player is neither the Dane nor the Greek.
9. The golfer lives somewhere to the left of the rower.
10. The person who eats the pear plays chess.
11. The person who eats the lime plays judo.
12. The fig eater lives next to the pear eater.
13. The plum eater lives somewhere to the right of the apple eater.
14. The Ford driver eats the pear.
15. The Opel driver lives directly left of the Ford driver.
16. The Mini driver is the Finn.
17. The Audi driver is not the Greek.
