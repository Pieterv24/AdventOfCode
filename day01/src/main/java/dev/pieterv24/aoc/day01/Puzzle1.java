package dev.pieterv24.aoc.day01;

import java.util.ArrayList;
import java.util.List;

import dev.pieterv24.aoc.common.BasePuzzle;

public class Puzzle1 extends BasePuzzle {

    @Override
    protected String processAnswer(List<String> lines) {
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        Integer answer = 0;

        lines.stream().forEach(line -> {
            String[] split = line.split("   ");
            list1.add(Integer.parseInt(split[0]));
            list2.add(Integer.parseInt(split[1]));
        });

        List<Integer> sortedList1 = list1.stream().sorted().toList();
        List<Integer> sortedList2 = list2.stream().sorted().toList();

        for(int i = 0; i < sortedList1.size(); i++) {
            Integer distance = Math.abs(sortedList1.get(i) - sortedList2.get(i));
            answer += distance;
        }

        return answer.toString();
    }
    
}
