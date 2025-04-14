from lib.grammar_checker import *

#sentence checker tests
def test_check_capital_pass():
    grammar = GrammarStats()
    result = grammar.check_grammar("This is a sentence.")
    assert result == True

def test_check_capital_fail():
    grammar = GrammarStats()
    result = grammar.check_grammar("this is a sentence")
    assert result == False

def test_check_grammar_last_char_full_stop():
    grammar = GrammarStats()
    result = grammar.check_grammar("This is a sentence.")
    assert result == True

def test_check_grammar_last_char_exclamation():
    grammar = GrammarStats()
    result = grammar.check_grammar("This is a sentence!")
    assert result == True

def test_check_grammar_last_char_question_mark():
    grammar = GrammarStats()
    result = grammar.check_grammar("This is a sentence?")
    assert result == True

def test_check_grammar_last_char_comma():
    grammar = GrammarStats()
    result = grammar.check_grammar("This is a sentence,")
    assert result == False

def test_check_grammar_last_char_none():
    grammar = GrammarStats()
    result = grammar.check_grammar("This is a sentence")
    assert result == False

#percentage checked tests
def test_how_many_sentences_pass():
    grammar = GrammarStats()
    grammar.check_grammar("This is a sentence")
    grammar.check_grammar("This is a sentence?")
    result = grammar.percentage_good()
    assert result == 50