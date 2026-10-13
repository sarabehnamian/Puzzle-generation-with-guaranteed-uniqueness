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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_enc_encB/e2_enc_encB_002.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/1/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, blue, yellow, white
- pet: dog, cat, bird, fish, hamster
- drink: tea, coffee, milk, juice, beer
- job: nurse, baker, pilot, judge, writer

Clues:
1. The red house is the middle house.
2. The green house is directly right of the red house.
3. The white house is next to the blue house.
4. The juice drinker lives in the blue house.
5. The beer drinker lives in the white house.
6. The juice drinker lives somewhere to the left of the beer drinker.
7. The milk drinker lives in the red house.
8. The coffee drinker lives in the green house.
9. The bird lives with the tea drinker.
10. The hamster lives in the green house.
11. The fish lives with the juice drinker.
12. The cat does not live with the beer drinker.
13. The nurse lives in the green house.
14. The pilot lives directly right of the nurse.
15. The judge drinks milk.
16. The writer lives in the blue house.

## Puzzle zebra/2/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- door: Beige, Navy, Lilac, Coral, Olive
- hobby: Chess, Archery, Yoga, Surfing, Knitting
- dish: Tacos, Salad, Curry, Soup, Pasta
- pet: Pony, Koi, Husky, Ferret, Gecko

Clues:
1. The olive door is at the far right.
2. The navy door is directly right of the beige door.
3. The lilac door is directly left of the coral door.
4. The coral door is somewhere to the right of the beige door.
5. The knitter lives behind the olive door.
6. The yoga fan lives behind the lilac door.
7. The surfer lives next to the knitter.
8. The archer lives directly right of the chess player.
9. The pasta eater lives behind the olive door.
10. The curry eater does yoga.
11. The soup eater lives directly left of the pasta eater.
12. The tacos eater plays chess.
13. The ferret owner is the surfer.
14. The husky owner lives behind the lilac door.
15. The koi belongs to the archer.
16. The gecko owner eats pasta.

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

## Puzzle zebra/0/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Ravi, Lena, Omar, Greta, Kofi
- city: Oslo, Lima, Cairo, Seoul, Quito
- dish: ramen, tacos, pizza, kebab, paella
- pet: lizard, rabbit, parrot, snail, mouse

Clues:
1. Kofi lives in the middle house.
2. There is exactly one house between Omar and Ravi.
3. Omar lives somewhere to the left of Ravi.
4. Lena does not live next to Omar.
5. The Lima resident is Kofi.
6. The Oslo resident lives directly right of the Lima resident.
7. The Cairo resident lives next to the Lima resident.
8. The Seoul resident lives somewhere to the left of the Quito resident.
9. The tacos fan is from Lima.
10. The kebab fan lives next to the tacos fan but not in Ravi's house.
11. The paella lover lives next to the tacos fan.
12. The pizza fan is not from Seoul.
13. The parrot owner eats tacos.
14. The lizard owner is from Oslo.
15. The mouse owner lives next to the parrot owner.
16. The snail owner lives somewhere to the left of the rabbit owner.

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

## Puzzle zebra/3/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- profession: actor, banker, clerk, diver, editor
- color: beige, cyan, gold, magenta, teal
- tree: birch, cedar, maple, oak, pine
- pet: crab, newt, owl, pig, yak

Clues:
1. The editor lives in the middle house.
2. The banker and the diver live at opposite ends of the row.
3. The diver lives somewhere left of the banker.
4. The clerk lives somewhere left of the actor.
5. The cyan house is at one end of the row, but it does not belong to the banker.
6. The magenta house belongs to the banker.
7. The gold house is directly right of the cyan house.
8. The teal house belongs to the actor.
9. The cedar grows at the teal house.
10. The birch grows in the banker's garden.
11. The maple grows in the editor's garden.
12. The pine grows somewhere left of the maple.
13. The oak is not in the gold house.
14. The crab lives with the actor.
15. The pig lives next to the crab.
16. The newt lives in the beige house.
17. The owl does not live in the gold house.

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

## Puzzle zebra/1/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Norwegian, Swede
- sport: tennis, golf, rugby, cricket, hockey
- car: Audi, Ford, Fiat, Volvo, Mazda
- fruit: apple, pear, plum, grape, mango

Clues:
1. The Norwegian lives in the first house.
2. The Swede lives next to the Norwegian.
3. The Brit lives directly right of the Swede.
4. The German lives somewhere to the left of the Dane.
5. The Norwegian plays hockey.
6. The tennis player lives directly right of the hockey player.
7. The cricket player is the Brit.
8. The golfer is not the Dane.
9. The hockey player drives the Fiat.
10. The Swede drives the Volvo.
11. The Audi owner lives directly left of the golfer.
12. The Dane drives the Ford.
13. The mango eater drives the Fiat.
14. The apple eater lives directly right of the mango eater.
15. The grape eater plays cricket.
16. The pear eater is not the Dane.

## Puzzle zebra/0/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Alice, Ben, Cara, Dev, Eve
- hobby: chess, knitting, gardening, painting, cycling
- drink: cocoa, lemonade, cider, tea, soda
- pet: parrot, rabbit, turtle, hamster, cat

Clues:
1. There is exactly one house between Cara and Eve.
2. Cara lives somewhere to the left of Eve.
3. Ben lives directly left of Eve.
4. Eve lives somewhere to the left of Alice.
5. Alice lives somewhere to the left of Dev.
6. Eve's hobby is knitting.
7. Alice plays chess.
8. The gardener lives directly right of the cyclist.
9. The knitter drinks soda.
10. The chess player drinks cider.
11. The cocoa drinker is the gardener.
12. The cyclist does not drink lemonade.
13. The parrot's owner drinks soda.
14. The turtle's owner drinks cider.
15. The cat lives next to the rabbit.
16. The rabbit's owner drinks tea.

## Puzzle zebra/3/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, blue, green, yellow, white
- pet: dog, cat, fish, bird, horse
- drink: tea, coffee, milk, juice, water
- job: doctor, chef, pilot, artist, teacher

Clues:
1. The coffee drinker lives in the middle house.
2. The water drinker lives directly right of the juice drinker.
3. The artist drinks juice.
4. The yellow house belongs to the water drinker.
5. The blue house is directly left of the yellow house.
6. The green house is at the far left end of the row.
7. The fish owner lives in the blue house.
8. The horse is kept in the yellow house.
9. The teacher lives in the yellow house.
10. The pilot drinks coffee.
11. The doctor lives directly right of the chef.
12. The chef drinks tea.
13. The doctor owns the dog.
14. The cat owner lives in the white house.
