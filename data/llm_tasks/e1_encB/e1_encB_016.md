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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_016.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00111

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, water, juice, milk
- hobby: tennis, cooking, hiking, painting, golf
- color: white, blue, purple, green, red
- job: doctor, pilot, farmer, teacher, baker

Clues:
1. The farmer and the pilot live next door to each other.
2. The tea drinker lives in the green house.
3. The resident of the white house is into either cooking or tennis.
4. The coffee drinker lives in the purple house.
5. The baker's home is either the blue house or the purple house.
6. The hiking enthusiast does not live in the fourth house.
7. The farmer lives right beside the painting enthusiast.
8. The baker and the purple house's occupant are neighbours.
9. The milk drinker and the teacher live with exactly one house between them.
10. The tennis fan lives in the third house.
11. The cooking enthusiast lives in one of the two end houses.
12. The red house's occupant drinks water.
13. The hiking enthusiast lives immediately to the right of the pilot.
14. The cooking enthusiast lives directly to the left of the green house's occupant.
15. The farmer's hobby is either golf or hiking.

## Puzzle plain:zebra-00070

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, chess, golf, painting, hiking
- job: teacher, baker, doctor, farmer, lawyer
- pet: dog, fish, cat, bird, rabbit
- nationality: Spaniard, Norwegian, Dane, German, Swede

Clues:
1. The bird owner enjoys chess.
2. The doctor and the Norwegian are neighbours.
3. The German enjoys chess.
4. The person who enjoys golf and the Spaniard live two houses apart.
5. The lawyer lives next to the person who enjoys painting.
6. The cooking enthusiast is the Swede.
7. The Dane lives in the last house.
8. The person who keeps the fish lives in the second house.
9. The Dane and the lawyer live two houses apart.
10. There is exactly one house between the farmer and the Norwegian.
11. The painting enthusiast lives in a lower-numbered house than the Norwegian.
12. The owner of the dog and the teacher live two houses apart.
13. The person who keeps the cat does not live in the fourth house.

## Puzzle hard:zebra_hard-00059

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, chess, golf
- nationality: Swede, German, Brit, Dane, Norwegian
- drink: cocoa, water, juice, milk, tea
- job: baker, doctor, pilot, teacher, lawyer

Clues:
1. The pilot and the person who drinks tea are one and the same person.
2. If the doctor does not enjoy painting, then that person enjoys tennis.
3. The person who drinks milk lives somewhere between the baker and the person who drinks water.
4. The left-hand neighbour of the person who drinks juice is the Dane.
5. Neither the Norwegian nor the person who drinks water works as the doctor.
6. The right-hand neighbour of the painting enthusiast works as the teacher.
7. The German and the teacher are one and the same person.
8. Neither the doctor nor the person who drinks juice is the Swede.
9. The left-hand neighbour of the German drinks juice.
10. The cooking enthusiast lives two doors away from the pilot.
11. One of the neighbours of the German enjoys chess.
12. If the person who enjoys chess is not the Brit, then that person is the Dane.

## Puzzle paraphrase:zebra-00112

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, golf, hiking, chess
- pet: dog, bird, rabbit, cat, horse
- job: farmer, doctor, teacher, pilot, baker
- drink: coffee, milk, tea, juice, water

Clues:
1. House 4 belongs to the milk drinker.
2. The chess enthusiast is not in house 1.
3. The cat keeper lives somewhere to the right of the baker.
4. The milk drinker is the farmer.
5. The baker and the juice drinker live next door to each other.
6. The pilot is the one who keeps the cat.
7. The dog owner does not live next to the water drinker.
8. The water drinker lives immediately to the right of the golf enthusiast.
9. The painting enthusiast keeps the horse.
10. The coffee drinker lives right beside the painting enthusiast.
11. The horse is kept in the third house.
12. The bird owner lives directly to the left of the teacher.
13. The chess enthusiast and the water drinker have exactly one house between them.
14. The hiking enthusiast lives in a house numbered lower than the tennis enthusiast's.

## Puzzle paraphrase:zebra-00183

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, golf, chess
- color: green, blue, white, red, yellow
- job: farmer, pilot, baker, teacher, lawyer
- pet: dog, rabbit, bird, horse, cat

Clues:
1. The dog owner is not the pilot.
2. The red house's occupant has either the bird or the rabbit.
3. The rabbit belongs to the occupant of the blue house.
4. The golf enthusiast is not the teacher.
5. The cooking enthusiast and the pilot live in neighbouring houses.
6. The green house is home to the cat.
7. The golf enthusiast lives in either the red house or the white house.
8. The lawyer and the teacher have exactly one house between them.
9. The white house lies somewhere to the left of the horse owner.
10. The bird's owner lives somewhere to the right of the teacher.
11. The horse owner and the tennis enthusiast live two houses apart.
12. The yellow house is one of the two end houses.
13. The red house is immediately to the left of the painting enthusiast.
14. The farmer and the painting enthusiast are next-door neighbours.
15. One house separates the green house from the painting enthusiast.
16. The teacher lives somewhere to the left of the cat owner.
17. The cooking enthusiast lives in one of the two end houses.

## Puzzle paraphrase:zebra-00137

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Spaniard, Brit, Norwegian, German
- drink: milk, juice, coffee, cocoa, water
- hobby: cooking, golf, tennis, hiking, painting
- pet: horse, rabbit, fish, bird, cat

Clues:
1. The juice drinker lives directly to the left of the Swede.
2. The Norwegian is the coffee drinker.
3. The German lives directly to the left of the hiking enthusiast.
4. The cooking enthusiast and the hiking enthusiast are two houses apart.
5. The bird owner lives in the second house.
6. The water drinker lives immediately to the right of the German.
7. The rabbit owner is either the Brit or the Spaniard.
8. The cat owner lives somewhere to the right of the Spaniard.
9. The hiking enthusiast and the horse owner live next door to each other.
10. The tennis enthusiast lives in the second house.
11. The milk drinker lives right next to the Spaniard.
12. The Spaniard keeps either the fish or the rabbit.
13. The Swede is the golf enthusiast.

## Puzzle hard:zebra_hard-00090

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, Swede, German, Spaniard
- color: yellow, green, blue, red, white
- job: farmer, pilot, teacher, lawyer, baker
- drink: water, coffee, milk, juice, cocoa

Clues:
1. The pilot lives somewhere between the juice drinker and the lawyer.
2. One of the neighbours of the occupant of the red house drinks coffee.
3. The left-hand neighbour of the German drinks water.
4. Neither the person in the blue house nor the cocoa drinker works as the baker.
5. If the cocoa drinker is not the German, then that person is the Norwegian.
6. One of the neighbours of the cocoa drinker drinks coffee.
7. The right-hand neighbour of the Norwegian is the Swede.
8. Whoever lives in the green house and the teacher are one and the same person.
9. The occupant of the green house does not live in the second house from the right.
10. The right-hand neighbour of the coffee drinker is the Norwegian.
11. Exactly 4 houses lie to the left of the home of the lawyer.
12. Neither the baker nor the person in the green house is the Spaniard.
13. The right-hand neighbour of the baker drinks water.
14. The German and the person in the white house are one and the same person.

## Puzzle paraphrase:zebra-00143

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, cooking, chess, tennis, painting
- color: yellow, blue, green, red, white
- job: doctor, baker, pilot, farmer, lawyer
- drink: tea, coffee, water, juice, milk

Clues:
1. The juice drinker and the tennis enthusiast live two houses apart.
2. The chess enthusiast lives next door to the hiking enthusiast.
3. The red house's occupant lives immediately left of the blue house's occupant.
4. The coffee drinker lives directly right of the pilot.
5. The juice drinker lives in house 3.
6. The baker lives in house 2.
7. The chess enthusiast lives directly right of the pilot.
8. The chess enthusiast and the water drinker live two houses apart.
9. The green house's occupant lives next to the tea drinker.
10. The pilot lives somewhere to the right of the lawyer.
11. The pilot lives in either the green house or the white house.
12. Hiking is the hobby of the milk drinker.
13. The painting enthusiast lives immediately left of the farmer.

## Puzzle plain:zebra-00022

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, water, juice, tea, coffee
- pet: rabbit, cat, bird, horse, dog
- job: lawyer, pilot, farmer, teacher, doctor
- hobby: chess, cooking, painting, golf, hiking

Clues:
1. The owner of the rabbit enjoys chess.
2. The hiking enthusiast drinks cocoa.
3. The person who enjoys cooking lives in the house just left of the one where the coffee drinker lives.
4. The person who keeps the horse and the person who keeps the rabbit are not neighbours.
5. The tea drinker lives in the fifth house.
6. The dog owner lives in one of the two end houses.
7. The golf enthusiast and the juice drinker live two houses apart.
8. The doctor either keeps the bird or keeps the cat.
9. The person who keeps the bird lives in house 2.
10. The teacher lives in the house just left of the one where the cooking enthusiast lives.
11. The person who enjoys painting lives somewhere to the right of the pilot.
12. The juice drinker either works as the farmer or works as the lawyer.
13. The lawyer either enjoys chess or enjoys hiking.

## Puzzle paraphrase:zebra-00167

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, farmer, pilot, baker
- drink: juice, coffee, tea, cocoa, milk
- color: red, green, purple, yellow, white
- pet: fish, cat, horse, dog, bird

Clues:
1. The fish owner and the lawyer live two doors apart.
2. The purple house is immediately to the left of the tea drinker's house.
3. The coffee drinker lives next door to the dog owner.
4. The juice drinker and the white house's occupant live in neighbouring houses.
5. Milk is drunk by someone living in one of the two end houses.
6. The purple house is directly to the right of the white house.
7. The bird belongs to the coffee drinker.
8. The purple house is where the dog owner lives.
9. The cat is owned by the baker.
10. The doctor lives right beside the dog owner.
11. The green house and the red house have exactly one house between them.
12. The farmer lives immediately to the left of the purple house's occupant.
13. The green house is the middle one.
14. The green house's occupant and the horse owner are two houses apart.
