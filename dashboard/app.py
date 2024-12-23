from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/analytics_dash')
def analytics_dashboard(methods=["GET", "POST"]):
    if request.method == "GET":
        lecture_data = {
                    "1": {
                        "1": [78, 85, 92],
                        "2": [90, 76, 83],
                        "3": [81, 65, 79],
                        "4": [88, 91, 77],
                        "5": [94, 89, 72],
                        "6": [70, 82, 84],
                        "7": [95, 88, 79],
                        "8": [78, 82, 89],
                        "9": [84, 90, 79],
                    },
                    "2": {
                        "1": [86, 91, 77],
                        "2": [93, 80, 78],
                        "3": [79, 91, 88],
                        "4": [95, 84, 77],
                        "5": [81, 83, 79],
                        "6": [93, 82, 84],
                        "7": [88, 90, 89],
                        "8": [76, 85, 94],
                        "9": [95, 87, 79],
                    },
                    "3": {
                        "1": [75, 84, 89],
                        "2": [90, 82, 88],
                        "3": [79, 86, 81],
                        "4": [94, 78, 85],
                        "5": [89, 82, 76],
                        "6": [83, 79, 90],
                        "7": [77, 91, 92],
                        "8": [85, 83, 88],
                        "9": [78, 89, 92],
                    },
                    
                }

        dummy_scores = [7, 7, 7, 4, 8, 9, 8, 7, 3, 4, 8, 4, 8, 10, 5, 6, 9, 7, 4, 5]
        lec_scores_hmap = {
            1: [7, 8, 3, 8, 9],
            2: [7, 9, 4, 10, 7],
            3: [7, 8, 8, 5, 4],
            4: [4, 7, 4, 6, 5]
        }
        averages = {
            subject: f"{float(sum(sum(lectures.values(), [])) / len(sum(lectures.values(), []))):.2f}"
            for subject, lectures in lecture_data.items()
        }
        weaks = {
            subject: min(lectures.values())
            for subject, lectures in lecture_data.items()
        }

        avg = 0
        for i in range(len(dummy_scores)):
            avg += dummy_scores[i]
        avg = avg / len(dummy_scores)
        data = {
            'scores': dummy_scores, #1/10
            'score_avg': avg,
            'lec_scores': lec_scores_hmap,
            'lec_data': lecture_data
            # 'recent_activity': [
            #     {'user': 'Alice', 'action': 'Logged In', 'time': '10:00 AM'},
            #     {'user': 'Bob', 'action': 'Purchased Item', 'time': '10:05 AM'},
            #     {'user': 'Charlie', 'action': 'Logged Out', 'time': '10:15 AM'},
            # ],

        }
        return render_template('dashboard.html', data=data, averages=averages, weaks=weaks)

@app.route("/subject_analytics/<subjectid>")
def analyze_subject(subjectid):
    subdata = {"subname":{"1": [78, 85, 92],
                        "2": [90, 76, 83],
                        "3": [81, 65, 79],
                        "4": [88, 91, 77],
                        "5": [94, 89, 72],
                        "6": [70, 82, 84],
                        "7": [95, 88, 79],
                        "8": [78, 82, 89],
                        "9": [84, 90, 79],
            }}
    return render_template('subanalytics.html', subdata=subdata)

if __name__ == '__main__':
    app.run(debug=True)
