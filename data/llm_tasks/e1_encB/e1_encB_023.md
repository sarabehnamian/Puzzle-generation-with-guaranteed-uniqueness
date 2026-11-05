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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_023.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00192

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, juice, milk, coffee, cocoa
- job: lawyer, baker, teacher, farmer, pilot
- hobby: tennis, golf, hiking, painting, chess
- pet: horse, fish, cat, bird, dog

Clues:
1. The baker does not live next door to the fish owner.
2. The cat owner lives directly to the left of the milk drinker.
3. The painting enthusiast lives in the leftmost house.
4. The horse owner and the teacher live two houses apart.
5. The cat owner and the hiking enthusiast are two houses apart.
6. The hiking enthusiast lives next door to the horse keeper.
7. The dog owner is either the farmer or the lawyer.
8. The pilot's hobby is either chess or tennis.
9. The dog owner lives in the house immediately left of the tea drinker.
10. The lawyer and the tea drinker have exactly one house between them.
11. Somewhere to the right of the farmer lives the hiking enthusiast.
12. The cat owner lives directly to the left of the chess enthusiast.
13. The fish owner's house has a lower number than the horse owner's.
14. Exactly one house separates the lawyer from the pilot.
15. The hiking enthusiast drinks either cocoa or milk.
16. The coffee drinker lives in house 1.

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
1. The fish owner lives somewhere to the right of the red house.
2. The green house's occupant drinks juice.
3. The milk drinker lives at one end of the row.
4. The Dane and the red house's occupant live two houses apart.
5. The bird keeper drinks cocoa.
6. The bird keeper is either the Brit or the Dane.
7. The fish owner lives immediately to the right of the blue house.
8. The Brit lives in the house just left of the red house.
9. The rabbit owner lives in the yellow house.
10. The water drinker keeps the cat.
11. The German lives next door to the water drinker.
12. The Spaniard lives immediately to the right of the Swede.
13. The German and the green house's occupant are two houses apart.

## Puzzle paraphrase:zebra-00172

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, fish, cat, bird
- job: lawyer, pilot, doctor, baker, teacher
- nationality: Swede, Norwegian, German, Brit, Dane
- color: blue, yellow, white, red, purple

Clues:
1. The yellow house's occupant is the doctor.
2. The German is not next door to the pilot.
3. The cat owner lives in either the blue house or the white house.
4. The red house and the yellow house are two houses apart.
5. The dog owner lives immediately to the left of the yellow house.
6. The bird owner lives somewhere to the left of the Dane.
7. Exactly one house lies between the lawyer and the white house.
8. The teacher lives immediately to the left of the fish owner.
9. One house separates the Brit from the pilot.
10. The lawyer and the Norwegian have exactly one house between them.
11. The Brit and the Dane are not neighbours.
12. The rabbit owner lives in house 2.
13. The Norwegian lives immediately to the left of the purple house.

## Puzzle paraphrase:zebra-00124

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, yellow, blue, purple
- pet: rabbit, horse, fish, bird, cat
- drink: juice, cocoa, milk, coffee, tea
- job: farmer, pilot, lawyer, teacher, doctor

Clues:
1. The purple house's occupant and the teacher are next-door neighbours.
2. The cat owner lives directly to the right of the fish owner.
3. The bird owner lives somewhere to the right of the farmer.
4. The pilot keeps either the cat or the fish.
5. The rabbit owner drinks either coffee or tea.
6. The juice drinker lives next door to the purple house.
7. The pilot and the yellow house's occupant are neighbours.
8. The farmer lives directly to the right of the cat owner.
9. The coffee drinker lives in house 1.
10. The farmer and the rabbit owner live in adjacent houses.
11. One house separates the blue house from the pilot.
12. The doctor lives somewhere to the right of the cocoa drinker.
13. The bird owner and the purple house's occupant are not neighbours.
14. The red house's occupant is the pilot.

## Puzzle paraphrase:zebra-00180

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, cocoa, water, milk
- pet: dog, bird, horse, fish, rabbit
- color: yellow, red, green, blue, white
- job: farmer, doctor, lawyer, baker, pilot

Clues:
1. Whoever drinks tea is the pilot.
2. The green house stands somewhere to the right of the doctor's house.
3. The dog's owner drinks water.
4. The horse owner lives right next door to the left of the rabbit owner.
5. The tea drinker is in house 4.
6. The cocoa drinker is not the one who keeps the rabbit.
7. The baker lives next to the white house.
8. The cocoa drinker and the lawyer live two houses apart.
9. The fish owner lives immediately to the left of the red house.
10. The bird is kept in house 2.
11. Exactly one house separates the white house from the yellow house.
12. The yellow house's occupant drinks coffee.
13. The dog owner does not live in house 5.
14. The farmer lives in house 5.

## Puzzle paraphrase:zebra-00109

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Norwegian, Swede, Spaniard, German
- job: doctor, baker, lawyer, farmer, pilot
- hobby: golf, hiking, painting, cooking, chess
- pet: fish, dog, cat, rabbit, horse

Clues:
1. The chess enthusiast lives in house 4.
2. The doctor's hobby is cooking.
3. The painting enthusiast lives immediately to the left of the hiker.
4. The Brit and the Spaniard live next door to each other.
5. The rabbit owner is the farmer.
6. The pilot lives immediately to the right of the baker.
7. One house lies between the farmer and the Norwegian.
8. The baker lives somewhere to the left of the horse owner.
9. The hiker keeps the dog.
10. The fish owner lives immediately to the left of the baker.
11. The lawyer lives immediately to the left of the German.
12. The fish owner is not the Spaniard.

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
