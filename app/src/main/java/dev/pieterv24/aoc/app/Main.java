package dev.pieterv24.aoc.app;

import java.util.List;

import dev.pieterv24.aoc.common.InputType;
import dev.pieterv24.aoc.day01.Puzzle1;
import dev.pieterv24.aoc.day01.Puzzle2;

public class Main {
    public static void main(String[] args) {
        IO.println("Welcome to the Advent of Code!");

        List.of(args).stream().forEach(arg -> {
            IO.println(arg);
        });

        Puzzle1 puzzle1 = new Puzzle1();
        puzzle1.run(InputType.INPUT);

        Puzzle2 puzzle2 = new Puzzle2();
        puzzle2.run(InputType.INPUT);
    }
}
