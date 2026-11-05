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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_023.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00127

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, milk, juice, coffee, tea
- color: blue, red, green, yellow, white
- nationality: Spaniard, Brit, Swede, Dane, German
- pet: fish, bird, horse, cat, rabbit

Clues:
1. The cocoa drinker and the Swede live next door to each other.
2. The cat owner does not live next to the Swede.
3. The Spaniard keeps the rabbit.
4. The Dane's house is immediately to the left of the fish owner's house.
5. The milk drinker lives directly to the left of the fish owner.
6. The German and the green house are two houses apart.
7. The rabbit owner lives somewhere to the right of the fish owner.
8. The coffee drinker lives in either the blue house or the white house.
9. The German lives in house 4.
10. The juice drinker lives in the blue house.
11. The milk drinker lives in the yellow house.
12. The German is not a neighbour of the horse owner.
13. The blue house is directly to the left of the Spaniard's house.
14. The cat owner lives next door to the Spaniard.

## Puzzle plain:zebra-00067

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, white, green, blue, purple
- hobby: golf, cooking, chess, painting, hiking
- nationality: Brit, Norwegian, Spaniard, German, Dane
- job: doctor, farmer, pilot, teacher, baker

Clues:
1. The Dane lives in a lower-numbered house than the baker.
2. The Norwegian lives next to the occupant of the purple house.
3. The cooking enthusiast and the Norwegian live in adjacent houses.
4. The person in the green house and the pilot live two houses apart.
5. The person in the blue house is the Spaniard.
6. Whoever lives in the red house lives in a lower-numbered house than the person in the white house.
7. Whoever lives in the red house enjoys chess.
8. The Norwegian lives next to the teacher.
9. The Brit enjoys golf.
10. The hiking enthusiast lives in the middle house.
11. The person in the green house and the occupant of the purple house live two houses apart.
12. The farmer and the person who enjoys hiking are neighbours.
13. The person in the red house works as the doctor.
14. The German lives next to the hiking enthusiast.

## Puzzle plain:zebra-00029

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, horse, rabbit, bird, cat
- drink: tea, water, coffee, milk, cocoa
- color: purple, white, green, blue, red
- job: lawyer, farmer, pilot, doctor, teacher

Clues:
1. The cocoa drinker lives in house 1.
2. Whoever lives in the purple house keeps the cat.
3. The farmer lives in the blue house.
4. The lawyer lives in the house just left of the one where the horse owner lives.
5. The person in the blue house and the owner of the fish live two houses apart.
6. The pilot either lives in the blue house or lives in the red house.
7. The person who keeps the horse lives immediately to the right of the person in the white house.
8. The person in the purple house lives directly to the left of the person who drinks milk.
9. The person who keeps the horse and the person who drinks tea are neighbours.
10. The tea drinker lives somewhere to the left of the doctor.
11. The owner of the rabbit either lives in the purple house or lives in the white house.
12. The lawyer lives in house 3.
13. The person in the blue house and the person who drinks water are neighbours.

## Puzzle paraphrase:zebra-00114

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, fish, cat, rabbit, horse
- nationality: Brit, Dane, Spaniard, Swede, Norwegian
- drink: coffee, tea, water, cocoa, juice
- job: lawyer, baker, farmer, teacher, doctor

Clues:
1. The cocoa drinker lives next door to the Spaniard.
2. The water drinker lives in a lower-numbered house than the tea drinker.
3. The fish keeper drinks cocoa.
4. The cocoa drinker and the juice drinker are not neighbours.
5. The Brit does not live next to the cat owner.
6. Exactly one house separates the Dane from the Spaniard.
7. The bird owner lives next door to the farmer.
8. The Dane lives immediately to the right of the Norwegian.
9. The horse owner lives immediately to the left of the doctor.
10. The Swede drinks water.
11. The lawyer keeps either the bird or the horse.
12. The cat is kept in the fifth house.
13. The cocoa drinker is the teacher.
14. The Brit lives right beside the farmer.
15. The tea drinker is the farmer.

## Puzzle hard:zebra_hard-00014

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, farmer, teacher, pilot
- pet: cat, bird, horse, fish, dog
- drink: water, milk, juice, coffee, cocoa
- color: blue, green, purple, red, white

Clues:
1. If the occupant of the blue house is not the baker, then that person works as the teacher.
2. One of the neighbours of the person in the purple house lives in the green house.
3. The left-hand neighbour of whoever lives in the white house lives in the green house.
4. The cat owner does not live in the fourth house from the right.
5. If the person who keeps the cat does not drink cocoa, then that person drinks milk.
6. Exactly one house separates the person who drinks coffee from the teacher.
7. Exactly one house separates the farmer from the pilot.
8. One of the neighbours of the occupant of the purple house drinks cocoa.
9. Exactly one house separates the person who keeps the dog from the person who drinks milk.
10. The left-hand neighbour of the person who keeps the cat works as the teacher.
11. The farmer and the person in the purple house are one and the same person.
12. One of the neighbours of the bird owner lives in the white house.
13. The coffee drinker and the person who keeps the horse are one and the same person.
14. The pilot and the water drinker are one and the same person.

## Puzzle paraphrase:zebra-00103

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, coffee, juice, water
- nationality: Spaniard, German, Brit, Swede, Norwegian
- hobby: hiking, golf, painting, cooking, chess
- color: red, purple, blue, green, white

Clues:
1. The coffee drinker's hobby is cooking.
2. The Brit lives in the purple house.
3. The cocoa drinker lives right next door to the hiker, on the hiker's right.
4. One house separates the blue house's occupant from the Norwegian.
5. The juice drinker lives in house 2.
6. The cocoa drinker lives somewhere to the right of the Swede.
7. One house lies between the German and the purple house's occupant.
8. The painting enthusiast lives immediately to the left of the Brit.
9. The white house's occupant enjoys hiking.
10. The Norwegian doesn't drink tea.
11. The blue house is house 3.
12. The red house's occupant enjoys golf.
13. The coffee drinker lives in the leftmost house.

## Puzzle paraphrase:zebra-00193

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Brit, Spaniard, Dane
- job: baker, doctor, teacher, farmer, pilot
- pet: fish, dog, cat, rabbit, horse
- color: green, blue, yellow, white, red

Clues:
1. The white house and the yellow house are next to each other.
2. The Dane is the doctor.
3. The cat keeper lives immediately to the right of the Swede.
4. The green house's occupant keeps either the cat or the dog.
5. The German and the red house's occupant are not neighbours.
6. The Brit lives next door to the farmer.
7. The Swede is the pilot.
8. The Dane and the occupant of the yellow house live two houses apart.
9. The German lives next door to the pilot.
10. The blue house is directly to the left of the yellow house.
11. The dog keeper lives somewhere to the right of the German.
12. The rabbit owner is either the doctor or the pilot.
13. The fish keeper is the teacher.
14. Somewhere to the right of the Brit lives the teacher.

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

## Puzzle paraphrase:zebra-00123

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, coffee, juice, milk, tea
- job: pilot, teacher, baker, farmer, lawyer
- nationality: Norwegian, Brit, Swede, German, Spaniard
- pet: cat, dog, bird, horse, rabbit

Clues:
1. The dog owner is a teacher.
2. The Norwegian occupies house 5.
3. The Swede's drink is either juice or milk.
4. The Swede is a pilot.
5. The tea drinker keeps the rabbit.
6. The dog owner lives next door to the Norwegian.
7. The Spaniard drinks milk.
8. One house lies between the milk drinker and the water drinker.
9. The farmer lives immediately to the right of the dog owner.
10. The baker lives next door to the cat owner.
11. The farmer and the horse owner are two houses apart.
12. The German lives directly to the right of the rabbit keeper.

## Puzzle hard:zebra_hard-00075

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, teacher, farmer, baker
- hobby: chess, golf, painting, cooking, tennis
- pet: cat, bird, fish, rabbit, horse
- nationality: Dane, Spaniard, German, Brit, Swede

Clues:
1. If the tennis enthusiast does not keep the cat, then that person keeps the horse.
2. The left-hand neighbour of the lawyer is the Dane.
3. One of the neighbours of the pilot enjoys cooking.
4. Exactly one house separates the Brit from the Swede.
5. The left-hand neighbour of the owner of the bird enjoys painting.
6. One of the neighbours of the Spaniard keeps the rabbit.
7. The baker lives two doors away from the owner of the cat.
8. The left-hand neighbour of the person who enjoys golf is the German.
9. The Spaniard and the teacher are one and the same person.
10. The Swede lives two doors away from the person who enjoys tennis.
11. The right-hand neighbour of the painting enthusiast is the Dane.
12. The owner of the fish lives further to the right than the German.
13. The person who enjoys painting has only one neighbour.
