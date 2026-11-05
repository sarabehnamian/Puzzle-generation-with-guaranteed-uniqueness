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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_enc_encB\e2_enc_encB_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/2/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Alice, Bob, Carol, Dave, Eve
- drink: water, tea, milk, juice, coffee
- pet: rabbit, parrot, dog, turtle, cat
- hobby: chess, cycling, painting, reading, gardening

Clues:
1. The painter lives in the middle house.
2. Eve is the painter.
3. Dave plays chess.
4. The chess player owns the rabbit.
5. The rabbit owner lives directly left of Alice.
6. Dave does not live next to Eve.
7. Carol does not live next to Eve.
8. The cyclist lives directly right of the chess player.
9. Carol is the gardener.
10. The tea drinker is the cyclist.
11. Bob drinks juice.
12. The milk drinker lives directly left of Bob.
13. The coffee drinker lives next to the juice drinker.
14. The parrot owner is the cyclist.
15. Eve owns the dog.
16. Bob does not own the cat.

## Puzzle zebra/0/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: orange, pink, grey, purple, brown
- pet: goat, cat, duck, pig, hen
- drink: cola, tea, juice, wine, beer
- music: folk, jazz, opera, techno, rock

Clues:
1. The grey house is in the middle.
2. The purple house is directly right of the grey house.
3. The pink house is next to the grey house.
4. The orange house is somewhere left of the pink house.
5. The juice drinker lives in the grey house.
6. The wine drinker lives next to the juice drinker.
7. The tea drinker lives in the pink house.
8. The beer drinker lives in the brown house.
9. The jazz fan drinks tea.
10. The opera fan drinks juice.
11. The techno fan lives directly right of the opera fan.
12. The rock fan drinks beer.
13. The cat owner likes jazz.
14. The hen owner lives in the brown house.
15. The pig owner drinks wine.
16. The goat owner lives somewhere left of the duck owner.

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

## Puzzle zebra/2/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Kim, Lou, Max, Nia, Oz
- fruit: mango, peach, grape, melon, cherry
- music: jazz, rock, opera, folk, blues
- pet: lizard, hare, koi, finch, ferret

Clues:
1. Lou lives in the last house.
2. Nia lives directly left of Kim.
3. Oz lives next to Kim.
4. Max lives somewhere to the left of Nia.
5. The mango eater lives in the middle house.
6. The cherry eater lives directly left of the mango eater.
7. Lou eats peaches.
8. The grape eater lives directly right of the mango eater.
9. The jazz fan eats cherries.
10. The melon eater likes folk.
11. Kim likes blues.
12. Oz does not like opera.
13. The hare owner likes jazz.
14. Kim owns the koi.
15. The ferret owner eats peaches.
16. The finch owner lives somewhere to the left of the lizard owner.

## Puzzle zebra/0/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Drew, Cleo, Finn, Ava, Ben
- pet: parrot, rabbit, hamster, turtle, goldfish
- dish: curry, pizza, sushi, tacos, pasta
- sport: hockey, tennis, soccer, rugby, cricket

Clues:
1. Ben lives at one of the two ends of the street.
2. Drew lives at one of the two ends of the street.
3. Drew lives somewhere left of Ben.
4. Finn lives directly left of Ava.
5. Cleo lives next to Drew.
6. Drew owns the parrot.
7. The rabbit owner lives next to the parrot owner.
8. The turtle owner lives directly right of the hamster owner.
9. The goldfish owner does not live next to the rabbit owner.
10. The pizza eater owns the rabbit.
11. The sushi eater owns the hamster.
12. The tacos eater lives directly left of the pasta eater.
13. The tennis player eats pizza.
14. The curry eater plays hockey.
15. The cricket player owns the goldfish.
16. Finn does not play rugby.

## Puzzle zebra/1/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- instrument: cello, drums, flute, guitar, piano
- food: curry, pasta, pizza, sushi, tacos
- city: Berlin, Delhi, Lima, Oslo, Rome
- shirt: blue, gold, pink, teal, violet

Clues:
1. The pianist lives in the middle house.
2. There is exactly one house between the guitarist and the drummer.
3. The flutist lives somewhere to the right of the cellist.
4. The guitarist lives next to the cellist.
5. The pianist eats curry.
6. The pizza eater lives next to the drummer.
7. The drummer eats tacos.
8. The guitarist does not eat pasta.
9. The Berliner plays either the cello or the flute.
10. The Delhi resident eats sushi.
11. The Delhi resident lives next to the Berliner.
12. The Rome resident plays the piano.
13. The Oslo resident is not the flutist.
14. The pianist wears teal.
15. The gold shirt is directly left of the violet shirt.
16. The pink shirt is not next to the teal shirt.
17. The cellist does not wear pink.

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

## Puzzle zebra/0/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, white, blue, yellow
- pet: cat, dog, bird, fish, horse
- drink: tea, juice, milk, coffee, water
- job: doctor, pilot, chef, artist, teacher

Clues:
1. The chef lives in house 3.
2. The chef lives in the white house.
3. The milk drinker lives in the white house.
4. The fish owner lives directly right of the white house.
5. The fish owner drinks coffee.
6. The artist drinks coffee.
7. The doctor lives directly left of the pilot.
8. The pilot drinks juice.
9. The teacher lives in the yellow house.
10. The blue house is next to the yellow house.
11. The horse owner drinks water.
12. The cat owner drinks tea.
13. The dog owner lives in the green house.
14. The cat owner lives in the red house.

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
