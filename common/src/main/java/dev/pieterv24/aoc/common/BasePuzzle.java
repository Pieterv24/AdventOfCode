package dev.pieterv24.aoc.common;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public abstract class BasePuzzle {
    protected abstract String processAnswer(List<String> lines);

    public void run(InputType inputType) {
        IO.println(String.format("The answer is: %s", this.processAnswer(readAllLines(inputType))));
    }

    // Inefficient, but easy
    public List<String> readAllLines(InputType inputType) {
        List<String> lines = new ArrayList<>();
        try (InputStream input = BasePuzzle.class.getClassLoader().getResourceAsStream(inputType.getFileName())) {
            if (input == null) {
                IO.println("File not found in resources!");
                return lines;
            }

            try (BufferedReader reader = new BufferedReader(new InputStreamReader(input))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    lines.add(line);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return lines;
    }
}
