package dev.pieterv24.aoc.day01;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import dev.pieterv24.aoc.common.BasePuzzle;

public class Puzzle2 extends BasePuzzle {

    @Override
    protected String processAnswer(List<String> lines) {
        Map<Integer, Integer> leftMap = new HashMap<>();
        Map<Integer, Integer> rightMap = new HashMap<>();
        Integer answer = 0;

        lines.stream().forEach(line -> {
            String[] split = line.split("   ");
            Integer leftItem = Integer.parseInt(split[0]);
            Integer rightItem = Integer.parseInt(split[1]);

            leftMap.compute(leftItem, (key, value) -> (value == null) ? 1 : value + 1);
            rightMap.compute(rightItem, (key, value) -> (value == null) ? 1 : value + 1);
        });

        answer = leftMap.keySet().stream()
            .filter(key -> leftMap.get(key) > 0)
            .reduce(0, (result, key) -> {
                return result + (leftMap.get(key) * (key * rightMap.getOrDefault(key, 0)));
            });

        return answer.toString();
    }
    
}
