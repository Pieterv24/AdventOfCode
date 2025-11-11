package dev.pieterv24.aoc.common;

public class TestLib {
    private String name;

    public TestLib(String name) {
        this.name = name;
    }

    public String getGreeting() {
        return String.format("Hello %s", this.name);
    }
}
