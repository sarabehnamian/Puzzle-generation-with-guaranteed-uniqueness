# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_009.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00829

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, white, purple, green, blue
- drink: coffee, juice, cocoa, milk, water
- nationality: Spaniard, Norwegian, Dane, German, Swede
- hobby: hiking, cooking, chess, painting, golf

Clues:
1. The Norwegian lives in the green house.
2. The person who drinks milk lives at one end of the row.
3. The painting enthusiast and whoever lives in the white house are neighbours.
4. The Dane and the hiking enthusiast are neighbours.
5. The person who drinks cocoa lives in the house just left of the one where the person who enjoys golf lives.
6. The Spaniard either drinks cocoa or drinks milk.
7. The person in the green house lives next to the Spaniard.
8. The person in the purple house lives somewhere to the right of the Dane.
9. The person in the red house lives directly to the left of the coffee drinker.
10. The person who drinks water lives in the house just left of the one where whoever lives in the green house lives.
11. The cooking enthusiast lives immediately to the right of the German.
12. The German and whoever lives in the white house live two houses apart.
13. Whoever lives in the red house lives somewhere to the right of the person who enjoys hiking.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
