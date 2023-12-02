package dev.pieterv24

import org.apache.commons.cli.CommandLineParser
import org.apache.commons.cli.DefaultParser
import org.apache.commons.cli.HelpFormatter
import org.apache.commons.cli.Option
import org.apache.commons.cli.Options
import org.apache.commons.cli.ParseException
import kotlin.system.exitProcess

val helpOption = Option.builder("h").longOpt("help").desc("Display Help menu").build()

fun main(args: Array<String>) {
    val options = Options()

    options.addOption(Option.builder("d").longOpt("day").hasArg()
        .desc("Select what day's algorithm to use.").type(Int::class.java).required().build())
    options.addOption(Option.builder("i").longOpt("input").hasArg()
        .desc("Input file").type(String::class.java).required().build())
    options.addOption(Option.builder("p").longOpt("part").hasArg()
        .desc("For what part to run the program").type(Int::class.java).build())
    options.addOption(helpOption)

    if (displayHelp(args)) {
        val helpFormatter = HelpFormatter()
        helpFormatter.printHelp("Help", options)
        return
    }

    val parser: CommandLineParser = DefaultParser()
    try {
        val cmd = parser.parse(options, args)
        val day: Int = cmd.getOptionValue("day").toInt()
        val input: String = cmd.getOptionValue("input")
        val part: Int = cmd.getOptionValue("part", "1").toInt()

    } catch (e: ParseException) {
        System.err.println("Error: " + e.message)
        exitProcess(1)
    }


}

fun displayHelp(args: Array<String>): Boolean {
    val helpOptions = Options()
    helpOptions.addOption(helpOption)

    val helpParser: CommandLineParser = DefaultParser()
    try {
        val cmd = helpParser.parse(helpOptions, args)

        return cmd.hasOption("help")
    } catch (e: ParseException) {
        return false
    }
}