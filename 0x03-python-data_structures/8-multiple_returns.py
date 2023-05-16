#!/usr/bin/python3
def multiple_returns(sentence):
    lgt = len(sentence)
    return(lgt, sentence[0] if lgt > 0 else None)
