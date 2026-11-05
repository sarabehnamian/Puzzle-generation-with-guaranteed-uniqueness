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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_enc_encA\e2_enc_encA_003.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/2/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- country: Chile, India, Italy, Ghana, Nepal
- dish: pasta, curry, stew, salad, sushi
- pet: cat, parrot, rabbit, gecko, dog
- colour: pink, violet, brown, cyan, gold

Clues:
1. The Ghanaian and the Indian live in the two end houses.
2. The Italian lives directly right of the Ghanaian.
3. The Chilean does not live next to the Italian.
4. The curry eater lives in the middle house.
5. The salad eater lives directly left of the Indian.
6. The Indian eats sushi.
7. The pasta eater is not the Ghanaian.
8. The dog owner eats salad.
9. The Indian owns the parrot.
10. The curry eater owns the rabbit.
11. The cat owner lives next to the rabbit owner.
12. The cat owner lives in the gold house.
13. The violet house is next to the brown house.
14. The gecko owner lives in the cyan house.
15. The Indian does not live in the violet house.
16. The Nepali lives in the pink house.

## Puzzle zebra/0/g6

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Quinn, Omar, Mia, Pia, Noah
- car: teal, silver, maroon, gold, navy
- hobby: pottery, skiing, knitting, painting, diving
- city: Cairo, Lima, Seoul, Rome, Oslo

Clues:
1. Quinn lives at one end of the street.
2. Noah lives at one end of the street.
3. Quinn lives somewhere left of Noah.
4. There is exactly one house between Mia and Noah.
5. Pia lives directly right of Mia.
6. Omar drives the silver car.
7. The silver car is directly left of the maroon car.
8. The navy car is at one end of the street.
9. The gold car is next to the navy car.
10. The skier drives the silver car.
11. The potter drives the teal car.
12. The diver lives at one end of the street.
13. The painter lives directly right of the knitter.
14. The Lima resident is the skier.
15. The painter lives in Rome.
16. The Seoul resident lives directly left of Pia.
17. The Cairo resident drives the teal car.

## Puzzle zebra/0/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- country: Egypt, Chile, Italy, Ghana, India
- tree: birch, oak, elm, pine, maple
- pet: mule, hare, swan, eel, otter
- sweet: jelly, toffee, fudge, tart, mousse

Clues:
1. The Egyptian lives at one end of the street.
2. The Indian lives at one end of the street.
3. The Egyptian lives somewhere left of the Indian.
4. The Italian does not live next to the Egyptian.
5. The Italian does not live next to the Indian.
6. The Ghanaian lives somewhere right of the Chilean.
7. The Italian's tree is the elm.
8. The pine tree stands directly right of the elm.
9. The oak stands directly right of the birch.
10. The swan owner lives under the elm.
11. The eel owner lives under the pine.
12. The Chilean owns the hare.
13. The swan owner likes fudge.
14. The tart lover lives directly right of the fudge lover.
15. The jelly lover owns the mule.
16. The toffee lover lives next to the jelly lover.

## Puzzle zebra/2/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Ann, Ben, Cy, Di, Ed
- car: Audi, BMW, Fiat, Ford, Kia
- city: Rome, Oslo, Lima, Bern, Cairo
- pet: cat, dog, owl, frog, hamster

Clues:
1. Ann lives in the middle house.
2. Di lives directly left of Ben.
3. Cy lives in one of the two end houses.
4. Ed lives somewhere to the left of Ann.
5. Ann drives the Kia.
6. The BMW driver lives next to Ann.
7. The Audi driver lives directly left of the Kia driver.
8. Cy drives the Ford.
9. The Audi driver is from Rome.
10. The Kia driver is from Cairo.
11. The person from Lima lives directly right of the person from Cairo.
12. Ben is not from Oslo.
13. The owl owner is from Oslo.
14. The dog owner drives the BMW.
15. The frog owner lives next to the dog owner.
16. The cat owner lives directly right of the owl owner.
17. Ann owns the hamster.

## Puzzle zebra/2/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: yellow, blue, red, white, green
- pet: cat, dog, bird, fish, horse
- drink: water, tea, milk, coffee, juice
- job: teacher, chef, pilot, doctor, artist

Clues:
1. The pilot lives in house 3.
2. The pilot drinks milk.
3. The teacher lives in house 1.
4. The teacher owns the cat.
5. The cat owner lives in the yellow house.
6. The chef lives directly right of the yellow house.
7. The chef drinks tea.
8. The tea drinker owns the dog.
9. The green house is directly right of the white house.
10. The coffee drinker lives in the white house.
11. The horse owner lives in the green house.
12. The artist drinks juice.
13. The fish owner lives in the white house.
14. The red house is directly right of the blue house.

## Puzzle zebra/3/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Ann, Ben, Cara, Dan, Eve
- flower: rose, tulip, daisy, lily, orchid
- music: jazz, rock, folk, opera, blues
- city: Rome, Oslo, Lima, Cairo, Paris

Clues:
1. Ben lives in an end house.
2. Cara lives directly left of Ben.
3. Eve lives next to Dan.
4. Ann does not live next to Dan.
5. Ann lives somewhere to the right of Dan.
6. Eve grows roses.
7. Cara grows tulips.
8. The orchid grower lives in the middle house.
9. The lily grower lives somewhere to the left of the daisy grower.
10. The jazz fan grows roses.
11. The opera fan grows orchids.
12. Ben is the folk fan.
13. The rock fan lives next to the opera fan.
14. The jazz fan comes from Lima.
15. The Paris native is the opera fan.
16. The Rome native lives directly right of the Paris native.
17. The Oslo native lives somewhere to the right of the Cairo native.

## Puzzle zebra/0/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Kara, Liam, Maya, Jack, Ines
- drink: mocha, punch, stout, cider, lassi
- vehicle: taxi, jeep, van, scooter, truck
- pet: newt, bunny, llama, crow, gecko

Clues:
1. Kara lives at one end of the street.
2. Ines lives at one end of the street.
3. Kara lives somewhere left of Ines.
4. Liam lives next to Kara.
5. Maya lives directly left of Jack.
6. Liam drinks punch.
7. The mocha drinker lives next to the punch drinker.
8. Maya drinks stout.
9. The lassi drinker lives somewhere right of the cider drinker.
10. The taxi driver drinks mocha.
11. The van driver drinks stout.
12. The jeep driver lives next to the taxi driver.
13. Jack does not drive the truck.
14. The newt owner drives the taxi.
15. The bunny owner lives next to the newt owner.
16. The crow owner lives directly right of the llama owner.
17. The gecko owner drinks lassi.

## Puzzle zebra/3/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: chef, pilot, vet, poet, judge
- city: Bern, Kyiv, Doha, Quito, Hanoi
- coat: red, black, tan, lilac, green
- drink: tea, rum, sake, milk, juice

Clues:
1. There is exactly one house between the chef and the judge.
2. The poet lives directly right of the chef.
3. The pilot lives in an end house.
4. The vet does not live next to the chef.
5. The pilot lives somewhere to the right of the judge.
6. The Quito native is the judge.
7. The Kyiv native is either the pilot or the vet.
8. The Hanoi native lives directly left of the Kyiv native.
9. The Bern native lives next to the Quito native.
10. The pilot wears the black coat.
11. The green coat is next to the black coat.
12. The poet wears the lilac coat.
13. The chef does not wear the red coat.
14. The tea drinker lives directly left of the judge.
15. The milk drinker lives in the house with the red coat.
16. The sake drinker wears the green coat.
17. The juice drinker is the pilot.

## Puzzle zebra/3/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Greek, Dane, Irish, Swede, Pole
- hobby: golf, chess, hiking, sailing, painting
- fruit: plum, mango, apple, pear, lemon
- vehicle: tram, bike, car, van, bus

Clues:
1. The Irish person lives in the middle house.
2. The Greek does not live next to the Irish person.
3. The Dane lives somewhere to the left of the Swede.
4. The Pole lives directly right of the Swede.
5. The Dane plays chess.
6. The Irish person loves hiking.
7. The Swede loves sailing.
8. The golfer lives somewhere to the left of the painter.
9. The apple eater is the hiker.
10. The pear eater lives directly right of the apple eater.
11. The mango eater lives next to the apple eater.
12. The lemon eater is the painter.
13. The bike rider eats mango.
14. The car driver is the hiker.
15. The Swede drives the van.
16. The golfer does not take the bus.

## Puzzle zebra/0/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- country: Kenya, Norway, Peru, Japan, Spain
- instrument: harp, drum, piano, flute, violin
- snack: candy, pretzel, cookie, chips, nuts
- door: yellow, black, red, green, blue

Clues:
1. The Kenyan lives in house 1.
2. The pianist lives in the middle house.
3. The Norwegian lives directly left of the pianist.
4. The Spaniard lives somewhere right of the Japanese.
5. The Peruvian does not live next to the Spaniard.
6. The harpist lives next to the Norwegian.
7. The flutist lives directly left of the violinist.
8. The pianist lives in the red house.
9. The Japanese lives in the green house.
10. The Spaniard lives in the blue house.
11. The drummer lives in the black house.
12. The cookie lover lives in the red house.
13. The candy eater plays the harp.
14. The chips eater lives directly left of the nuts eater.
