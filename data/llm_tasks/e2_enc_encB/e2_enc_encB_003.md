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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_enc_encB\e2_enc_encB_003.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/2/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Abe, Bea, Cal, Dot, Eli
- shirt: lime, navy, coral, ochre, silver
- pet: pig, hen, cow, sheep, mule
- crop: corn, wheat, rye, oats, beans

Clues:
1. The cow owner lives in the middle house.
2. The cow owner grows beans.
3. Eli grows beans.
4. Eli wears silver.
5. The navy shirt is directly right of the silver shirt.
6. Dot lives in one of the end houses.
7. Abe lives directly right of Dot.
8. Cal does not live next to Eli.
9. Cal wears ochre.
10. The lime shirt is somewhere to the left of the coral shirt.
11. The wheat grower wears navy.
12. The rye grower wears lime.
13. The oats grower lives next to the wheat grower.
14. The hen lives directly right of the cow.
15. The mule owner grows corn.
16. Cal does not own the pig.

## Puzzle zebra/2/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: green, white, red, blue, yellow
- country: Kenya, Peru, Japan, Spain, Brazil
- instrument: drums, piano, violin, flute, guitar
- snack: cheese, apple, bread, nuts, cake

Clues:
1. The drummer lives in house 1.
2. The Kenyan plays the drums.
3. The Peruvian lives directly right of the Kenyan.
4. The Peruvian lives in the white house.
5. The apple eater lives in the white house.
6. The pianist lives next to the drummer.
7. The Kenyan lives in the green house.
8. The Japanese lives in the red house, which is somewhere to the right of the white house.
9. The violinist lives in the red house.
10. The blue house is directly right of the red house.
11. The Spaniard lives in the blue house.
12. The Brazilian does not live next to the Japanese.
13. The cheese eater plays the drums.
14. The bread eater lives in the red house.
15. The flute player eats nuts.
16. The nuts eater lives in the blue house.

## Puzzle zebra/1/g5

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: grey, pink, black, orange, brown
- vehicle: tram, bike, van, bus, car
- pet: goat, snake, hen, pony, ferret
- drink: tea, wine, cocoa, cider, lemonade

Clues:
1. The van owner lives in the middle house.
2. The bus owner lives somewhere to the right of the van owner.
3. The car owner does not live next to the van owner.
4. The bike rider lives directly right of the tram rider.
5. The bus owner lives in the orange house.
6. The van owner lives in the black house.
7. The bike rider lives in the pink house.
8. The brown house is next to the orange house.
9. The hen owner drives the van.
10. The goat owner rides the tram.
11. The snake owner rides the bike.
12. The ferret owner does not live next to the hen owner.
13. The tea drinker owns the goat.
14. The wine drinker lives in the pink house.
15. The cocoa drinker owns the hen.
16. The lemonade drinker lives directly right of the cider drinker.

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

## Puzzle zebra/0/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Vera, Tess, Sam, Rhea, Uri
- hat: visor, beret, beanie, fedora, cap
- snack: bagel, olives, popcorn, grapes, fries
- city: Quito, Paris, Perth, Tunis, Delhi

Clues:
1. Sam lives in the middle house.
2. Vera lives in house 1.
3. Tess lives directly right of Vera.
4. Rhea lives next to Sam.
5. Sam wears the beanie.
6. The beret wearer lives directly left of the beanie wearer.
7. Uri wears the cap.
8. The fedora wearer lives next to the cap wearer.
9. The beret wearer eats olives.
10. The bagel eater wears the visor.
11. The fries eater wears the cap.
12. The grapes eater lives directly left of the fries eater.
13. The Parisian eats olives.
14. The Quito resident lives at one end of the street and does not wear the cap.
15. The Tunis resident lives next to Sam.
16. The Delhi resident eats fries.

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

## Puzzle zebra/1/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, blue, yellow, white
- nationality: Brit, Dane, German, Norwegian, Swede
- pet: dog, cat, bird, fish, horse
- drink: tea, coffee, milk, beer, water

Clues:
1. The green house is directly left of the yellow house.
2. The red house and the white house are at opposite ends of the row.
3. The blue house is next to the red house.
4. The green house is somewhere to the right of the red house.
5. The Brit lives in the red house.
6. The Dane lives in the blue house.
7. The German lives in the green house.
8. The Swede lives directly right of the German.
9. The cat owner lives next to the Brit.
10. The Swede keeps the fish.
11. The dog owner lives in the red house.
12. The horse is kept in one of the end houses.
13. The milk drinker lives in the middle house.
14. The Dane drinks coffee.
15. The beer drinker lives directly right of the milk drinker.
16. The water drinker lives next to the beer drinker.

## Puzzle zebra/1/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Italian, Japanese, Kenyan, Mexican, Polish
- drink: tea, coffee, juice, milk, soda
- car: Audi, Fiat, Ford, Mini, Volvo
- music: jazz, rock, folk, opera, blues

Clues:
1. The Mexican lives in the middle house.
2. There is exactly one house between the Kenyan and the Italian.
3. The Kenyan lives somewhere to the left of the Italian.
4. The Japanese lives next to the Italian.
5. The Mexican drinks coffee.
6. The tea drinker lives next to the Polish.
7. The Italian drinks soda.
8. The Japanese does not drink juice.
9. The Audi owner drinks soda.
10. The Mini owner drinks coffee.
11. The Fiat is directly left of the Mini.
12. The Ford owner lives next to the Audi owner.
13. The jazz fan lives directly right of the Polish.
14. The opera fan drinks milk.
15. The rock fan drives the Mini.
16. The blues fan lives somewhere to the right of the folk fan.

## Puzzle zebra/0/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Emil, Anna, Dara, Boris, Chen
- fruit: banana, cherry, pear, apple, grape
- hobby: golf, chess, archery, sailing, judo
- transport: bus, train, bike, tram, car

Clues:
1. Dara lives in the middle house.
2. Emil and Chen live at the two ends of the street.
3. Emil lives somewhere left of Anna.
4. Emil eats bananas.
5. Boris lives next to Chen.
6. The cherry eater lives next to the banana eater.
7. Dara eats pears.
8. The apple eater lives directly left of the grape eater.
9. The golfer eats bananas.
10. The sailor eats apples.
11. The archer lives directly left of the sailor.
12. The chess player eats cherries.
13. Emil takes the bus.
14. The train passenger lives directly right of the bus rider.
15. The tram rider eats apples.
16. The bike rider eats pears.
