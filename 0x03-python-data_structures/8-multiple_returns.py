#!/usr/bin/python3
def multiple_returns(sentence):
    match (len(sentence)):
        case 0:
            return 0, None
        case x:
            return x, sentence[0]
