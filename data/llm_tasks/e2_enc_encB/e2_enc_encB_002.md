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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_enc_encB\e2_enc_encB_002.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/1/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, blue, yellow, ivory
- nationality: Spanish, English, Ukrainian, Norwegian, Japanese
- pet: dog, snails, fox, horse, zebra
- drink: coffee, tea, milk, juice, water

Clues:
1. The Spaniard lives in the red house.
2. The Englishman drinks milk.
3. The milk drinker lives in the ivory house.
4. The ivory house is directly right of the red house.
5. The Norwegian lives in the yellow house, which is at one end of the row.
6. The Ukrainian drinks coffee.
7. The coffee drinker lives in the blue house.
8. The blue house is directly right of the ivory house.
9. The Japanese lives next to the Norwegian.
10. The green house is somewhere to the right of the red house.
11. The tea drinker lives next to the milk drinker.
12. The Japanese does not drink water.
13. The Englishman keeps the dog.
14. The fox is kept by the water drinker.
15. The horse owner lives directly left of the zebra owner.

## Puzzle zebra/2/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: ivory, maroon, teal, orange, black
- pet: goat, duck, mouse, snake, pony
- drink: cola, tea, juice, milk, beer
- job: vet, cook, poet, clerk, mason

Clues:
1. The poet lives in the ivory house.
2. The beer drinker is the poet.
3. The ivory house is in the middle of the row.
4. The orange house is directly right of the ivory house.
5. The teal house is next to the ivory house.
6. The mason lives in the maroon house.
7. The vet lives in the black house.
8. The vet lives somewhere to the right of the mason.
9. The clerk lives in the teal house.
10. The cook drinks milk.
11. The cola drinker lives next to the beer drinker.
12. The juice drinker lives directly right of the milk drinker.
13. The goat owner drinks cola.
14. The mouse owner is the vet.
15. The pony owner lives in the orange house.
16. The mason does not own the duck.

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

## Puzzle zebra/3/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: maroon, navy, ivory, olive, coral
- pet: snake, ferret, hamster, turtle, parrot
- drink: tea, cider, wine, beer, cola
- hobby: fishing, chess, gardening, knitting, diving

Clues:
1. The navy house is next to the ivory house.
2. The olive house is directly right of the ivory house.
3. The coral house is at the right-hand end.
4. The maroon house is not next to the olive house.
5. The wine drinker lives in the ivory house.
6. The tea drinker lives in the maroon house.
7. The cider drinker lives in the navy house.
8. The beer drinker lives next to the wine drinker.
9. The hamster owner drinks wine.
10. The parrot owner drinks cola.
11. The snake owner drinks tea.
12. The turtle owner lives somewhere to the right of the ferret owner.
13. The fisher drinks tea.
14. The diver lives in the coral house.
15. The chess player drinks cider.
16. The knitter keeps the turtle.

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

## Puzzle zebra/1/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, blue, green, yellow, purple
- job: doctor, chef, pilot, teacher, artist
- pet: dog, cat, rabbit, parrot, turtle
- hobby: chess, golf, painting, reading, cycling

Clues:
1. The red house is in the middle.
2. The pilot lives in the red house.
3. The chef lives directly left of the doctor.
4. The teacher lives somewhere to the right of the pilot.
5. The artist does not live next to the pilot.
6. The chef lives in the yellow house.
7. The purple house is directly right of the yellow house.
8. The artist does not live in the blue house.
9. The dog lives directly left of the red house.
10. The parrot lives in the green house.
11. The cat owner lives next to the parrot owner.
12. The turtle is not in an end house.
13. The artist's hobby is painting.
14. The golfer lives in the red house.
15. The reader keeps the cat.
16. The chess player lives somewhere to the left of the cyclist.

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

## Puzzle zebra/3/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: yellow, blue, red, white, green
- pet: cat, dog, bird, horse, fish
- drink: water, tea, milk, coffee, juice
- job: pilot, artist, doctor, chef, teacher

Clues:
1. The milk drinker lives in the middle house.
2. The doctor lives in the red house.
3. The dog owner drinks tea.
4. The green house is house 5.
5. The white house is directly left of the green house.
6. The coffee drinker lives in the white house.
7. The bird owner drinks milk.
8. The chef owns the horse.
9. The fish owner lives in the green house.
10. The yellow house is not next to the red house.
11. The pilot lives somewhere to the left of the doctor.
12. The pilot lives in the yellow house.
13. The teacher drinks juice.
14. The artist lives next to the pilot.
15. The cat owner lives in house 1.
