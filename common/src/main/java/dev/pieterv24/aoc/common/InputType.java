package dev.pieterv24.aoc.common;

public enum InputType {
    EXAMPLE("example.txt"),
    INPUT("input.txt");

    private final String fileName;

    private InputType(String fileName) {
        this.fileName = fileName;
    }

    public String getFileName() {
        return this.fileName;
    }
}
