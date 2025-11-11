pluginManagement {
    // Include 'plugins build' to define convention plugins.
    includeBuild("build-logic")
}

plugins {
}

rootProject.name = "AdventOfCode"
include("app", "common")
