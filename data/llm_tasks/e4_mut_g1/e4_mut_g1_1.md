# Task: make fair logic puzzles harder for language-model solvers

Each puzzle below is a 5-house logic-grid puzzle with a known unique solution. A language-model
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
  end(a)           a is in house 1 or house 5
  or(a,b,c)        a is with b or with c (b and c from the same category)
Every clue you add must be TRUE of the stated solution. A program will apply your edits, add a clue
if the result is no longer unique, and reject variants that need guessing, so focus on what makes the
deduction harder to follow (for example: fewer direct position clues, longer chains of inference,
negative and relative clues, information spread across many clues).

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_mut_g1/e4_mut_g1_1.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle evo-g0-02

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Brit, Spaniard, German, Norwegian
- hobby: painting, tennis, golf, cooking, hiking
- job: lawyer, doctor, baker, teacher, farmer
- pet: fish, horse, bird, cat, dog

Formal clues (with their English text):
1. next_to(german, lawyer)   "The German and the lawyer live in adjacent houses."
2. not_next_to(fish, golf)   "The person who keeps the fish and the golf enthusiast are not neighbours."
3. same(cat, golf)   "The golf enthusiast keeps the cat."
4. next_to(doctor, golf)   "The doctor and the golf enthusiast live in adjacent houses."
5. left_of(cooking, norwegian)   "The Norwegian lives immediately to the right of the person who enjoys cooking."
6. same(cooking, german)   "The German enjoys cooking."
7. next_to(norwegian, spaniard)   "The Norwegian lives next to the Spaniard."
8. same(horse, painting)   "The person who keeps the horse enjoys painting."
9. left_of(bird, german)   "The German lives immediately to the right of the bird owner."
10. next_to(lawyer, tennis)   "The lawyer and the tennis enthusiast live in adjacent houses."
11. before(fish, farmer)   "The person who keeps the fish lives somewhere to the left of the farmer."
12. gap2(farmer, horse)   "There is exactly one house between the farmer and the person who keeps the horse."
13. or(hiking, norwegian, swede)   "The person who enjoys hiking either is the Norwegian or is the Swede."
14. left_of(hiking, teacher)   "The hiking enthusiast lives in the house just left of the one where the teacher lives."

Solution: house 1: baker, bird, hiking, swede; house 2: cooking, fish, german, teacher; house 3: horse, lawyer, norwegian, painting; house 4: doctor, dog, spaniard, tennis; house 5: brit, cat, farmer, golf
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle evo-g0-04

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, teacher, baker
- pet: cat, dog, bird, horse, fish
- hobby: chess, golf, cooking, tennis, hiking
- color: white, yellow, purple, red, green

Formal clues (with their English text):
1. left_of(horse, cat)   "The cat owner lives immediately to the right of the owner of the horse."
2. same(chess, red)   "The person who enjoys chess lives in the red house."
3. at(yellow, 5)   "The person in the yellow house lives in the fifth house."
4. at(baker, 4)   "The baker lives in house 4."
5. next_to(bird, lawyer)   "The owner of the bird and the lawyer are neighbours."
6. same(bird, hiking)   "The bird owner enjoys hiking."
7. left_of(pilot, cat)   "The pilot lives directly to the left of the person who keeps the cat."
8. end(cooking)   "The person who enjoys cooking lives at one end of the row."
9. gap2(chess, doctor)   "There is exactly one house between the chess enthusiast and the doctor."
10. or(purple, hiking, tennis)   "Whoever lives in the purple house either enjoys hiking or enjoys tennis."
11. next_to(purple, white)   "Whoever lives in the purple house and the person in the white house are neighbours."
12. before(cooking, cat)   "The person who keeps the cat lives somewhere to the right of the person who enjoys cooking."
13. next_to(horse, tennis)   "The horse owner lives next to the person who enjoys tennis."
14. or(dog, cooking, hiking)   "The person who keeps the dog either enjoys cooking or enjoys hiking."

Solution: house 1: cooking, dog, lawyer, white; house 2: bird, hiking, purple, teacher; house 3: chess, horse, pilot, red; house 4: baker, cat, green, tennis; house 5: doctor, fish, golf, yellow
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle evo-g0-05

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, tennis, cooking, hiking
- nationality: Norwegian, Swede, German, Spaniard, Dane
- color: red, green, blue, yellow, white
- drink: cocoa, water, tea, milk, juice

Formal clues (with their English text):
1. left_of(cocoa, red)   "The person who drinks cocoa lives directly to the left of whoever lives in the red house."
2. next_to(dane, german)   "The Dane lives next to the German."
3. or(tea, red, white)   "The tea drinker either lives in the red house or lives in the white house."
4. left_of(swede, milk)   "The Swede lives in the house just left of the one where the milk drinker lives."
5. same(golf, water)   "The golf enthusiast drinks water."
6. next_to(german, red)   "The German and the occupant of the red house are neighbours."
7. left_of(dane, yellow)   "The Dane lives in the house just left of the one where the person in the yellow house lives."
8. same(painting, swede)   "The Swede enjoys painting."
9. not_next_to(golf, juice)   "The person who enjoys golf does not live next to the juice drinker."
10. same(norwegian, tennis)   "The Norwegian enjoys tennis."
11. left_of(blue, yellow)   "The person in the blue house lives directly to the left of whoever lives in the yellow house."
12. before(white, hiking)   "Whoever lives in the white house lives somewhere to the left of the person who enjoys hiking."
13. left_of(painting, cooking)   "The painting enthusiast lives in the house just left of the one where the person who enjoys cooking lives."
14. next_to(german, painting)   "The German and the painting enthusiast are neighbours."

Solution: house 1: norwegian, tea, tennis, white; house 2: blue, dane, golf, water; house 3: cocoa, german, hiking, yellow; house 4: juice, painting, red, swede; house 5: cooking, green, milk, spaniard
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00
