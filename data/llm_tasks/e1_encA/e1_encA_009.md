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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_009.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00107

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, hiking, tennis, cooking
- pet: bird, dog, fish, rabbit, cat
- nationality: German, Dane, Brit, Swede, Spaniard
- job: lawyer, teacher, doctor, pilot, baker

Clues:
1. The Brit is the teacher.
2. The Dane lives next door to the Spaniard.
3. The Swede lives immediately to the left of the fish owner.
4. The hiker lives in the last house.
5. The fish owner lives next door to the lawyer.
6. The golf enthusiast lives immediately to the right of the cooking enthusiast.
7. One house separates the cat owner from the hiker.
8. One house lies between the pilot and the tennis enthusiast.
9. The hiker lives next door to the Spaniard.
10. The doctor lives immediately to the left of the lawyer.
11. The Dane keeps the bird.
12. The chess enthusiast lives in the fourth house.
13. The doctor and the rabbit owner are neighbours.

## Puzzle plain:zebra-00040

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, cocoa, water, tea
- hobby: golf, tennis, chess, hiking, painting
- job: farmer, baker, lawyer, pilot, teacher
- nationality: Dane, German, Brit, Norwegian, Swede

Clues:
1. There is exactly one house between the Dane and the teacher.
2. The person who drinks cocoa enjoys painting.
3. The farmer and the tea drinker live in adjacent houses.
4. The Brit lives in house 2.
5. The pilot and the person who drinks tea are not neighbours.
6. The farmer enjoys chess.
7. The person who drinks cocoa is the Norwegian.
8. The Dane and the farmer live in adjacent houses.
9. The Dane lives in house 4.
10. The milk drinker lives in the house just left of the one where the person who enjoys golf lives.
11. The farmer and the lawyer live two houses apart.
12. The tea drinker lives next to the water drinker.
13. The German lives immediately to the right of the person who enjoys tennis.
14. The Norwegian lives in house 5.
15. The pilot lives in one of the two end houses.

## Puzzle plain:zebra-00090

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Spaniard, Dane, Swede, Brit
- job: farmer, doctor, pilot, baker, teacher
- color: purple, red, white, yellow, green
- pet: bird, rabbit, horse, cat, fish

Clues:
1. There is exactly one house between the bird owner and the Swede.
2. The fish owner lives immediately to the right of the Brit.
3. The pilot lives in house 2.
4. The farmer lives in the house just left of the one where the Spaniard lives.
5. The doctor either is the Dane or is the Norwegian.
6. The Norwegian lives next to the occupant of the purple house.
7. The occupant of the purple house lives immediately to the right of the baker.
8. The person who keeps the fish and the owner of the horse live in adjacent houses.
9. The owner of the fish lives immediately to the right of the person in the yellow house.
10. The owner of the cat and the doctor live in adjacent houses.
11. The Spaniard lives directly to the left of the doctor.
12. The person in the green house either is the Dane or is the Spaniard.
13. Whoever lives in the green house and the occupant of the red house live two houses apart.

## Puzzle hard:zebra_hard-00065

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, teacher, baker, doctor, lawyer
- hobby: hiking, cooking, painting, golf, chess
- nationality: Dane, Brit, Swede, German, Spaniard
- drink: coffee, juice, cocoa, tea, water

Clues:
1. The baker lives somewhere between the juice drinker and the teacher.
2. If the German does not enjoy cooking, then that person enjoys golf.
3. Neither the golf enthusiast nor the Spaniard works as the lawyer.
4. Exactly one house separates the baker from the Spaniard.
5. The baker and the person who enjoys golf are one and the same person.
6. The chess enthusiast lives in the fifth house from the right.
7. The right-hand neighbour of the person who enjoys painting drinks water.
8. The right-hand neighbour of the Brit is the German.
9. The left-hand neighbour of the coffee drinker enjoys golf.
10. Exactly 0 houses lie to the left of the home of the farmer.
11. The person who drinks coffee and the German are one and the same person.
12. The left-hand neighbour of the person who drinks cocoa is the Dane.
13. The left-hand neighbour of the juice drinker drinks tea.

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

## Puzzle plain:zebra-00079

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, tennis, cooking, golf, chess
- color: purple, yellow, green, white, blue
- pet: bird, dog, cat, fish, rabbit
- job: doctor, baker, pilot, farmer, lawyer

Clues:
1. The person who keeps the fish lives immediately to the right of the person who keeps the dog.
2. The pilot lives directly to the left of the farmer.
3. The pilot and the owner of the rabbit live two houses apart.
4. The occupant of the yellow house either works as the baker or works as the pilot.
5. The farmer lives somewhere to the right of the occupant of the purple house.
6. The fish owner either enjoys chess or enjoys golf.
7. The person in the blue house either works as the farmer or works as the pilot.
8. The person in the purple house does not live in house 2.
9. The baker enjoys hiking.
10. The person who keeps the rabbit lives in a lower-numbered house than the person who keeps the cat.
11. The occupant of the white house is not the lawyer.
12. The person who enjoys cooking lives immediately to the right of the fish owner.
13. The golf enthusiast lives in the house just left of the one where the person in the purple house lives.
14. The pilot and the person in the white house live two houses apart.
15. The person who enjoys tennis either lives in the blue house or lives in the green house.

## Puzzle hard:zebra_hard-00020

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, fish, bird, rabbit
- nationality: Spaniard, Brit, German, Dane, Swede
- drink: water, tea, coffee, cocoa, milk
- color: white, yellow, purple, blue, red

Clues:
1. The person who keeps the bird lives two doors away from the occupant of the purple house.
2. The left-hand neighbour of the cat owner lives in the red house.
3. The person who drinks cocoa and the Dane are one and the same person.
4. The owner of the fish and the person who drinks tea are one and the same person.
5. The person who drinks water has only one neighbour.
6. The Brit lives in the fifth house from the right.
7. Neither the bird owner nor whoever lives in the red house is the Dane.
8. The person who drinks water lives further to the right than the person in the yellow house.
9. The person who drinks coffee and the person in the yellow house are one and the same person.
10. Whoever lives in the blue house lives in the fifth house from the right.
11. The person who drinks milk lives somewhere between the person who drinks water and the occupant of the yellow house.
12. One of the neighbours of the German is the Brit.
13. The Swede lives somewhere between the bird owner and the owner of the horse.

## Puzzle paraphrase:zebra-00182

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, horse, dog, bird
- nationality: Swede, Brit, German, Spaniard, Norwegian
- hobby: tennis, golf, hiking, painting, cooking
- color: blue, green, yellow, white, red

Clues:
1. The tennis fan lives immediately to the right of the green house.
2. The Brit occupies the leftmost house.
3. The cooking enthusiast lives in house 3.
4. The dog owner lives right next door to the right of the white house.
5. The cat owner lives next to the cooking enthusiast.
6. The Spaniard keeps the bird.
7. The Swede is the cat's owner.
8. The Spaniard's hobby is hiking.
9. One house lies between the blue house and the cooking enthusiast.
10. The tennis enthusiast lives in the fifth house.
11. The red house and the white house are not next to each other.
12. The horse owner lives immediately to the left of the Spaniard.
13. The Norwegian and the painter live two houses apart.

## Puzzle paraphrase:zebra-00151

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, juice, milk, cocoa
- color: red, green, yellow, blue, purple
- nationality: Swede, Spaniard, Brit, Dane, Norwegian
- job: teacher, lawyer, farmer, pilot, baker

Clues:
1. The lawyer lives in the red house.
2. The baker lives somewhere to the right of the Swede.
3. The Brit lives in one of the end houses.
4. The Norwegian lives right next door to the right of the milk drinker.
5. The yellow house's resident is either the farmer or the pilot.
6. The Norwegian lives immediately to the right of the green house's occupant.
7. The blue house and the Swede are two houses apart.
8. The occupant of the blue house is the Spaniard.
9. The Dane is the baker.
10. Exactly one house lies between the farmer and the red house's occupant.
11. The juice drinker and the milk drinker live two houses apart.
12. The red house is immediately to the left of the juice drinker's house.
13. The teacher lives in a lower-numbered house than the Spaniard.
14. The Norwegian lives somewhere to the left of the water drinker.
15. The blue house's occupant and the coffee drinker are not neighbours.

## Puzzle paraphrase:zebra-00158

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, chess, cooking, hiking
- color: white, green, red, purple, blue
- nationality: Spaniard, Brit, Dane, German, Swede
- pet: dog, fish, rabbit, horse, bird

Clues:
1. The hiker keeps the fish.
2. The green house's occupant lives next door to the Swede.
3. The German lives immediately to the left of the white house.
4. The purple house's occupant and the rabbit owner are neighbours.
5. The painter lives in the red house.
6. The purple house's occupant doesn't play tennis.
7. The cooking enthusiast and the Dane live next to each other.
8. The rabbit keeper's hobby is cooking.
9. The bird owner lives next door to the Swede.
10. The Dane keeps the horse.
11. The blue house's occupant is the Brit.
12. The Brit and the red house's occupant live two houses apart.
13. The red house's occupant is the Swede.
