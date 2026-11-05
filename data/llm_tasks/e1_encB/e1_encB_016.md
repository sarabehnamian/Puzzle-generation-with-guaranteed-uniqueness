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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_016.out.json with this exact structure
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
1. The farmer and the pilot are next-door neighbours.
2. Tea is drunk by the person in the green house.
3. The occupant of the white house enjoys either cooking or tennis.
4. The purple house's occupant drinks coffee.
5. The baker lives in either the blue house or the purple house.
6. The hiking enthusiast does not live in the fourth house.
7. The farmer lives right beside the painting enthusiast.
8. The baker is a neighbour of the purple house's occupant.
9. The milk drinker and the teacher live two houses apart.
10. The tennis enthusiast lives in the third house.
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
1. The milk drinker lives in house 4.
2. The chess enthusiast is not in house 1.
3. The cat keeper lives somewhere to the right of the baker.
4. The milk drinker is the farmer.
5. The baker and the juice drinker are neighbours.
6. The pilot is the one who keeps the cat.
7. The dog keeper does not live next to the water drinker.
8. The water drinker lives immediately to the right of the golf enthusiast.
9. The horse is kept by the painting enthusiast.
10. The coffee drinker lives next door to the painting enthusiast.
11. The horse owner lives in the third house.
12. The bird owner lives in the house immediately left of the teacher's.
13. The chess enthusiast and the water drinker live two houses apart.
14. The hiking enthusiast lives in a lower-numbered house than the tennis enthusiast.

## Puzzle paraphrase:zebra-00184

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, dog, cat, bird
- color: purple, green, blue, white, red
- nationality: German, Dane, Norwegian, Spaniard, Brit
- drink: milk, water, coffee, cocoa, juice

Clues:
1. The Norwegian is the one who drinks water.
2. The cocoa drinker lives at one end of the row.
3. The Dane lives immediately to the left of the Spaniard.
4. The fish owner lives somewhere to the right of the horse owner.
5. The blue house is immediately to the left of the coffee drinker's house.
6. The Spaniard lives immediately to the left of the milk drinker.
7. One house lies between the coffee drinker and the white house.
8. The bird owner is either the Brit or the Dane.
9. The German drinks either coffee or juice.
10. The fish owner drinks coffee.
11. The red house is house 5.
12. One house separates the cat owner from the purple house.
13. The green house and the Spaniard are two houses apart.

## Puzzle paraphrase:zebra-00137

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Spaniard, Brit, Norwegian, German
- drink: milk, juice, coffee, cocoa, water
- hobby: cooking, golf, tennis, hiking, painting
- pet: horse, rabbit, fish, bird, cat

Clues:
1. The juice drinker lives immediately to the left of the Swede.
2. The Norwegian drinks coffee.
3. The German lives directly to the left of the hiking enthusiast.
4. The cooking enthusiast and the hiking enthusiast live two houses apart.
5. The bird is kept in the second house.
6. The water drinker lives immediately to the right of the German.
7. The rabbit owner is either the Brit or the Spaniard.
8. The cat owner lives somewhere to the right of the Spaniard.
9. The hiking enthusiast and the horse owner live next door to each other.
10. The tennis enthusiast lives in the second house.
11. The milk drinker lives next door to the Spaniard.
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
3. The red house is immediately left of the blue house.
4. The coffee drinker lives directly right of the pilot.
5. The juice drinker lives in the middle house, number 3.
6. The baker lives in house 2.
7. The chess enthusiast lives directly right of the pilot.
8. Two houses separate the chess enthusiast from the water drinker.
9. The green house's occupant lives next to the tea drinker.
10. The pilot lives somewhere to the right of the lawyer.
11. The pilot lives in either the green house or the white house.
12. The milk drinker enjoys hiking.
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

## Puzzle paraphrase:zebra-00168

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, fish, horse, bird, cat
- drink: cocoa, coffee, juice, milk, water
- job: pilot, doctor, lawyer, farmer, baker
- nationality: Dane, Brit, Norwegian, Swede, German

Clues:
1. One house separates the bird owner from the German.
2. The bird owner lives in a lower-numbered house than the pilot.
3. The lawyer lives immediately to the left of the baker.
4. The cocoa drinker lives immediately to the left of the baker.
5. The pilot lives immediately to the left of the Swede.
6. The horse owner lives in house 4.
7. The Dane is the coffee drinker.
8. The Brit lives directly to the left of the Dane.
9. The cat owner lives directly to the left of the water drinker.
10. The pilot keeps the fish.
11. The farmer keeps the horse.
12. The horse owner lives next door to the juice drinker.
