import difflib
import webbrowser
import time
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


'''
@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]


    return render_template('index.html', name = name)
'''    

@app.route('/distance',methods=['POST', 'GET'])
def distance(w1, w2):
    while True:
        w1 = input('Enter first word: ')
        w2 = input('Enter second word: ')
        if (str.isalpha(w1) == False or str.isalpha(w2) == False):
            print("Sorry, please input only letters, or input quit to exit")
            continue
        elif(w1 == "exit" or w2 == "exit"):
            quit()
        else:
            return


    r = len(w1) + 1
    c = len(w2) + 1

    word_distance = [[
        0 for i in range(c)
    ]
        for i in range(r)
    ]

    print('\n','Matrix:')

    for i in range(1, r):
        word_distance[i][0] = i

    for i in range(1, c):
        word_distance[0][i] = i

    for column in range(1, c):
        for row in range(1, r):
            if w1[row-1] == w2[column-1]:
                incr = 0
            else:
                incr = 1

            word_distance[row][column] = min(word_distance[row-1][column] + 1, word_distance[row][column-1] + 1, word_distance[row-1][column-1] + incr)
    
    for display in range(r):
        print(word_distance[display])

    return word_distance[row][column]


    return render_template('index.html', w1 = w1, w2 = w2)

print('Edit Distance: ',distance('word1', 'word2'))
    



if __name__ == "__main__":
    app.run(debug=True)



