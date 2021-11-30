import difflib
import webbrowser
import time


from flask import Flask, render_template, url_for, request

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]


    return render_template('index.html', name = name)
    




if __name__ == "__main__":
    app.run(debug=True)
















def distance(w1, w2):

    w1 = input('Enter first word: ')
    w2 = input('Enter seond word: ')

#matrix of edit distance
    r = len(w1) + 1
    c = len(w2) + 1
    align = ''

    edit_distance = [[
        0 for i in range(c)
    ]
        for i in range(r)
    ]

    print('\n','Matrix:')

    for i in range(1, r):
        edit_distance[i][0] = i

    for i in range(1, c):
        edit_distance[0][i] = i

    for column in range(1, c):
        for row in range(1, r):
            if w1[row-1] == w2[column-1]:
                incr = 0
            else:
                incr = 1

            edit_distance[row][column] = min(edit_distance[row-1][column] + 1, edit_distance[row][column-1] + 1, edit_distance[row-1][column-1] + incr)
    
    for display in range(r):
        print(edit_distance[display])

    return edit_distance[row][column]

print('Edit Distance: ',distance('word1', 'word2'))
