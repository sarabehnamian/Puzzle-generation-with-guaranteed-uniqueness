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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00018

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, doctor, teacher, lawyer, farmer
- nationality: Dane, Brit, Norwegian, German, Swede
- drink: juice, water, tea, coffee, cocoa
- hobby: golf, tennis, painting, chess, cooking

Clues:
1. The person who drinks water lives in one of the two end houses.
2. The golf enthusiast and the juice drinker are not neighbours.
3. The Brit and the Dane are not neighbours.
4. The coffee drinker and the cooking enthusiast live two houses apart.
5. The person who enjoys cooking works as the doctor.
6. The Norwegian lives somewhere to the right of the person who drinks cocoa.
7. The teacher is the Norwegian.
8. The person who drinks juice lives next to the Norwegian.
9. The teacher lives at one end of the row.
10. The person who enjoys painting lives directly to the left of the Swede.
11. The person who drinks tea works as the lawyer.
12. The Brit and the painting enthusiast live two houses apart.
13. The person who enjoys tennis lives in the house just left of the one where the Dane lives.
14. The farmer does not live in house 3.
15. There is exactly one house between the person who drinks juice and the pilot.

## Puzzle hard:zebra_hard-00072

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, fish, bird, dog, cat
- nationality: Swede, German, Norwegian, Dane, Spaniard
- job: teacher, farmer, pilot, doctor, lawyer
- hobby: cooking, golf, tennis, hiking, painting

Clues:
1. The doctor and the hiking enthusiast are one and the same person.
2. The Dane and the pilot are one and the same person.
3. Neither the hiking enthusiast nor the person who enjoys painting keeps the dog.
4. One of the neighbours of the cat owner works as the doctor.
5. The left-hand neighbour of the Spaniard enjoys cooking.
6. One of the neighbours of the Norwegian is the Dane.
7. The fish owner lives further to the right than the hiking enthusiast.
8. The cat owner lives somewhere between the person who enjoys cooking and the lawyer.
9. The Norwegian lives somewhere between the painting enthusiast and the person who enjoys tennis.
10. The person who enjoys cooking lives two doors away from the person who enjoys golf.
11. The person who keeps the rabbit and the person who enjoys tennis are one and the same person.
12. The farmer lives two doors away from the Swede.

## Puzzle plain:zebra-00010

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, doctor, farmer, pilot, teacher
- drink: cocoa, milk, tea, water, coffee
- pet: bird, fish, horse, rabbit, dog
- nationality: German, Brit, Swede, Dane, Norwegian

Clues:
1. The Dane and the German live two houses apart.
2. There is exactly one house between the Norwegian and the teacher.
3. The owner of the fish lives next to the German.
4. The farmer lives next to the Norwegian.
5. The owner of the rabbit either works as the farmer or works as the pilot.
6. The owner of the horse lives directly to the left of the person who keeps the fish.
7. The bird owner works as the doctor.
8. The teacher lives in the house just left of the one where the coffee drinker lives.
9. The German lives next to the person who drinks tea.
10. The tea drinker either is the Brit or is the Norwegian.
11. The person who keeps the fish drinks cocoa.
12. The Brit lives next to the person who drinks milk.
13. The Swede is not the doctor.
14. The pilot lives directly to the left of the owner of the bird.
15. The milk drinker lives in house 2.

## Puzzle paraphrase:zebra-00170

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, white, yellow, red
- nationality: Norwegian, German, Dane, Swede, Brit
- drink: tea, milk, water, cocoa, coffee
- hobby: hiking, chess, painting, tennis, golf

Clues:
1. The hiking fan is either the German or the Swede.
2. Next door to the tea drinker lives the tennis enthusiast.
3. Between the Norwegian and the resident of the white house there are exactly two houses' worth of distance: they are two houses apart.
4. The person who enjoys painting lives immediately to the right of the person who enjoys hiking.
5. The tennis enthusiast and the water drinker have exactly one house between them.
6. One house separates the person who enjoys hiking from the person who enjoys tennis.
7. Somewhere to the right of the white house's occupant lives the Swede.
8. Whoever lives in the red house enjoys either golf or hiking.
9. The Dane's hobby is golf.
10. The Brit is the German's neighbour.
11. The milk drinker is not a neighbour of the person who drinks tea.
12. The coffee drinker's house is right beside the Dane's.
13. The Swede's neighbour is the person in the yellow house.
14. The person who enjoys chess lives immediately to the right of the green house's occupant.
15. The tennis enthusiast lives further along to the right than the Brit.
16. Further to the left than the cocoa drinker lives the coffee drinker.

## Puzzle paraphrase:zebra-00105

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, rabbit, bird, cat
- job: lawyer, farmer, teacher, pilot, doctor
- drink: juice, tea, milk, water, coffee
- color: green, blue, white, red, purple

Clues:
1. The green house belongs to the lawyer.
2. House 4 is where the coffee drinker lives.
3. Somewhere to the right of the blue house's occupant lives the occupant of the red house.
4. The cat owner lives immediately to the right of the dog owner.
5. The bird owner and the doctor live in neighbouring houses.
6. The tea drinker lives immediately to the right of the rabbit owner.
7. The farmer lives in the red house.
8. The juice drinker lives immediately to the left of the purple house's occupant.
9. The coffee drinker and the doctor have exactly one house between them.
10. The coffee drinker and the pilot live next door to each other.
11. The horse is kept by the occupant of the blue house.
12. The water drinker lives immediately to the left of the lawyer.

## Puzzle paraphrase:zebra-00199

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, pilot, baker, farmer, doctor
- drink: milk, tea, coffee, juice, cocoa
- hobby: chess, painting, tennis, cooking, hiking
- nationality: Brit, Dane, German, Norwegian, Spaniard

Clues:
1. The milk drinker is not the doctor.
2. The baker lives directly to the right of the pilot.
3. The chess enthusiast lives immediately to the left of the Brit.
4. The pilot's house is immediately to the right of the farmer's.
5. The painting enthusiast lives right after the Brit, immediately to the right.
6. The Dane is the tea drinker.
7. The tea drinker lives next door to the tennis enthusiast.
8. The chess enthusiast drinks coffee.
9. Exactly one house lies between the Brit and the farmer.
10. The Norwegian lives immediately to the right of the cooking enthusiast.
11. The juice drinker lives next door to the Norwegian.
12. The Spaniard is the lawyer.
13. The doctor's house is immediately to the left of the farmer's.

## Puzzle hard:zebra_hard-00068

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, fish, cat, horse, dog
- color: red, blue, yellow, purple, white
- nationality: Dane, Norwegian, Brit, Swede, Spaniard
- drink: coffee, cocoa, juice, tea, water

Clues:
1. One of the neighbours of the Norwegian is the Dane.
2. Exactly 2 houses lie to the left of the home of the owner of the dog.
3. The juice drinker and the occupant of the yellow house are one and the same person.
4. One of the neighbours of the person who keeps the horse drinks coffee.
5. Neither the person who drinks cocoa nor the coffee drinker keeps the bird.
6. The occupant of the blue house has only one neighbour.
7. Exactly 3 houses lie to the left of the home of the Brit.
8. The Norwegian has only one neighbour.
9. The fish owner lives somewhere between the owner of the horse and the Swede.
10. Exactly 0 houses lie to the left of the home of the occupant of the purple house.
11. The left-hand neighbour of the fish owner drinks cocoa.
12. The left-hand neighbour of the owner of the dog lives in the yellow house.
13. The right-hand neighbour of the occupant of the red house is the Swede.
14. Exactly 4 houses lie to the left of the home of the tea drinker.

## Puzzle hard:zebra_hard-00015

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, hiking, chess, tennis
- nationality: Spaniard, Norwegian, Dane, Swede, Brit
- color: red, yellow, green, white, purple
- drink: juice, tea, coffee, milk, cocoa

Clues:
1. One of the neighbours of the Swede enjoys painting.
2. If the person who enjoys chess does not drink coffee, then that person drinks tea.
3. The person in the white house lives somewhere between the occupant of the purple house and the Spaniard.
4. The left-hand neighbour of the hiking enthusiast lives in the purple house.
5. The Dane lives somewhere between the person who drinks juice and whoever lives in the white house.
6. One of the neighbours of the occupant of the green house drinks milk.
7. None of the neighbours of the occupant of the yellow house drinks milk.
8. None of the neighbours of the juice drinker drinks tea.
9. The Swede is not the same person as the occupant of the white house.
10. The Brit and the tennis enthusiast are one and the same person.
11. The right-hand neighbour of whoever lives in the yellow house enjoys tennis.
12. One of the neighbours of the cocoa drinker is the Swede.
13. The person in the yellow house lives somewhere between the milk drinker and whoever lives in the purple house.

## Puzzle hard:zebra_hard-00003

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, fish, bird, cat
- color: green, white, red, purple, blue
- job: pilot, baker, farmer, teacher, lawyer
- hobby: painting, cooking, hiking, tennis, chess

Clues:
1. Exactly 0 houses lie to the left of the home of the hiking enthusiast.
2. The pilot and the person in the white house are one and the same person.
3. One of the neighbours of the hiking enthusiast keeps the bird.
4. If the occupant of the green house is not the farmer, then that person works as the pilot.
5. The person who enjoys chess lives further to the right than whoever lives in the green house.
6. The person who keeps the cat lives somewhere between the baker and the fish owner.
7. None of the neighbours of the occupant of the white house lives in the red house.
8. The person who keeps the fish and the teacher are one and the same person.
9. The person who enjoys painting and the person in the white house are one and the same person.
10. One of the neighbours of the teacher keeps the dog.
11. The bird owner and the person in the green house are one and the same person.
12. If the occupant of the blue house is not the baker, then that person works as the farmer.
13. One of the neighbours of the cooking enthusiast keeps the dog.
14. The cooking enthusiast does not live in the second house from the right.

## Puzzle paraphrase:zebra-00151

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, juice, milk, cocoa
- color: red, green, yellow, blue, purple
- nationality: Swede, Spaniard, Brit, Dane, Norwegian
- job: teacher, lawyer, farmer, pilot, baker

Clues:
1. The lawyer's house is red.
2. Somewhere further to the right of the Swede lives the baker.
3. The Brit's house is at one of the two ends of the row.
4. The Norwegian lives right next door to the right of the milk drinker.
5. The yellow house's occupant is either the farmer or the pilot.
6. The Norwegian's house is immediately right of the green house.
7. The blue house's occupant and the Swede live two houses apart.
8. The Spaniard is the one living in the blue house.
9. The Dane is the baker.
10. A single house lies between the farmer and the occupant of the red house.
11. The juice drinker and the milk drinker live two houses apart.
12. The red house stands directly to the left of the juice drinker's house.
13. The teacher's house number is lower than the Spaniard's.
14. The Norwegian lives somewhere to the left of the water drinker.
15. The blue house's occupant and the coffee drinker do not live next door to each other.
