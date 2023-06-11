#!/usr/bin/python3
def multiple_returns(sentence):
    t = len(sentence)
    if t == 0:
        return t, None
    else:
        return t, sentence[0]
