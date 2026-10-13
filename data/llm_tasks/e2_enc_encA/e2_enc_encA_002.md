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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_enc_encA/e2_enc_encA_002.out.json with this exact structure
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

## Puzzle zebra/0/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, blue, yellow, white
- pet: dog, cat, fish, bird, horse
- drink: tea, coffee, milk, juice, water
- job: doctor, teacher, chef, pilot, artist

Clues:
1. The doctor lives in the leftmost house.
2. The yellow house is the far right house.
3. The green house is directly right of the blue house.
4. The white house is directly right of the green house.
5. The red house is next to the blue house.
6. The chef lives in the blue house.
7. The milk drinker lives in the middle house.
8. The fish owner drinks milk.
9. The pilot lives next to the artist.
10. The artist lives in the yellow house.
11. The cat lives directly right of the dog.
12. The pilot keeps the bird.
13. The pilot drinks juice.
14. The dog owner drinks tea.
15. The coffee drinker lives somewhere to the left of the water drinker.

## Puzzle zebra/0/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: amber, teal, pink, grey, brown
- instrument: piano, flute, harp, drums, cello
- snack: nuts, cake, pie, chips, cookie
- country: Peru, Cuba, Chad, Fiji, Iran

Clues:
1. The amber house is in the middle.
2. The pink house is not next to the amber house.
3. The teal house is directly left of the grey house.
4. The brown house is next to the amber house.
5. The grey house is not the rightmost house.
6. The Iranian lives directly left of the brown house.
7. The Peruvian lives next to the Iranian but not in the brown house.
8. The Cuban lives in the brown house.
9. The Fijian lives somewhere to the left of the Chadian.
10. The cello player is the Iranian.
11. The drummer is the Cuban.
12. The pianist and the harpist live next to each other.
13. The pianist lives in the grey house.
14. The person eating chips plays the drums.
15. The pie eater plays the harp.
16. The cookie eater is the Iranian.
17. The nut eater is not the Chadian.

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

## Puzzle zebra/3/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Gus, Hana, Ivan, Lena, Kai
- dance: tango, waltz, salsa, polka, swing
- gem: opal, ruby, topaz, onyx, pearl
- month: April, March, July, May, June

Clues:
1. Gus lives in the middle house.
2. Lena lives at one end of the row.
3. Ivan lives somewhere right of Gus.
4. Hana lives directly left of Ivan.
5. The waltz dancer lives next to Gus and is not Hana.
6. The polka dancer lives directly right of Gus.
7. The swing dancer lives at the far right end of the row.
8. Lena does not dance salsa.
9. The ruby is worn by the waltz dancer.
10. The topaz owner lives directly right of the ruby owner.
11. The pearl owner is the swing dancer.
12. The onyx owner does not live at either end of the row.
13. The person born in July owns the topaz.
14. The person born in June is the swing dancer.
15. The person born in March lives directly right of the person born in April.

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

## Puzzle zebra/2/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: Teal, Amber, Crimson, Violet, Ivory
- instrument: Drums, Violin, Harp, Flute, Piano
- fruit: Plum, Cherry, Mango, Lemon, Apple
- country: Chile, Norway, Kenya, Japan, Peru

Clues:
1. The ivory house is at the far right.
2. The violet house is directly left of the ivory house.
3. There is exactly one house between the teal house and the crimson house.
4. The crimson house is somewhere to the right of the teal house.
5. The piano player lives in the ivory house.
6. The flute player lives directly left of the piano player.
7. The harp player lives in the crimson house.
8. The violinist lives directly right of the drummer.
9. The apple eater is the piano player.
10. The mango eater is the harp player.
11. The lemon eater lives directly right of the mango eater.
12. The cherry eater is the violinist.
13. The Japanese resident lives in the violet house.
14. The Kenyan resident eats mango.
15. The Norwegian lives next to the Kenyan.
16. The Chilean lives directly left of the Norwegian.

## Puzzle zebra/1/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Italian, French, Greek, Polish, Dutch
- dish: soup, curry, salad, stew, noodles
- transport: bus, bike, tram, train, taxi
- door: red, blue, green, white, black

Clues:
1. The Dutch person lives in the middle house.
2. The Greek lives directly left of the Dutch person.
3. The French person lives next to the Italian.
4. The Italian lives somewhere to the right of the French person.
5. The Polish person eats curry.
6. The Dutch person eats soup.
7. The French person eats stew.
8. The Italian does not eat noodles.
9. The taxi passenger eats curry.
10. The bike rider eats noodles.
11. The bus rider is Dutch.
12. The tram rider lives somewhere to the right of the train rider.
13. The green door belongs to the bus rider.
14. The Polish person's door is white.
15. The black door is next to the white door.
16. The blue door is not the French person's.

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
