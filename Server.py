import os
import random
from flask import Flask, redirect, request, render_template, url_for, make_response, g, session
import sqlite3
import time


DATABASE = "sql/client_information.db"
CV_ALLOWED_EXTENSIONS = set(['doc', 'pdf', 'docx'])
PIC_ALLOWED_EXTENSIONS = set(['png', 'PNG', 'jpg', 'jpeg', 'gif'])
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
CV_UPLOAD_FOLDER = os.path.join(APP_ROOT,'static/uploads/cvs')
PIC_UPLOAD_FOLDER = os.path.join(APP_ROOT,'static/uploads/pictures')

app = Flask(__name__)
app.config['CV_UPLOAD_FOLDER'] = CV_UPLOAD_FOLDER
app.config['PIC_UPLOAD_FOLDER'] = PIC_UPLOAD_FOLDER

def allowedFile(filename, filetype):
    ext = filename.rsplit('.',1)[1]
    if filetype == 'CV':
        return '.' in filename and ext in CV_ALLOWED_EXTENSIONS
    if filetype =='PIC':
        return '.' in filename and ext in PIC_ALLOWED_EXTENSIONS

@app.route("/Landing", methods=['GET'])
def landingPage():
    if request.method=='GET':
        return render_template('landing_page.html')

app.secret_key = os.urandom(24)

@app.route('/Login', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('login.html')
    if request.method == 'POST':
        session.pop('user', None)
        if request.form['password'] == 'password':
            session['user'] = request.form['userName']
            return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/protected')
def protected():
    if g.user:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT postCode FROM contactInformation")
        data = cur.fetchall()
        usableData = [x[0] for x in data]
        jsonString = {"postcodes": usableData}
        return render_template('admin.html',data=jsonString)
    return redirect(url_for('getsession'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Sorry you are not logged in'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Signed out'

@app.route("/Form", methods=['GET', 'POST'])
def addContractorDetails():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        cvPath = cvUpload()
        picPath = picUpload()
        fieldlist = ['title', 'firstName', 'surname', 'gender', 'dob', 'niNumber', 'eAddress', 'contactNumber',
                     'postCode', 'addressLine1', 'addressLine2', 'addressLine3', 'town', 'emergContact',
                     'emergContactNumber', 'workReq', 'quali', 'nameOfCompany', 'eligibility',
                     'proofOfEligibility', 'licence', 'criminalConviction', 'criminalDetails', 'disability',
                     'disabilityDetails', 'refereeName1', 'refereeJob1', 'refereeComp1', 'refereeAddress1',
                     'refereeNum1', 'refereeEmail1', 'refereeName2', 'refereeJob2', 'refereeComp2', 'refereeNum2',
                     'refereeAddress2', 'refereeEmail2', 'userName', 'password']
        valuelist = []
        for i in fieldlist:
            valuelist.append(request.form.get(i, default="Error"))
        print("inserting contractor " + valuelist[1])

        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT eAddress FROM contactInformation")
        data = cur.fetchall()
        if request.form.get('eAddress') not in data:
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute("INSERT INTO personalInformation ('title', 'firstName', 'surname', 'gender',\
                                         'dob', 'niNumber') VALUES (?,?,?,?,?,?)", (valuelist[0],valuelist[1],\
                                        valuelist[2], valuelist[3], valuelist[4],valuelist[5]))

                cur.execute("INSERT INTO contactInformation ('eAddress', 'contactNumber','postCode', 'addressLine1',\
                                           'addressLine2', 'addressLine3', 'town', 'emergContact','emergContactNumber')\
                                            VALUES (?,?,?,?,?,?,?,?,?)", (valuelist[6],valuelist[7], valuelist[8],\
                                            valuelist[9],valuelist[10],valuelist[11], valuelist[12], valuelist[13], valuelist[14]))

                cur.execute("SELECT userID FROM contactInformation WHERE eAddress=?;", [request.form.get('eAddress')])
                userID = cur.fetchall()
                userID = [x[0] for x in userID]
                userID = userID[0]
                print(userID)

                cur.execute("INSERT INTO workInformation ('workReq', 'quali', 'nameOfCompany')\
                                            VALUES (?,?,?)", (valuelist[15], valuelist[16], valuelist[17]))

                cur.execute("INSERT INTO extendedInformation ('eligibility', 'proofOfEligibility', 'licence',\
                                           'criminalConviction', 'criminalDetails', 'disability','disabilityDetails')\
                                            VALUES (?,?,?,?,?,?,?)", (valuelist[18], valuelist[19],valuelist[20],\
                                            valuelist[21],valuelist[22], valuelist[23], valuelist[24]))

                res = [(userID, valuelist[25],valuelist[26],valuelist[27],valuelist[28],valuelist[29],valuelist[30]),(userID, valuelist[31],valuelist[32],valuelist[33],valuelist[34],valuelist[35],valuelist[36])]
                cur.executemany("INSERT INTO referees ('userID','refereeName', 'refereeJob', 'refereeCompany',\
                                            'refereeAddress', 'refereePhoneNumber', 'refereeEmail')\
                                            VALUES (?,?,?,?,?,?,?)", res)

                cur.execute("INSERT INTO accountAndUploads ('userName', 'password', 'cvFilePath','picFilePath')\
                                            VALUES (?,?,?,?)", (valuelist[37], valuelist[38], cvPath, picPath))
                conn.commit()
                msg = "Record sucessfully added"
            except Exception as e:
                 conn.rollback()
                 msg = "Error in insert operation: " + str(e)
            finally:
                conn.close()
                if msg == "Record sucessfully added":
                    return render_template("form_completion.html")
                else:
                    return msg
        else:
            return "Email already used"

def cvUpload():
    if 'CV' not in request.files:
        print("No file received")
    else:
        cv = request.files["CV"]
        if cv.filename == "":
            print("File name blank")
        elif cv and allowedFile(cv.filename, 'CV'):
            filename = secureFilename(cv.filename, 'CV')
            filePath = os.path.join(app.config['CV_UPLOAD_FOLDER'], filename)
            cv.save(filePath)
            return filePath

def picUpload() :
    if 'profileImage' not in request.files:
        print("No picture received")
    else:
        pic = request.files["profileImage"]
        if pic.filename == "":
            print("Picture name blank")
        elif pic and allowedFile(pic.filename, 'PIC'):
            filename = secureFilename(pic.filename, 'Picture')
            filePath = os.path.join(app.config['PIC_UPLOAD_FOLDER'], filename)
            pic.save(filePath)
            return filePath

def secureFilename(filename, filetype):
    first = request.form.get('firstName')
    last = request.form.get('surname')
    main = str(first) + str(last) + filetype +"."+ filename.rsplit('.',1)[1]
    return main

def pdfFilename(filetype):
    first = request.form.get('firstName')
    last = request.form.get('surname')
    main = str(first) + str(last) + filetype +".pdf"
    return main

@app.route("/FormCompletion", methods=['GET'])
def thankYouPage():
    if request.method=='GET':
        return render_template("form_completion.html")

@app.route("/Admin", methods=['GET'])
def adminSearch():
    if request.method == 'POST':
        try:
            surname = request.form.get('surname', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM personalInformation WHERE surname=?;", [surname])
            data = cur.fetchall()
            print(data)
            return render_template('admin.html',data=jsonString)
        except:
            print('There was an error', data)
            conn.close()
        finally:
            conn.close()
            return render_template('list_data.html', data = data)

if __name__ == '__main__':
    app.run(debug=True)
