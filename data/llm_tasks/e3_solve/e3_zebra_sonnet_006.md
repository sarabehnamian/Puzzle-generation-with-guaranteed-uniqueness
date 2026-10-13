# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e3_solve/e3_zebra_sonnet_006.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01305

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, farmer, pilot, baker, lawyer
- color: white, yellow, purple, blue, green
- hobby: hiking, chess, tennis, cooking, painting
- nationality: Swede, Dane, Spaniard, Norwegian, Brit

Clues:
1. There is exactly one house between the chess enthusiast and the lawyer.
2. The occupant of the blue house lives somewhere to the right of the person in the white house.
3. The Dane enjoys chess.
4. The Swede lives next to the tennis enthusiast.
5. The Spaniard lives immediately to the right of the baker.
6. The Spaniard lives in the blue house.
7. The person who enjoys painting lives in the purple house.
8. The baker is the Norwegian.
9. The farmer lives immediately to the right of the person in the white house.
10. The person who enjoys cooking does not live in house 5.
11. The baker lives directly to the left of the lawyer.
12. The occupant of the green house lives immediately to the right of the person in the white house.
13. The person who enjoys hiking either works as the farmer or works as the pilot.
14. The pilot and the person in the yellow house are different people.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00360

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Spaniard, Dane, Norwegian, Brit
- hobby: tennis, hiking, cooking, painting, golf
- color: purple, green, yellow, white, red
- drink: coffee, juice, cocoa, tea, milk

Clues:
1. The Dane lives next to the golf enthusiast.
2. The Brit lives directly to the left of the person who enjoys golf.
3. The coffee drinker lives in the third house.
4. The person in the white house lives in the house just left of the one where the milk drinker lives.
5. The cooking enthusiast lives next to the person who enjoys tennis.
6. The Norwegian lives in the purple house.
7. The person who drinks cocoa lives somewhere to the left of the person who drinks tea.
8. The occupant of the red house lives in the house just left of the one where the person who drinks tea lives.
9. The tea drinker enjoys tennis.
10. The person who enjoys cooking either lives in the purple house or lives in the white house.
11. The occupant of the green house and the person who enjoys painting live two houses apart.
12. The coffee drinker and the German live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
