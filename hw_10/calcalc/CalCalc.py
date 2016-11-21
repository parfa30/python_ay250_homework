import argparse
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
from unittest import TestCase

def simple_calc(string):
    """ Need to put something in here to make eval safe"""
    answer = eval(string)
    return answer

def complex_calc(string):

    answers = []
    string_list = string.split()
    new_string = '+'.join(word for word in string_list)
    response = urlopen('http://api.wolframalpha.com/v2/query?input=%s&appid=UAGAWR-3X6Y8W777Q'  % new_string)
    html = response.read()
    soup = BeautifulSoup(html,"html.parser")
    for item in  soup.find_all('img',formatter=None):
        answers.append(item.get('alt'))

    return answers[1]
    
def calculate(string,type=None):
    #First need to do some work on evaluating the string and make sure
    if type == 'simple':
        answer = simple_calc(string)
    elif type == 'complex':
        answer = complex_calc(string)
    else:
        try:
            answer = simple_calc(string)
        except SyntaxError:
            answer = complex_calc(string)
    return answer

def test_1():
    assert abs(1.5 - calculate('3/2')) < 0.001

def test_2():
    assert abs(16 - calculate('4**2')) < 0.001
    
def test_3():
    a = '299792 km/s  (kilometers per second)'
    assert a == calculate('What is the speed of light')

def test_4():
    assert abs(6 - calculate('1+2+3')) < 0.001
    

def test_5():
    assert abs(5.44 - calculate('3.2*1.7')) < .001

        
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='CalCalc')
    parser.add_argument('string_input', help='This is the request and is required')
    parser.add_argument('-s', action='store_true', dest='simple',
                    help='This is a simple calculation')
    parser.add_argument('-c', action='store_true', dest='complex',
                    help='This is a more complex action that is solved using Wolfram Alpha')
    results = parser.parse_args()
    input = results.string_input
    if results.simple:
        type = 'simple'
        x = calculate(input,type)
    elif results.complex:
        type = 'complex'
        x = calculate(input,type)
    else:
        x = calculate(input)
    print(x)
