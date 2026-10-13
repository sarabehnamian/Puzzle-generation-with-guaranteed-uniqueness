# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_eval_g1/e4_eval_g1_haiku_004.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle evo-g0-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, tennis, cooking, hiking
- nationality: Norwegian, Swede, German, Spaniard, Dane
- color: red, green, blue, yellow, white
- drink: cocoa, water, tea, milk, juice

Clues:
1. The person who drinks cocoa lives directly to the left of whoever lives in the red house.
2. The Dane lives next to the German.
3. The tea drinker either lives in the red house or lives in the white house.
4. The Swede lives in the house just left of the one where the milk drinker lives.
5. The golf enthusiast drinks water.
6. The German and the occupant of the red house are neighbours.
7. The Dane lives in the house just left of the one where the person in the yellow house lives.
8. The Swede enjoys painting.
9. The person who enjoys golf does not live next to the juice drinker.
10. The Norwegian enjoys tennis.
11. The person in the blue house lives directly to the left of whoever lives in the yellow house.
12. Whoever lives in the white house lives somewhere to the left of the person who enjoys hiking.
13. The painting enthusiast lives in the house just left of the one where the person who enjoys cooking lives.
14. The German and the painting enthusiast are neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-11

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, tennis, cooking, hiking
- nationality: Norwegian, Swede, German, Spaniard, Dane
- color: red, green, blue, yellow, white
- drink: cocoa, water, tea, milk, juice

Clues:
1. The Swede lives directly to the left of the milk drinker.
2. The person who enjoys painting is the Swede.
3. The occupant of the white house lives somewhere to the left of the hiking enthusiast.
4. The German and the person in the red house live in adjacent houses.
5. The occupant of the yellow house lives somewhere to the right of whoever lives in the blue house.
6. The Dane and the German live in adjacent houses.
7. The tea drinker either lives in the red house or lives in the white house.
8. The German and the person who enjoys painting are neighbours.
9. The Dane and the occupant of the yellow house live in adjacent houses.
10. The golf enthusiast drinks water.
11. The cocoa drinker lives in the house just left of the one where whoever lives in the red house lives.
12. The cooking enthusiast lives immediately to the right of the painting enthusiast.
13. The golf enthusiast does not live next to the juice drinker.
14. The person who enjoys tennis is the Norwegian.
15. Whoever lives in the green house and the person who enjoys hiking live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
