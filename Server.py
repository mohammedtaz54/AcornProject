import os
import random
from flask import Flask, redirect, request, render_template
import sqlite3

DATABASE = "sql/client_information.db"
CV_ALLOWED_EXTENSIONS = set(['doc', 'doc', 'docx'])
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

@app.route("/Login", methods=['POST', 'GET'])
def loginToForm():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        userName = request.form.get('userName', default="Error")
        password = request.form.get('password', default="Error")
        uniqueID = request.form.get('uniqueID', default="Error")
        if userName == 'admin' and password == 'admin' and uniqueID == '555':
            return render_template('admin.html')

@app.route("/Form", methods=['POST', 'GET'])
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
        userID = random.randint(0, 9999)
        print("inserting contractor " + valuelist[1])
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO personalDetails ('userID', 'title', 'firstName', 'surname', 'gender',\
                                     'dob', 'niNumber') VALUES (?,?,?,?,?,?,?)", (userID, valuelist[0],valuelist[1],\
                                    valuelist[2], valuelist[3], valuelist[4],valuelist[5]))
            conn.commit()
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO contactInformation ('userID', 'eAddress', 'contactNumber','postCode', 'addressLine1',\
                                       'addressLine2', 'addressLine3', 'town', 'emergContact','emergContactNumber')\
                                        VALUES (?,?,?,?,?,?,?,?,?,?)", (userID, valuelist[6],valuelist[7], valuelist[8],\
                                        valuelist[9],valuelist[10],valuelist[11], valuelist[12], valuelist[13], valuelist[14]))
            conn.commit()
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO workInformation ('userID', 'workReq', 'quali', 'nameOfCompany')\
                                        VALUES (?,?,?,?)", (userID, valuelist[15], valuelist[16], valuelist[17]))
            conn.commit()
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO extendedInformation ('userID', 'eligibility', 'proofOfEligibility', 'licence',\
                                       'criminalConviction', 'criminalDetails', 'disability','disabilityDetails')\
                                        VALUES (?,?,?,?,?,?,?,?)", (userID, valuelist[18], valuelist[19],valuelist[20],\
                                        valuelist[21],valuelist[22], valuelist[23], valuelist[24]))
            conn.commit()
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            res = [(userID, valuelist[25],valuelist[26],valuelist[27],valuelist[28],valuelist[29],valuelist[30]),(userID,valuelist[31],valuelist[32],valuelist[33],valuelist[34],valuelist[35],valuelist[36])]
            cur.executemany("INSERT INTO referees ('userID', 'refereeName', 'refereeJob', 'refereeCompany',\
                                        'refereeAddress', 'refereePhoneNumber', 'refereeEmail')\
                                        VALUES (?,?,?,?,?,?,?)", res)
            conn.commit()
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO accountAndUploads ('userID', 'userName', 'password', 'cvFilePath','picFilePath')\
                                        VALUES (?,?,?,?,?)", (userID, valuelist[37], valuelist[38], cvPath, picPath))
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

@app.route("/Admin", methods=['POST', 'GET'])
def adminSearch():
    if request.method == 'GET':
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT postCode FROM contactInformation")
        data = cur.fetchall()
        usableData = [x[0] for x in data]
        jsonString = {"postcodes": usableData}
        print(jsonString)
        return render_template('admin.html',data=jsonString)
    if request.method == 'POST':
        try:
            surname = request.form.get('surname', default="Error")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM personalDetails WHERE surname=?;", [surname])
            data = cur.fetchall()
            print(data)
        except:
            print('There was an error', data)
            conn.close()
        finally:
            conn.close()
            return render_template('list_data.html', data = data)

@app.route('/Email')
def email():
    return render_template('inProgressPages/emailing_page.html')

if __name__ == '__main__':
    app.run(debug=True)
