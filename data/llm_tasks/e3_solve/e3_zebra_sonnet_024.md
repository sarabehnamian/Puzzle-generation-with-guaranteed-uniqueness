# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_024.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00885-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Norwegian, Brit, Dane, Spaniard
- job: lawyer, pilot, farmer, doctor, teacher
- hobby: cooking, tennis, painting, hiking, golf
- pet: fish, horse, cat, rabbit, dog

Clues:
1. The person who keeps the rabbit and the Spaniard are neighbours.
2. The doctor and the golf enthusiast are not neighbours.
3. The painting enthusiast is not the Spaniard.
4. The dog owner lives in house 4.
5. The farmer lives somewhere to the left of the German.
6. The farmer keeps the rabbit.
7. The Dane and the tennis enthusiast live in adjacent houses.
8. The Norwegian and the owner of the rabbit live in adjacent houses.
9. The person who enjoys hiking lives in house 3.
10. The Spaniard lives directly to the left of the farmer.
11. The doctor lives directly to the left of the person who enjoys tennis.
12. The hiking enthusiast either works as the pilot or works as the teacher.
13. The cooking enthusiast lives next to the teacher.
14. The doctor and the Norwegian are neighbours.
15. The cooking enthusiast lives immediately to the right of the Norwegian.
16. The tennis enthusiast works as the pilot.
17. The owner of the cat and the person who keeps the rabbit are neighbours.
18. The Dane and the fish owner live in adjacent houses.
19. The Brit and the person who enjoys hiking live in adjacent houses.
20. The golf enthusiast does not live next to the Norwegian.
21. The Brit does not live next to the dog owner.
22. The Spaniard keeps the cat.
23. The teacher keeps the horse.
24. The owner of the horse either enjoys cooking or enjoys hiking.
25. The farmer does not live in the first house.
26. The painting enthusiast lives in the second house.
27. The person who keeps the horse and the lawyer are not neighbours.
28. The doctor lives in the fourth house.
29. The rabbit owner does not live in the fifth house.
30. The person who enjoys painting does not keep the fish.
31. The dog owner and the pilot are neighbours.
32. The person who keeps the rabbit lives next to the teacher.
33. The painting enthusiast does not live in house 1.
34. The Spaniard and the horse owner are different people.
35. There is exactly one house between the Brit and the dog owner.
36. The Spaniard and the hiking enthusiast are different people.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
