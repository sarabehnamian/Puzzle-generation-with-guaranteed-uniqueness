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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_enc_encA\e2_enc_encA_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle zebra/3/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Thai, Mexican, Italian, Dane, Kenyan
- instrument: drums, piano, harp, cello, flute
- dessert: flan, cake, mousse, gelato, pie
- transport: tram, bike, ferry, scooter, bus

Clues:
1. The Mexican lives next to the Thai.
2. The Italian lives directly right of the Mexican.
3. The Kenyan lives in an end house.
4. The Dane lives somewhere to the right of the Italian.
5. The Dane does not live in an end house.
6. The Mexican plays the piano.
7. The cellist lives next to the Italian.
8. The flute player is Kenyan.
9. The drummer lives somewhere to the left of the harpist.
10. The cake lover plays the piano.
11. The mousse eater plays the harp.
12. The pie eater lives directly right of the gelato eater.
13. The bike rider eats cake.
14. The Dane rides the scooter.
15. The ferry passenger does not live in an end house.
16. The tram rider eats flan.

## Puzzle zebra/0/g5

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, judge, baker, tailor, nurse
- pet: owl, snake, pony, mouse, ferret
- drink: cider, cocoa, espresso, lemonade, soda
- flower: tulip, rose, orchid, lily, daisy

Clues:
1. The espresso drinker lives in the middle house.
2. The baker drinks espresso.
3. There is exactly one house between the farmer and the baker.
4. The tailor lives next to the baker.
5. The judge lives directly left of the baker.
6. The nurse lives somewhere right of the judge.
7. The baker owns the pony.
8. The snake owner lives directly right of the owl owner.
9. The mouse owner is the tailor.
10. The tailor drinks lemonade.
11. The cocoa drinker lives next to the espresso drinker.
12. The nurse does not drink cider.
13. The baker grows orchids.
14. The rose grower drinks cocoa.
15. The lily grower lives directly right of the orchid grower.
16. The tulip grower owns the owl.

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

## Puzzle zebra/2/g6

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Fay, Gus, Hal, Ida, Jon
- sport: tennis, golf, rowing, judo, skiing
- snack: chips, grapes, pretzel, olives, popcorn
- shirt: pink, gray, black, orange, purple

Clues:
1. Ida and Hal live in the two end houses.
2. Ida lives somewhere to the left of Gus.
3. Jon lives directly right of Gus.
4. Fay does not live next to Ida.
5. The skier lives in the middle house.
6. Ida is the rower.
7. The judoka lives next to the golfer.
8. Hal does not play golf.
9. The rower eats olives.
10. The tennis player eats chips.
11. The grape eater lives directly left of the pretzel eater.
12. The skier does not eat grapes.
13. The tennis player wears pink.
14. The golfer wears black.
15. The pretzel eater wears orange.
16. The olive eater does not wear gray.

## Puzzle zebra/1/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: cream, lilac, maroon, navy, orange
- job: baker, clerk, judge, nurse, pilot
- pet: ferret, gecko, koi, pigeon, tortoise
- drink: ale, cola, juice, tea, wine

Clues:
1. The clerk and the nurse live at opposite ends of the row.
2. The baker lives next to the judge.
3. The pilot lives somewhere to the right of the baker.
4. The nurse lives next to the pilot.
5. The judge lives in the cream house.
6. The baker lives in the orange house.
7. The cream house is directly right of the orange house.
8. The pilot lives in the lilac house.
9. The nurse does not live in the navy house.
10. The baker keeps the koi.
11. The tortoise owner lives next to the nurse.
12. The ferret owner lives in the cream house.
13. The pigeon owner is not the clerk.
14. The tea drinker keeps the koi.
15. The wine drinker lives in the lilac house.
16. The cola drinker lives in the middle house.
17. The clerk drinks ale.

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

## Puzzle zebra/2/g5

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, nurse, judge, tailor, farmer
- flower: rose, tulip, lily, daisy, orchid
- vehicle: bike, bus, tram, scooter, taxi
- drink: cocoa, lemonade, cider, smoothie, espresso

Clues:
1. The farmer lives directly left of the baker.
2. There is exactly one house between the nurse and the baker.
3. The tailor lives in house 5.
4. The judge lives somewhere to the right of the farmer.
5. The nurse lives in one of the end houses.
6. The baker grows tulips.
7. The nurse grows orchids.
8. The rose grower lives next to the orchid grower.
9. The judge grows lilies.
10. The nurse rides the tram.
11. The baker takes the taxi.
12. The bus rider lives next to the scooter rider.
13. The tailor does not ride the scooter.
14. The espresso drinker lives in the middle house.
15. The cocoa drinker rides the tram.
16. The lemonade drinker lives directly left of the smoothie drinker.
