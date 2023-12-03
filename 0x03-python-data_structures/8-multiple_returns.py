#!/usr/bin/python3
def multiple_returns(sentence):
    return (0, "None") if sentence == "" else (len(sentence), sentence[0])