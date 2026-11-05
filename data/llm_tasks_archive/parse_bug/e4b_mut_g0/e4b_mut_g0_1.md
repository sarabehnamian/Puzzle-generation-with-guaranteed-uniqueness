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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_mut_g0\e4b_mut_g0_1.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4b-g0-02

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, doctor, teacher, farmer
- hobby: tennis, cooking, hiking, painting, golf, chess
- drink: cocoa, coffee, juice, water, tea, milk
- pet: fish, rabbit, bird, cat, dog, horse
- color: green, purple, blue, yellow, red, white
- nationality: Spaniard, German, Swede, Brit, Norwegian, Dane

Formal clues (with their English text):
1. gap2(dane, norwegian)   "The Dane and the Norwegian live two houses apart."
2. not_same(golf, yellow)   "The person who enjoys golf does not live in the yellow house."
3. gap2(baker, tea)   "There is exactly one house between the baker and the tea drinker."
4. at(water, 1)   "The water drinker lives in the first house."
5. before(german, hiking)   "The German lives somewhere to the left of the hiking enthusiast."
6. gap2(brit, purple)   "The Brit and the person in the purple house live two houses apart."
7. same(blue, spaniard)   "The person in the blue house is the Spaniard."
8. left_of(tennis, doctor)   "The person who enjoys tennis lives directly to the left of the doctor."
9. or(cooking, baker, lawyer)   "The cooking enthusiast either works as the baker or works as the lawyer."
10. before(milk, hiking)   "The person who drinks milk lives somewhere to the left of the hiking enthusiast."
11. or(farmer, purple, red)   "The farmer either lives in the purple house or lives in the red house."
12. same(chess, horse)   "The person who keeps the horse enjoys chess."
13. or(cocoa, chess, painting)   "The cocoa drinker either enjoys chess or enjoys painting."
14. same(lawyer, swede)   "The lawyer is the Swede."
15. at(pilot, 4)   "The pilot lives in house 4."
16. left_of(white, golf)   "The occupant of the white house lives directly to the left of the golf enthusiast."
17. at(red, 1)   "The occupant of the red house lives in house 1."
18. same(chess, green)   "The occupant of the green house enjoys chess."
19. same(juice, white)   "The juice drinker lives in the white house."
20. or(fish, spaniard, swede)   "The owner of the fish either is the Spaniard or is the Swede."
21. at(spaniard, 2)   "The Spaniard lives in house 2."
22. same(dog, yellow)   "The owner of the dog lives in the yellow house."
23. same(dane, pilot)   "The pilot is the Dane."
24. not_next_to(cat, coffee)   "The owner of the cat and the person who drinks coffee are not neighbours."
25. same(bird, milk)   "The person who keeps the bird drinks milk."

Solution: house 1: cat, farmer, german, red, tennis, water; house 2: bird, blue, doctor, milk, painting, spaniard; house 3: baker, brit, coffee, cooking, dog, yellow; house 4: dane, hiking, juice, pilot, rabbit, white; house 5: fish, golf, lawyer, purple, swede, tea; house 6: chess, cocoa, green, horse, norwegian, teacher
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-05

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Formal clues (with their English text):
1. gap2(chess, lawyer)   "There is exactly one house between the chess enthusiast and the lawyer."
2. or(baker, horse, rabbit)   "The baker either keeps the horse or keeps the rabbit."
3. at(german, 6)   "The German lives in house 6."
4. same(blue, juice)   "The person who drinks juice lives in the blue house."
5. gap2(farmer, red)   "The farmer and the person in the red house live two houses apart."
6. left_of(tea, green)   "The tea drinker lives directly to the left of the person in the green house."
7. left_of(yellow, horse)   "The horse owner lives immediately to the right of whoever lives in the yellow house."
8. same(golf, lawyer)   "The lawyer enjoys golf."
9. next_to(norwegian, yellow)   "The Norwegian and the occupant of the yellow house are neighbours."
10. same(brit, white)   "The occupant of the white house is the Brit."
11. left_of(water, swede)   "The water drinker lives in the house just left of the one where the Swede lives."
12. or(rabbit, dane, german)   "The owner of the rabbit either is the Dane or is the German."
13. same(coffee, painting)   "The person who enjoys painting drinks coffee."
14. not_same(coffee, purple)   "The person in the purple house does not drink coffee."
15. same(bird, farmer)   "The farmer keeps the bird."
16. gap2(blue, doctor)   "The person in the blue house and the doctor live two houses apart."
17. left_of(rabbit, horse)   "The rabbit owner lives directly to the left of the owner of the horse."
18. next_to(golf, tea)   "The golf enthusiast and the person who drinks tea are neighbours."
19. next_to(cat, purple)   "The cat owner lives next to the person in the purple house."
20. or(cocoa, doctor, pilot)   "The person who drinks cocoa either works as the doctor or works as the pilot."
21. same(cooking, fish)   "The fish owner enjoys cooking."
22. next_to(green, tennis)   "The person in the green house lives next to the tennis enthusiast."
23. left_of(norwegian, german)   "The Norwegian lives in the house just left of the one where the German lives."
24. or(dog, lawyer, teacher)   "The owner of the dog either works as the lawyer or works as the teacher."
25. same(tennis, white)   "The person in the white house enjoys tennis."

Solution: house 1: brit, dog, tea, teacher, tennis, white; house 2: cat, golf, green, lawyer, spaniard, water; house 3: bird, farmer, hiking, milk, purple, swede; house 4: chess, cocoa, dane, doctor, rabbit, yellow; house 5: baker, coffee, horse, norwegian, painting, red; house 6: blue, cooking, fish, german, juice, pilot
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-06

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Formal clues (with their English text):
1. left_of(brit, blue)   "The person in the blue house lives immediately to the right of the Brit."
2. before(teacher, painting)   "The teacher lives in a lower-numbered house than the person who enjoys painting."
3. gap2(cooking, yellow)   "The cooking enthusiast and whoever lives in the yellow house live two houses apart."
4. same(juice, white)   "The person who drinks juice lives in the white house."
5. same(teacher, white)   "The teacher lives in the white house."
6. left_of(dane, farmer)   "The Dane lives directly to the left of the farmer."
7. same(horse, purple)   "The owner of the horse lives in the purple house."
8. same(spaniard, tennis)   "The tennis enthusiast is the Spaniard."
9. not_next_to(bird, fish)   "The person who keeps the bird and the owner of the fish are not neighbours."
10. or(golf, farmer, pilot)   "The person who enjoys golf either works as the farmer or works as the pilot."
11. next_to(coffee, norwegian)   "The person who drinks coffee and the Norwegian live in adjacent houses."
12. at(chess, 2)   "The chess enthusiast lives in house 2."
13. gap2(cocoa, spaniard)   "The cocoa drinker and the Spaniard live two houses apart."
14. left_of(tennis, cooking)   "The tennis enthusiast lives in the house just left of the one where the cooking enthusiast lives."
15. left_of(rabbit, tennis)   "The rabbit owner lives in the house just left of the one where the tennis enthusiast lives."
16. at(bird, 2)   "The bird owner lives in house 2."
17. not_same(dane, milk)   "The Dane and the person who drinks milk are different people."
18. same(golf, swede)   "The Swede enjoys golf."
19. same(doctor, red)   "The occupant of the red house works as the doctor."
20. same(brit, white)   "The Brit lives in the white house."
21. same(dog, german)   "The German keeps the dog."
22. left_of(water, white)   "The occupant of the white house lives immediately to the right of the person who drinks water."
23. same(baker, green)   "The baker lives in the green house."
24. at(golf, 3)   "The golf enthusiast lives in house 3."
25. next_to(doctor, tennis)   "The doctor and the person who enjoys tennis live in adjacent houses."

Solution: house 1: baker, dog, german, green, hiking, water; house 2: bird, brit, chess, juice, teacher, white; house 3: blue, cat, cocoa, golf, pilot, swede; house 4: dane, lawyer, painting, rabbit, tea, yellow; house 5: coffee, farmer, horse, purple, spaniard, tennis; house 6: cooking, doctor, fish, milk, norwegian, red
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00
