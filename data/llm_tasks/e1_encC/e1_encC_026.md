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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_026.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00129

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, cocoa, water, tea, coffee
- hobby: chess, painting, cooking, tennis, golf
- color: purple, blue, yellow, red, green
- job: lawyer, doctor, pilot, farmer, baker

Clues:
1. The doctor lives directly to the left of the red house.
2. The tea drinker lives immediately to the right of the milk drinker.
3. The baker lives directly to the left of the yellow house.
4. The coffee drinker and the tennis enthusiast have exactly one house between them.
5. The coffee drinker does not live next door to the golf enthusiast.
6. The green house stands immediately to the left of the yellow house.
7. The yellow house's occupant is the lawyer.
8. The coffee drinker lives somewhere to the left of the blue house.
9. The golf enthusiast lives in either the purple house or the yellow house.
10. The pilot lives further to the left than the farmer.
11. The cocoa drinker lives next door to the cooking enthusiast.
12. The coffee drinker lives immediately to the right of the water drinker.
13. The blue house is at one end of the row.
14. The painting enthusiast lives directly to the left of the milk drinker.

## Puzzle paraphrase:zebra-00121

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, blue, yellow, purple
- hobby: cooking, golf, chess, tennis, hiking
- pet: fish, bird, horse, cat, dog
- nationality: Spaniard, Dane, Brit, Swede, German

Clues:
1. The dog owner and the keeper of the fish live next door to each other.
2. The hiking enthusiast lives right beside the Swede.
3. The Brit and the golf enthusiast have exactly one house between them.
4. The horse owner lives in the fifth house.
5. The Dane and the person in the yellow house are next-door neighbours.
6. The Swede's home adjoins the white house.
7. The fish keeper and the golf enthusiast live side by side.
8. The person in the purple house is the golf enthusiast.
9. The chess enthusiast is either the German or the Swede.
10. The German lives immediately to the right of the yellow house's occupant.
11. The bird owner lives in the blue house.
12. The Spaniard is the one who enjoys cooking.
13. The cooking enthusiast lives in the white house.

## Puzzle hard:zebra_hard-00044

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, tea, juice, coffee, cocoa
- job: teacher, doctor, pilot, farmer, baker
- pet: dog, fish, cat, rabbit, horse
- color: purple, green, yellow, white, red

Clues:
1. Exactly 4 houses lie to the left of the home of the cocoa drinker.
2. The doctor and the tea drinker are one and the same person.
3. The baker lives somewhere between the person who drinks juice and the water drinker.
4. The person who keeps the cat is not the same person as the pilot.
5. The owner of the horse and the teacher are one and the same person.
6. The occupant of the green house and the person who drinks juice are one and the same person.
7. The pilot lives somewhere between the owner of the rabbit and the water drinker.
8. If the occupant of the yellow house does not drink coffee, then that person drinks tea.
9. One of the neighbours of the pilot keeps the dog.
10. The owner of the dog lives two doors away from whoever lives in the purple house.
11. The doctor lives somewhere between the owner of the rabbit and the occupant of the white house.
12. The dog owner does not live to the right of the cat owner.

## Puzzle paraphrase:zebra-00145

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, chess, painting, hiking, tennis
- job: doctor, baker, farmer, pilot, teacher
- pet: rabbit, fish, bird, dog, cat
- drink: milk, water, coffee, juice, tea

Clues:
1. The farmer drinks water.
2. The doctor lives next to the tea drinker.
3. The juice drinker and the milk drinker are neighbours.
4. The chess enthusiast lives immediately left of the dog owner.
5. The juice drinker lives directly right of the golf enthusiast.
6. The rabbit owner lives in house 1.
7. The doctor lives in house 4.
8. The fish keeper's hobby is hiking.
9. The pilot lives immediately left of the hiking enthusiast.
10. The teacher lives immediately right of the pilot.
11. The pilot lives directly right of the chess enthusiast.
12. The cat owner lives next door to the golf enthusiast.
13. The tennis enthusiast is the pilot.

## Puzzle hard:zebra_hard-00048

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, blue, white, purple, red
- hobby: golf, tennis, chess, painting, hiking
- drink: cocoa, coffee, juice, tea, water
- nationality: German, Swede, Spaniard, Dane, Norwegian

Clues:
1. The left-hand neighbour of the tea drinker enjoys hiking.
2. The person who enjoys golf and the occupant of the white house are one and the same person.
3. One of the neighbours of the Spaniard is the Swede.
4. Exactly one house separates the person who drinks water from whoever lives in the white house.
5. The German lives two doors away from the Spaniard.
6. The person who enjoys hiking lives two doors away from whoever lives in the purple house.
7. The person who enjoys chess lives somewhere between the German and the person in the white house.
8. The right-hand neighbour of the Dane lives in the blue house.
9. The person who enjoys chess and the coffee drinker are one and the same person.
10. The tennis enthusiast and the water drinker are one and the same person.
11. The Swede and whoever lives in the yellow house are one and the same person.
12. The person in the blue house and the person who drinks juice are one and the same person.

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

## Puzzle paraphrase:zebra-00181

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Dane, Swede, Spaniard
- color: white, green, yellow, blue, purple
- job: doctor, baker, farmer, teacher, lawyer
- pet: cat, dog, rabbit, horse, fish

Clues:
1. The blue house and the dog owner's house are neighbours.
2. The doctor lives in the yellow house.
3. The Norwegian has the rabbit.
4. The doctor is not in house 5.
5. The Dane occupies house 2.
6. The green house is where the horse is kept.
7. The farmer lives next door to the Norwegian.
8. The dog belongs to whoever lives in the purple house.
9. The horse lives in house 3.
10. The lawyer's house is immediately to the right of the blue house.
11. The Spaniard occupies house 4.
12. The Swede lives immediately to the left of the baker.
13. The fish owner lives next door to the Norwegian.

## Puzzle plain:zebra-00086

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, water, coffee, juice, tea
- pet: horse, cat, dog, rabbit, fish
- hobby: painting, cooking, hiking, chess, golf
- nationality: Brit, Norwegian, German, Swede, Spaniard

Clues:
1. The Norwegian lives in house 4.
2. The fish owner lives in a lower-numbered house than the person who drinks cocoa.
3. The juice drinker lives in house 2.
4. The golf enthusiast lives in the house just left of the one where the chess enthusiast lives.
5. The person who enjoys hiking either is the German or is the Spaniard.
6. The horse owner is the Spaniard.
7. The owner of the rabbit is the Swede.
8. The person who enjoys chess lives next to the person who drinks cocoa.
9. The Brit lives directly to the left of the owner of the fish.
10. The person who drinks coffee and the water drinker live two houses apart.
11. The Brit and the person who enjoys golf live in adjacent houses.
12. The Spaniard drinks water.
13. The person who keeps the dog enjoys cooking.
14. The water drinker lives in a lower-numbered house than the coffee drinker.

## Puzzle hard:zebra_hard-00030

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, juice, water, milk
- color: white, red, blue, yellow, green
- job: lawyer, teacher, pilot, farmer, doctor
- nationality: Swede, Dane, Norwegian, Brit, German

Clues:
1. The occupant of the white house has only one neighbour.
2. The occupant of the yellow house lives somewhere between the person who drinks milk and the person in the red house.
3. The juice drinker and the occupant of the yellow house are one and the same person.
4. The doctor is not the same person as the person who drinks tea.
5. The left-hand neighbour of the pilot is the Brit.
6. None of the neighbours of the person in the red house lives in the green house.
7. The Brit and the person who drinks tea are one and the same person.
8. The water drinker lives further to the right than the Norwegian.
9. Whoever lives in the red house lives in the fifth house from the right.
10. The Dane and the teacher are one and the same person.
11. The Dane and the person in the yellow house are one and the same person.
12. One of the neighbours of the doctor is the German.
13. The left-hand neighbour of the lawyer lives in the yellow house.
14. The right-hand neighbour of the person who drinks juice drinks water.

## Puzzle paraphrase:zebra-00133

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Spaniard, Swede, German, Dane
- drink: tea, water, juice, milk, cocoa
- pet: horse, rabbit, dog, cat, bird
- job: doctor, lawyer, farmer, teacher, baker

Clues:
1. The dog belongs to the Swede.
2. The baker lives directly to the left of the horse owner.
3. The Swede is the one who drinks milk.
4. The bird owner and the Swede live in neighbouring houses.
5. The lawyer is the one who owns the bird.
6. The doctor is either the Dane or the Swede.
7. The farmer lives immediately to the left of the dog owner.
8. The lawyer lives somewhere further left than the cocoa drinker.
9. The German lives directly to the left of the juice drinker.
10. One house separates the Norwegian from the Swede.
11. The doctor lives in the fifth house.
12. The farmer drinks water.
13. The cat's owner is the baker.
