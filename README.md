# The Nerd Bot

## Introduction

This Discord Chatbot, developed in Python, was created during COVID-19 to fetch resources directly from my study resources website (the website is currently shut down). Students had the opportunity to type in commands in any text channel of the Discord Server in which the bot was added, and necessary resources would be delivered to them on demand. Originally, this Bot used to run in Repl.it, triggered by periodic pings from Uptime Robot so that the bot’s source code ran continuously. This GitHub repository was created to facilitate reviewing the project by Caltech admissions.

## Getting Started

To trigger the bot, begin any command with the “::” prefix. In the chatbox.

Ex: `::give \[sub\] \[ch\]`

NOTE: Since this bot was created in 2020-2021, slash commands now currently available in Discord is not incorporated in this bot.

## Command List with Parameters

| Command | Aliases (if any) | Parameters | Description |
| --- | --- | --- | --- |
| `ping` | N/A | N/A |  |
| `predict` | `pwheel, divination, 8ball` | `question` (Users input question) | Gives “prediction” for any Yes/No question |
| `give` | N/A | `sub` (subject code) `ch` (chapter no) | Provides notes of specific topic, or routine of specific section, based on arguments provided. Returns link to command list if invalid parameters input. |
| `joinclass` | N/A | `sub` (subject code) | Returns Zoom Class Link based on arguments provided. |
| `help` | N/A | N/A | Returns command list in website |

## Supported Subject Code List

| Subject Code | Subject |
| --- | --- |
|  `ban1` | Bengali-1 (Literature) |
| `ban2` | Bengali-2 (Language) |
| `phys` | Physics |
| `chem` | Chemistry |
| `biol` | Biology |
| `bstu` | Bangladesh Studies |
| `econ` | Economics |
| `comp` | Computer Science |
| `eng2` | English Language |
| `eng1` | English Literature |
| `admt` | Additional Mathematics |
| `matd` | Mathematics-D |
| `routine` | Used to fetch class routine (only available in give command) |

## Disclaimer

1.  The website from which the bot fetched resources is currently shut down and not available following the end of pandemic. Some links may not work.
2.  Most of the Zoom class links, links to notes, and the Discord API Token Number have been removed from the source code for confidentiality.
