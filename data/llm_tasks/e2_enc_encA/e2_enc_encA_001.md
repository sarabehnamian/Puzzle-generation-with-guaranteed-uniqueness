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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_enc_encA/e2_enc_encA_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/2/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Elena, Carla, Boris, Anna, Dmitri
- fruit: Pear, Kiwi, Peach, Fig, Lime
- pet: Hamster, Lizard, Tortoise, Parrot, Beagle
- sport: Squash, Cycling, Hockey, Rowing, Cricket

Clues:
1. Dmitri lives in the last house.
2. Anna lives next to Dmitri.
3. There is exactly one house between Elena and Boris.
4. Boris lives somewhere to the right of Elena.
5. The pear eater is Elena.
6. The lime eater lives in the last house.
7. The fig eater lives next to the lime eater.
8. The kiwi eater is Carla.
9. The beagle owner eats lime.
10. The parrot owner eats fig.
11. Boris owns the tortoise.
12. The lizard owner lives directly right of the hamster owner.
13. Anna plays rowing.
14. The cricket player owns the beagle.
15. The hockey player owns the tortoise.
16. The squash player does not live next to the hockey player.

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

## Puzzle zebra/3/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: amber, coral, indigo, olive, silver
- pet: ferret, gecko, goldfish, pony, spider
- drink: cider, lemonade, mead, smoothie, stout
- hobby: baking, chess, knitting, painting, hiking

Clues:
1. The amber house is in the middle of the row.
2. There is exactly one house between the olive house and the silver house.
3. The coral house is not next to the amber house.
4. The silver house is somewhere right of the olive house.
5. The indigo house is somewhere left of the olive house.
6. The goldfish lives in the coral house.
7. The spider lives in the silver house.
8. The pony lives in the olive house.
9. The gecko does not live in the amber house.
10. The mead drinker keeps the goldfish.
11. The lemonade drinker lives in the silver house.
12. The smoothie drinker keeps the ferret.
13. The cider drinker does not live in the indigo house.
14. The knitter drinks mead.
15. The painter drinks lemonade.
16. The chess player lives in the amber house.
17. The baker lives directly right of the hiker.

## Puzzle zebra/0/g5

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Ann, Bob, Cy, Di, Ed
- major: law, art, math, music, physics
- transport: bus, tram, bike, taxi, ferry
- meal: soup, stew, pasta, salad, curry

Clues:
1. Ed lives in one of the two end houses.
2. Bob lives in one of the two end houses.
3. Ed lives somewhere to the left of Bob.
4. Ann lives directly right of Ed.
5. Cy lives somewhere to the left of Di.
6. Ed studies law.
7. The physics student lives somewhere to the left of the art student.
8. The art student lives somewhere to the left of the music student.
9. Di studies art.
10. The math student is neither Bob nor Cy.
11. The music student takes the taxi.
12. The tram user lives next to the taxi user.
13. The bus user studies physics.
14. The ferry user lives somewhere to the left of the bike rider.
15. The curry lover takes the ferry.
16. The salad eater takes the tram.
17. The pasta eater studies physics.
18. The soup eater lives next to the curry eater.

## Puzzle zebra/0/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, nurse, farmer, judge, tailor
- vehicle: van, jeep, truck, moped, coach
- fruit: kiwi, mango, grape, peach, lemon
- hobby: yoga, dance, golf, chess, sewing

Clues:
1. The judge lives in the middle house.
2. The baker lives next to the judge.
3. The tailor lives next to the judge.
4. The farmer lives somewhere to the left of the nurse.
5. The tailor lives somewhere to the left of the baker.
6. The nurse rides the moped.
7. The tailor drives the coach.
8. The jeep driver lives next to the van driver.
9. The truck driver lives somewhere to the left of the tailor.
10. The baker does not drive the van.
11. The kiwi eater drives the coach.
12. The mango eater rides the moped.
13. The peach eater is the judge.
14. The lemon eater drives the jeep.
15. The golfer is the judge.
16. The yoga fan eats lemon.
17. The nurse enjoys sewing.
18. The chess player lives directly right of the dancer.

## Puzzle zebra/2/g6

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: Artist, Judge, Farmer, Nurse, Pilot
- city: Lima, Oslo, Paris, Cairo, Rome
- drink: Soda, Cocoa, Latte, Cider, Mead
- pet: Duck, Mule, Goat, Hen, Pig

Clues:
1. The farmer lives in the middle house.
2. The nurse lives directly left of the pilot.
3. The artist does not live next to the farmer.
4. The judge lives in one of the first two houses.
5. The pilot comes from Rome.
6. The farmer comes from Paris.
7. The Cairo resident lives directly left of the Rome resident.
8. The judge comes from Oslo.
9. The soda drinker is the artist.
10. The latte drinker lives in Paris.
11. The cider drinker lives in Cairo.
12. The cocoa drinker lives directly right of the soda drinker.
13. The goat owner drinks latte.
14. The pig lives in the house of the mead drinker.
15. The hen is kept by the nurse.
16. The mule belongs to the cocoa drinker.
17. The duck owner does not live next to the goat owner.

## Puzzle zebra/1/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Ana, Bo, Cy, Di, Ed
- fruit: apple, kiwi, lime, melon, fig
- sport: golf, judo, polo, yoga, darts
- city: Bern, Riga, Oslo, Rome, Kiev

Clues:
1. Ana lives in the middle house.
2. Ed and Di each live directly next to Ana, on opposite sides of her.
3. Ed lives to the left of Di.
4. Bo lives somewhere to the right of Cy.
5. Ana eats apples.
6. The fig eater lives directly left of Ana.
7. The kiwi eater lives next to the apple eater and is not the fig eater.
8. The lime eater lives somewhere to the right of the kiwi eater.
9. Bo does yoga.
10. The polo player eats melon.
11. The golfer lives directly left of the darts player.
12. Ed does not do judo.
13. The polo player lives in Rome.
14. The person from Riga does yoga.
15. The person from Bern plays golf.
16. The person from Oslo lives next to the person from Riga.

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

## Puzzle zebra/1/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, blue, yellow, white
- pet: dog, cat, bird, fish, rabbit
- drink: tea, coffee, milk, juice, water
- hobby: sailing, chess, golf, yoga, darts

Clues:
1. The green house is directly left of the red house.
2. The yellow house is directly right of the red house.
3. The blue house is somewhere to the right of the yellow house.
4. The white house is at one end of the row.
5. The water drinker lives in the white house.
6. The tea drinker lives in the green house.
7. The tea drinker lives directly right of the water drinker.
8. The milk drinker lives in the red house.
9. The juice drinker lives directly left of the coffee drinker.
10. The rabbit lives in the white house.
11. The cat drinks tea.
12. The dog lives in the red house.
13. The fish lives next to the dog.
14. The yoga fan drinks water.
15. The chess player owns the cat.
16. The darts player owns the dog.
17. The golfer lives next to the darts player.

## Puzzle zebra/2/g5

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Thai, Dane, Finn, Greek, Brit
- pet: Rabbit, Dog, Turtle, Parrot, Cat
- car: Van, Mini, Truck, Coupe, Jeep
- snack: Fudge, Crisps, Pretzel, Nachos, Popcorn

Clues:
1. The Finn lives in the middle house.
2. There is exactly one house between the Dane and the Greek.
3. The Brit lives directly right of the Greek.
4. The Dane owns the dog.
5. The Brit owns the cat.
6. The parrot owner lives directly left of the cat owner.
7. The turtle owner is the Finn.
8. The Jeep driver owns the cat.
9. The Coupe driver is the Greek.
10. The Mini driver lives right next to both the Van driver and the Truck driver.
11. The Truck driver is the Finn.
12. Popcorn is eaten by the Jeep driver.
13. The nachos eater lives next to the popcorn eater.
14. The pretzel eater drives the Truck.
15. The crisps eater owns the dog.
