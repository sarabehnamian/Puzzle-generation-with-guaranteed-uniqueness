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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_023.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00191

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, golf, cooking, chess, tennis
- job: pilot, baker, lawyer, teacher, farmer
- pet: horse, bird, fish, cat, dog
- nationality: Norwegian, Swede, Spaniard, Brit, Dane

Clues:
1. The Dane and the dog owner are next-door neighbours.
2. The horse owner lives immediately to the right of the chess enthusiast.
3. The tennis enthusiast is the pilot.
4. The cat owner lives next door to the Swede.
5. The house directly to the right of the Swede's is the horse owner's.
6. The lawyer is the one who keeps the bird.
7. The teacher lives somewhere to the right of the pilot.
8. The cooking enthusiast is the farmer.
9. The painting enthusiast has the cat.
10. The dog owner's house is immediately to the right of the horse owner's.
11. The Spaniard is the cooking enthusiast.
12. The tennis enthusiast keeps the horse.
13. The Brit is the pilot.

## Puzzle hard:zebra_hard-00098

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: cat, horse, rabbit, bird, dog
- color: blue, white, yellow, purple, green
- drink: milk, tea, water, cocoa, coffee
- nationality: Norwegian, Swede, German, Brit, Dane

Clues:
1. The Dane lives two doors away from the person who drinks water.
2. Neither whoever lives in the blue house nor the Norwegian drinks milk.
3. The right-hand neighbour of the tea drinker is the Dane.
4. Exactly 0 houses lie to the left of the home of the occupant of the blue house.
5. The Brit and the person who drinks coffee are one and the same person.
6. Exactly one house separates the person in the blue house from whoever lives in the green house.
7. Exactly 0 houses lie to the left of the home of the owner of the rabbit.
8. The left-hand neighbour of the owner of the bird is the Norwegian.
9. The German lives in the fifth house from the right.
10. Exactly one house separates the Norwegian from whoever lives in the purple house.
11. One of the neighbours of the dog owner keeps the horse.
12. One of the neighbours of the horse owner keeps the cat.
13. The Brit and the person who keeps the dog are one and the same person.
14. The Norwegian and the occupant of the white house are one and the same person.

## Puzzle plain:zebra-00021

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Brit, Spaniard, Norwegian, Swede
- job: farmer, baker, doctor, pilot, lawyer
- pet: fish, rabbit, dog, cat, horse
- color: yellow, blue, green, white, red

Clues:
1. The occupant of the white house works as the farmer.
2. The occupant of the white house lives at one end of the row.
3. The fish owner either is the Norwegian or is the Spaniard.
4. Whoever lives in the blue house and the fish owner are neighbours.
5. The cat owner lives in the second house.
6. The pilot is the Swede.
7. The person who keeps the dog lives directly to the left of the cat owner.
8. The German keeps the horse.
9. The doctor lives in the last house.
10. The fish owner lives next to the Spaniard.
11. The owner of the fish either lives in the blue house or lives in the green house.
12. There is exactly one house between the German and the lawyer.
13. Whoever lives in the red house lives in the house just left of the one where the baker lives.

## Puzzle paraphrase:zebra-00196

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, bird, rabbit, fish
- nationality: German, Swede, Dane, Brit, Spaniard
- drink: water, milk, juice, coffee, cocoa
- color: red, white, green, yellow, blue

Clues:
1. The fish owner lives somewhere to the right of the red house's occupant.
2. The green house's resident drinks juice.
3. The milk drinker lives at one end of the row.
4. The Dane and the red house's resident are two houses apart.
5. The bird owner drinks cocoa.
6. The bird owner is either the Brit or the Dane.
7. The fish owner lives immediately to the right of the blue house's resident.
8. The Brit's house is just to the left of the red house.
9. The yellow house is home to the rabbit owner.
10. The cat belongs to the water drinker.
11. The German lives right next to the water drinker.
12. The Spaniard lives immediately to the right of the Swede.
13. The German and the green house's resident are two houses apart.

## Puzzle paraphrase:zebra-00171

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, German, Spaniard, Swede
- color: blue, purple, white, green, yellow
- drink: coffee, cocoa, tea, water, milk
- job: baker, farmer, lawyer, doctor, pilot

Clues:
1. The Dane is the one who drinks tea.
2. The occupant of the blue house is either the Dane or the German.
3. The milk drinker is next door to the pilot.
4. The Dane and the Spaniard live in adjacent houses.
5. The Norwegian lives beside the occupant of the purple house.
6. The occupant of the yellow house is either the Dane or the Swede.
7. The doctor drinks either coffee or water.
8. The Swede occupies house 1.
9. The pilot is not the person in the green house.
10. The farmer's house has a lower number than the green house's.
11. The Norwegian and the water drinker are next-door neighbours.
12. The milk drinker lives in one of the two end houses.
13. The farmer lives further to the left than the occupant of the yellow house.
14. Cocoa is not what the person in the green house drinks.
15. The baker lives next to whoever is in the white house.
16. The doctor and the Spaniard live side by side.

## Puzzle paraphrase:zebra-00124

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, yellow, blue, purple
- pet: rabbit, horse, fish, bird, cat
- drink: juice, cocoa, milk, coffee, tea
- job: farmer, pilot, lawyer, teacher, doctor

Clues:
1. The purple house's occupant lives right beside the teacher.
2. The cat owner lives directly to the right of the fish owner.
3. The bird owner lives somewhere to the right of the farmer.
4. The pilot keeps either the cat or the fish.
5. The rabbit owner drinks either coffee or tea.
6. The juice drinker lives next door to the purple house.
7. The pilot lives next door to the yellow house.
8. The farmer lives directly to the right of the cat owner.
9. The coffee drinker lives in the first house.
10. The farmer and the rabbit owner are next-door neighbours.
11. One house lies between the blue house and the pilot.
12. The doctor lives somewhere to the right of the cocoa drinker.
13. The bird owner does not live next door to the purple house.
14. The red house's occupant is the pilot.

## Puzzle paraphrase:zebra-00179

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Dane, Swede, Spaniard, Brit
- color: yellow, blue, red, green, white
- drink: cocoa, tea, coffee, water, juice
- job: lawyer, doctor, baker, pilot, farmer

Clues:
1. The German does not live next door to the water drinker.
2. The tea drinker lives immediately to the left of the red house's occupant.
3. The Dane occupies the first house.
4. The baker lives at one of the two ends of the row.
5. The farmer is a neighbour of the German.
6. The lawyer is the tea drinker.
7. The green house's occupant and the juice drinker are two houses apart.
8. The pilot is the one in the blue house.
9. The red house and the yellow house have exactly one house between them.
10. The Brit is the farmer.
11. The Spaniard lives immediately to the right of the white house's occupant.
12. The Brit lives at one end of the row.
13. The Brit lives somewhere to the right of the cocoa drinker.
14. The occupant of the red house drinks coffee.

## Puzzle paraphrase:zebra-00109

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Norwegian, Swede, Spaniard, German
- job: doctor, baker, lawyer, farmer, pilot
- hobby: golf, hiking, painting, cooking, chess
- pet: fish, dog, cat, rabbit, horse

Clues:
1. The chess enthusiast lives in house 4.
2. The doctor's hobby is cooking.
3. The painting enthusiast lives immediately to the left of the hiking enthusiast.
4. The Brit and the Spaniard are next-door neighbours.
5. The rabbit owner is the farmer.
6. The pilot lives immediately to the right of the baker.
7. The farmer and the Norwegian have exactly one house between them.
8. The baker lives somewhere to the left of the horse owner.
9. The hiking enthusiast keeps the dog.
10. The fish owner lives immediately to the left of the baker.
11. The lawyer lives immediately to the left of the German.
12. The Spaniard does not own the fish.

## Puzzle plain:zebra-00009

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, tennis, golf
- pet: rabbit, dog, cat, bird, fish
- color: red, yellow, blue, purple, green
- drink: juice, water, milk, tea, coffee

Clues:
1. The person who drinks coffee and the tea drinker live two houses apart.
2. The cat owner and the person in the purple house live in adjacent houses.
3. The owner of the cat lives in the fourth house.
4. The person who drinks tea lives somewhere to the right of the occupant of the blue house.
5. The fish owner lives in the leftmost house.
6. The occupant of the green house enjoys chess.
7. The occupant of the green house either drinks coffee or drinks milk.
8. The tennis enthusiast either keeps the cat or keeps the dog.
9. There is exactly one house between the person who enjoys golf and the person in the green house.
10. The person who drinks juice enjoys cooking.
11. The person who drinks juice keeps the rabbit.
12. The person who drinks milk either keeps the cat or keeps the dog.
13. The person in the red house lives directly to the left of the tea drinker.
14. The water drinker keeps the cat.

## Puzzle hard:zebra_hard-00061

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, bird, dog, horse
- hobby: tennis, golf, hiking, cooking, chess
- color: green, blue, red, yellow, white
- drink: water, coffee, juice, milk, tea

Clues:
1. Exactly 1 house lies to the left of the home of the person who drinks tea.
2. The person who enjoys golf lives somewhere between the person who drinks coffee and the horse owner.
3. The person in the blue house and the juice drinker are one and the same person.
4. One of the neighbours of the person who keeps the cat enjoys chess.
5. Whoever lives in the blue house and the person who enjoys cooking are one and the same person.
6. One of the neighbours of the person who enjoys cooking lives in the white house.
7. The person who enjoys hiking lives two doors away from the occupant of the red house.
8. One of the neighbours of the occupant of the white house drinks milk.
9. The left-hand neighbour of the chess enthusiast drinks water.
10. The owner of the cat and whoever lives in the red house are one and the same person.
11. Exactly one house separates the person who keeps the fish from the person in the green house.
12. One of the neighbours of the owner of the dog enjoys chess.
