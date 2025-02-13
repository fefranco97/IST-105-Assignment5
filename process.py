import sys
import random
    
inputNumber = int(sys.argv[1])
message = sys.argv[2]


def numberPuzzle(number):
    if number % 2 == 0:
        numberType = "even"
        result = number ** 0.5
    else:
        numberType = "odd"
        result = number ** 3
    return result, numberType

def textPuzzle(message):
    binary = ''.join(format(ord(i), '08b') for i in message)
    vowels = 0
    for i in message:
        if i in "aeiouAEIOU":
            vowels += 1
    return binary, vowels

def treasureHunt():
    number = random.randint(1, 100)
    attempts = 0
    while attempts < 5:
        guess = random.randint(1, 100)
        if guess == number:
            isFound = 'Found'
            break
        elif guess < number:
            isFound = 'Not Found'
        elif guess > number:
            isFound = 'Not Found'
        
        attempts += 1
        
    return number, attempts, guess, isFound

result, numberType = numberPuzzle(inputNumber)
binary, vowels = textPuzzle(message)
number, attempts, guess, found =  treasureHunt()

print(f"""
<html>
<body>
    <main 
    style="
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
    padding: 1rem;
    border-radius: 0.45rem;
    margin: auto;
    max-width: fit-content;
    ">   
    
        <h1>Assignment 5 - Felipe Franco de Camargo</h1>
        <h2>Number Puzzle</h2>
        <p>Input number: {inputNumber} is {numberType}. Its calculation is {result}</p>
        <h2>Text Puzzle</h2>
        <p>
           Its binary representation is:  {binary}
        </p>
        <p>
           Input text: {message} has {vowels} vowels. 
        </p>
        
        <h2>Treasure Hunt</h2>
        <p> 
            <ul>  
                <li>Random number: {number}</li>
                <li>Attempts: {attempts}</li>
                <li>Your last guess: {guess}</li>
                <li>Is the treasure found? {found}</li>
            </ul>
        </p>        
    </main>
</body>
</html>
""")
    
    

