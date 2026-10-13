# Task: make fair logic puzzles harder for language-model solvers

Each puzzle below is a 6-house logic-grid puzzle with a known unique solution. A language-model
solver attempted it; its mistakes are listed. Propose 2 variants of each puzzle that you expect to
be HARDER for a language-model solver, while staying solvable by pure step-by-step deduction.

You edit puzzles with operations on the formal clue list:
- {"op": "remove", "clue": <clue number>}
- {"op": "add", "clue": {"type": <type>, "args": [...]}}
- {"op": "replace", "clue": <clue number>, "with": {"type": <type>, "args": [...]}}
Use 1 to 4 operations per variant. Clue types (a, b, c are value names; k is a house number):
  same(a,b)        a and b belong to the same person
  not_same(a,b)    a and b belong to different people
  at(a,k)          a is in house k            not_at(a,k)     a is not in house k
  left_of(a,b)     a is directly left of b    next_to(a,b)    a and b are neighbours
  not_next_to(a,b) a and b are not neighbours (they may share a house)
  before(a,b)      a is somewhere left of b   gap2(a,b)       exactly one house between a and b
  end(a)           a is in house 1 or house 6
  or(a,b,c)        a is with b or with c (b and c from the same category)
Every clue you add must be TRUE of the stated solution. A program will apply your edits, add a clue
if the result is no longer unique, and reject variants that need guessing, so focus on what makes the
deduction harder to follow (for example: fewer direct position clues, longer chains of inference,
negative and relative clues, information spread across many clues).

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_mut_g1/e4b_mut_g1_0.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4b-g0-00

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, bird, cat, horse, fish
- drink: milk, juice, water, coffee, cocoa, tea
- color: blue, purple, yellow, red, white, green
- nationality: Dane, Spaniard, German, Swede, Norwegian, Brit
- job: doctor, baker, teacher, pilot, farmer, lawyer
- hobby: chess, painting, cooking, golf, tennis, hiking

Formal clues (with their English text):
1. same(coffee, golf)   "The person who enjoys golf drinks coffee."
2. gap2(swede, white)   "The Swede and the occupant of the white house live two houses apart."
3. next_to(baker, cocoa)   "The baker and the cocoa drinker live in adjacent houses."
4. before(dog, tea)   "The person who keeps the dog lives somewhere to the left of the tea drinker."
5. same(green, hiking)   "The person who enjoys hiking lives in the green house."
6. next_to(doctor, red)   "The doctor and the occupant of the red house live in adjacent houses."
7. same(brit, tea)   "The Brit drinks tea."
8. left_of(rabbit, painting)   "The painting enthusiast lives immediately to the right of the person who keeps the rabbit."
9. at(water, 5)   "The person who drinks water lives in the fifth house."
10. left_of(farmer, rabbit)   "The farmer lives directly to the left of the owner of the rabbit."
11. gap2(cat, lawyer)   "There is exactly one house between the person who keeps the cat and the lawyer."
12. left_of(juice, cat)   "The person who drinks juice lives directly to the left of the owner of the cat."
13. same(chess, yellow)   "The person who enjoys chess lives in the yellow house."
14. at(blue, 3)   "The occupant of the blue house lives in the third house."
15. at(juice, 2)   "The juice drinker lives in house 2."
16. same(bird, dane)   "The owner of the bird is the Dane."
17. next_to(purple, spaniard)   "The person in the purple house lives next to the Spaniard."
18. same(horse, pilot)   "The pilot keeps the horse."
19. same(teacher, tennis)   "The teacher enjoys tennis."
20. at(coffee, 6)   "The person who drinks coffee lives in the last house."
21. next_to(green, red)   "Whoever lives in the green house and whoever lives in the red house are neighbours."
22. next_to(cocoa, norwegian)   "The cocoa drinker and the Norwegian live in adjacent houses."
23. gap2(tea, tennis)   "The tea drinker and the tennis enthusiast live two houses apart."

Solution: house 1: bird, dane, doctor, green, hiking, milk; house 2: dog, juice, norwegian, red, teacher, tennis; house 3: blue, cat, cocoa, cooking, farmer, swede; house 4: baker, brit, chess, rabbit, tea, yellow; house 5: fish, lawyer, painting, spaniard, water, white; house 6: coffee, german, golf, horse, pilot, purple
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-02

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, baker, pilot, doctor, teacher
- hobby: tennis, hiking, golf, chess, painting, cooking
- pet: rabbit, bird, fish, cat, dog, horse
- color: green, blue, white, yellow, red, purple
- drink: cocoa, juice, milk, tea, coffee, water
- nationality: Brit, Norwegian, German, Swede, Spaniard, Dane

Formal clues (with their English text):
1. same(juice, norwegian)   "The Norwegian drinks juice."
2. same(hiking, norwegian)   "The person who enjoys hiking is the Norwegian."
3. same(cocoa, golf)   "The person who drinks cocoa enjoys golf."
4. at(water, 1)   "The water drinker lives in the first house."
5. same(fish, lawyer)   "The person who keeps the fish works as the lawyer."
6. next_to(bird, red)   "The person who keeps the bird and the person in the red house live in adjacent houses."
7. at(blue, 1)   "The person in the blue house lives in house 1."
8. left_of(tennis, teacher)   "The teacher lives immediately to the right of the person who enjoys tennis."
9. before(yellow, swede)   "The person in the yellow house lives in a lower-numbered house than the Swede."
10. left_of(horse, baker)   "The owner of the horse lives directly to the left of the baker."
11. or(purple, juice, tea)   "The person in the purple house either drinks juice or drinks tea."
12. same(painting, pilot)   "The painting enthusiast works as the pilot."
13. next_to(norwegian, rabbit)   "The Norwegian and the owner of the rabbit live in adjacent houses."
14. same(coffee, painting)   "The coffee drinker enjoys painting."
15. next_to(dane, rabbit)   "The Dane lives next to the person who keeps the rabbit."
16. same(brit, rabbit)   "The person who keeps the rabbit is the Brit."
17. at(bird, 6)   "The bird owner lives in the sixth house."
18. next_to(cat, german)   "The cat owner and the German are neighbours."
19. left_of(cooking, green)   "Whoever lives in the green house lives immediately to the right of the person who enjoys cooking."
20. same(golf, green)   "The occupant of the green house enjoys golf."
21. left_of(rabbit, green)   "The person who keeps the rabbit lives directly to the left of whoever lives in the green house."
22. left_of(farmer, baker)   "The farmer lives directly to the left of the baker."
23. left_of(dog, milk)   "The person who drinks milk lives immediately to the right of the dog owner."

Solution: house 1: blue, fish, lawyer, spaniard, tennis, water; house 2: dog, hiking, juice, norwegian, purple, teacher; house 3: brit, cooking, doctor, milk, rabbit, yellow; house 4: cocoa, dane, farmer, golf, green, horse; house 5: baker, cat, chess, red, swede, tea; house 6: bird, coffee, german, painting, pilot, white
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-05

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, bird, cat, fish, horse, rabbit
- color: green, white, red, yellow, blue, purple
- drink: cocoa, coffee, juice, milk, tea, water
- job: teacher, farmer, pilot, lawyer, baker, doctor
- hobby: painting, cooking, tennis, chess, golf, hiking
- nationality: German, Brit, Swede, Dane, Norwegian, Spaniard

Formal clues (with their English text):
1. same(bird, brit)   "The Brit keeps the bird."
2. same(baker, chess)   "The baker enjoys chess."
3. same(bird, lawyer)   "The owner of the bird works as the lawyer."
4. gap2(hiking, juice)   "The person who enjoys hiking and the person who drinks juice live two houses apart."
5. at(white, 1)   "Whoever lives in the white house lives in the leftmost house."
6. next_to(teacher, tennis)   "The teacher and the tennis enthusiast live in adjacent houses."
7. next_to(dane, farmer)   "The Dane lives next to the farmer."
8. same(farmer, tennis)   "The farmer enjoys tennis."
9. or(chess, blue, yellow)   "The chess enthusiast either lives in the blue house or lives in the yellow house."
10. at(purple, 2)   "Whoever lives in the purple house lives in the second house."
11. before(norwegian, juice)   "The Norwegian lives somewhere to the left of the juice drinker."
12. or(horse, farmer, pilot)   "The owner of the horse either works as the farmer or works as the pilot."
13. gap2(cat, purple)   "There is exactly one house between the person who keeps the cat and whoever lives in the purple house."
14. gap2(bird, yellow)   "There is exactly one house between the bird owner and whoever lives in the yellow house."
15. same(fish, milk)   "The person who drinks milk keeps the fish."
16. same(coffee, pilot)   "The coffee drinker works as the pilot."
17. left_of(norwegian, blue)   "The Norwegian lives in the house just left of the one where whoever lives in the blue house lives."
18. gap2(cocoa, golf)   "The cocoa drinker and the golf enthusiast live two houses apart."
19. same(rabbit, swede)   "The Swede keeps the rabbit."
20. left_of(german, cooking)   "The German lives in the house just left of the one where the person who enjoys cooking lives."
21. same(dane, tea)   "The Dane drinks tea."
22. left_of(red, rabbit)   "The rabbit owner lives immediately to the right of whoever lives in the red house."
23. same(farmer, juice)   "The farmer drinks juice."

Solution: house 1: bird, brit, lawyer, painting, water, white; house 2: coffee, golf, horse, pilot, purple, spaniard; house 3: baker, chess, fish, milk, norwegian, yellow; house 4: blue, cat, cocoa, doctor, german, hiking; house 5: cooking, dane, dog, red, tea, teacher; house 6: farmer, green, juice, rabbit, swede, tennis
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-01

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, rabbit, dog, bird, cat
- hobby: hiking, tennis, cooking, painting, chess, golf
- job: doctor, farmer, teacher, lawyer, pilot, baker
- drink: coffee, juice, water, cocoa, tea, milk
- color: red, yellow, white, purple, blue, green
- nationality: Swede, German, Norwegian, Brit, Dane, Spaniard

Formal clues (with their English text):
1. left_of(bird, baker)   "The bird owner lives in the house just left of the one where the baker lives."
2. left_of(milk, norwegian)   "The person who drinks milk lives directly to the left of the Norwegian."
3. or(chess, cat, rabbit)   "The person who enjoys chess either keeps the cat or keeps the rabbit."
4. same(blue, norwegian)   "The person in the blue house is the Norwegian."
5. at(brit, 5)   "The Brit lives in the fifth house."
6. same(golf, rabbit)   "The person who keeps the rabbit enjoys golf."
7. same(pilot, spaniard)   "The Spaniard works as the pilot."
8. left_of(norwegian, tennis)   "The tennis enthusiast lives immediately to the right of the Norwegian."
9. next_to(horse, painting)   "The person who keeps the horse and the painting enthusiast are neighbours."
10. next_to(cocoa, rabbit)   "The cocoa drinker and the person who keeps the rabbit live in adjacent houses."
11. next_to(coffee, white)   "The person who drinks coffee lives next to the occupant of the white house."
12. gap2(purple, white)   "There is exactly one house between the person in the purple house and whoever lives in the white house."
13. same(juice, rabbit)   "The owner of the rabbit drinks juice."
14. at(dane, 6)   "The Dane lives in the sixth house."
15. or(cooking, green, purple)   "The cooking enthusiast either lives in the green house or lives in the purple house."
16. same(tea, teacher)   "The teacher drinks tea."
17. at(doctor, 3)   "The doctor lives in house 3."
18. at(chess, 4)   "The person who enjoys chess lives in house 4."
19. same(fish, tea)   "The person who drinks tea keeps the fish."
20. same(bird, german)   "The bird owner is the German."
21. left_of(yellow, rabbit)   "The owner of the rabbit lives immediately to the right of the occupant of the yellow house."
22. before(yellow, german)   "The German lives somewhere to the right of the person in the yellow house."
23. or(green, doctor, farmer)   "Whoever lives in the green house either works as the doctor or works as the farmer."
24. same(red, tea)   "The person who drinks tea lives in the red house."

Solution: house 1: cocoa, dog, hiking, pilot, spaniard, yellow; house 2: farmer, golf, green, juice, rabbit, swede; house 3: bird, cooking, doctor, german, milk, purple; house 4: baker, blue, cat, chess, coffee, norwegian; house 5: brit, horse, lawyer, tennis, water, white; house 6: dane, fish, painting, red, tea, teacher
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-06

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Swede, Brit, Spaniard, German, Norwegian
- pet: bird, rabbit, dog, horse, fish, cat
- hobby: cooking, tennis, painting, golf, hiking, chess
- job: teacher, baker, pilot, doctor, farmer, lawyer
- drink: juice, coffee, milk, water, tea, cocoa
- color: yellow, white, purple, blue, red, green

Formal clues (with their English text):
1. before(yellow, green)   "The occupant of the green house lives somewhere to the right of whoever lives in the yellow house."
2. at(blue, 4)   "Whoever lives in the blue house lives in house 4."
3. left_of(hiking, cat)   "The person who enjoys hiking lives in the house just left of the one where the owner of the cat lives."
4. left_of(spaniard, purple)   "The Spaniard lives directly to the left of whoever lives in the purple house."
5. at(milk, 3)   "The milk drinker lives in the third house."
6. not_next_to(fish, pilot)   "The person who keeps the fish does not live next to the pilot."
7. left_of(juice, fish)   "The fish owner lives immediately to the right of the person who drinks juice."
8. at(brit, 5)   "The Brit lives in house 5."
9. gap2(cocoa, teacher)   "The person who drinks cocoa and the teacher live two houses apart."
10. or(cocoa, blue, yellow)   "The cocoa drinker either lives in the blue house or lives in the yellow house."
11. same(horse, yellow)   "The owner of the horse lives in the yellow house."
12. next_to(doctor, red)   "The doctor lives next to the person in the red house."
13. same(green, tea)   "The occupant of the green house drinks tea."
14. gap2(painting, pilot)   "The painting enthusiast and the pilot live two houses apart."
15. left_of(norwegian, tennis)   "The Norwegian lives directly to the left of the tennis enthusiast."
16. before(cocoa, coffee)   "The cocoa drinker lives somewhere to the left of the coffee drinker."
17. gap2(teacher, tennis)   "There is exactly one house between the teacher and the person who enjoys tennis."
18. same(baker, cooking)   "The person who enjoys cooking works as the baker."
19. before(bird, swede)   "The owner of the bird lives somewhere to the left of the Swede."
20. at(swede, 3)   "The Swede lives in the third house."
21. same(lawyer, swede)   "The lawyer is the Swede."
22. left_of(farmer, chess)   "The farmer lives in the house just left of the one where the person who enjoys chess lives."
23. at(cat, 6)   "The cat owner lives in house 6."
24. gap2(dane, rabbit)   "There is exactly one house between the Dane and the person who keeps the rabbit."

Solution: house 1: baker, bird, cooking, norwegian, water, white; house 2: cocoa, horse, pilot, spaniard, tennis, yellow; house 3: dog, golf, lawyer, milk, purple, swede; house 4: blue, german, juice, painting, rabbit, teacher; house 5: brit, coffee, farmer, fish, hiking, red; house 6: cat, chess, dane, doctor, green, tea
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00
