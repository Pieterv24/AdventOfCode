package dev.pieterv24.aoc.common;

public class CommonLib {
    private String name;

    public CommonLib(String name) {
        this.name = name;
    }

    public String getGreeting() {
        return String.format("Hello %s", this.name);
    }
}
