import os
from flask import Flask, redirect, request, render_template
import sqlite3

DATABASE = "sql/client_information.db"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


@app.route("/Home", methods=['POST', 'GET'])
def addContractorDetails():
    if request.method == 'GET':
        return render_template('first_page.html')
    if request.method == 'POST':
        fieldlist = ['title', 'firstName', 'surname', 'gender', 'dob', 'niNumber', 'eAddress', 'contactNumber',
                     'postCode', 'addressLine1', 'addressLine2', 'addressLine3', 'town', 'emergContact',
                     'emergContactNumber', 'workReq', 'quali', 'nameOfCompany', 'eligibility',
                     'proofOfEligibility', 'licence', 'criminalConviction', 'criminalDetails', 'disability',
                     'disabilityDetails', 'refereeName1', 'refereeJob1', 'refereeComp1', 'refereeAddress1',
                     'refereeNum1', 'refereeEmail1', 'refereeName2', 'refereeJob2', 'refereeComp2', 'refereeNum2',
                     'refereeAddress2', 'refereeEmail2']
        valuelist = []
        for i in fieldlist:
            valuelist.append(request.form.get(i, default="Error"))
        # title = request.form.get('title', default="Error")
        print("inserting contractor " + valuelist[1])
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO form_data ('title', 'firstName', 'surname', 'gender',\
                                    'dob', 'niNumber', 'eAddress', 'contactNumber','postCode', 'addressLine1',\
                                    'addressLine2', 'addressLine3', 'town', 'emergContact','emergContactNumber',\
                                    'workReq', 'quali', 'nameOfCompany', 'eligibility', 'proofOfEligibility', 'licence',\
                                    'criminalConviction', 'criminalDetails', 'disability','disabilityDetails',\
                                    'refereeName1', 'refereeJob1', 'refereeComp1', 'refereeAddress1','refereeNum1',\
                                    'refereeEmail1','refereeName2', 'refereeJob2', 'refereeComp2','refereeAddress2',\
                                    'refereeNum2','refereeEmail2')\
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (valuelist[0],\
                                valuelist[1], valuelist[2], valuelist[3], valuelist[4], valuelist[5],\
                                valuelist[6], valuelist[7], valuelist[8], valuelist[9], valuelist[10],\
                                valuelist[11], valuelist[12], valuelist[13], valuelist[14], valuelist[15],\
                                valuelist[16], valuelist[17], valuelist[18], valuelist[19], valuelist[20],\
                                valuelist[21], valuelist[22], valuelist[23], valuelist[24], valuelist[25],\
                                valuelist[26], valuelist[27], valuelist[28], valuelist[29], valuelist[30],\
                                valuelist[31], valuelist[32], valuelist[33], valuelist[34], valuelist[35], valuelist[36]))
            conn.commit()
            msg = "Record sucessfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg

if __name__ == '__main__':
    app.run(debug=True)
