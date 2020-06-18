<h1>Basic Hangman Game</h1>

[![Travis][build-badge]][build]

[build-badge]: https://img.shields.io/travis/dannycrief/the-hangman-game/master.png?style=flat-square
[build]: https://travis-ci.org/github/dannycrief/the-hangman-game

<h4>There Are Three Main Classes:</h4>
<ol>
    <li><b>GuessAttempt:</b> an attempt to guess a letter.</li>
    <li><b>GuessWord:</b> a word to guess. Is used by a HangmanGame to keep track of the word to guess.</li>
    <li><b>HangmanGame:</b> the main interface for the user, the "general" game that will be used.</li>
</ol>

<h4>How To Run:</h4>
<ul>
    <li>python3 main.py</li>
</ul>

<h4>How To Test:</h4>
<ul>
    <li><b>GuessAttempt:</b> <u>py.test test_guess_attempt.py --tb=short</u></li>
    <li><b>GuessWord:</b> <u>py.test test_guess_word.py --tb=short</u></li>
    <li><b>HangmanGame:</b> <u>py.test test_hangman_game.py --tb=short</u></li>
</ul>

<p><b>How To Test Function:</b>
<br>
For example:
<br>
<u>py.test test_hangman_game.py --tb=short -k test_game_wins_several_moves_some_misses</u></p>