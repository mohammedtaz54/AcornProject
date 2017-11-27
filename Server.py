import os
from flask import Flask, redirect, request, render_template
import sqlite3

DATABASE = "sql/client_information.db"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


@app.route("/Home", methods = ['POST', 'GET'])
def addContractorDetails():
    if request.method =='GET':
        return render_template('first_page.html')
    if request.method =='POST':
        fieldlist = ['title', 'firstName', 'surname', 'gender', 'dob', 'niNumber', 'eAddress', 'contactNumber',
                 'postCode', 'addressLine1', 'addressLine2', 'addressLine3', 'town', 'emergContact',
                 'emergContactNumber', 'workReq', 'quali', 'nameOfCompany', 'eligibility',
                 'proofOfEligibility', 'licence', 'criminalConviction', 'criminalDetails', 'disability',
                 'disabilityDetails', 'refereeName1', 'refereeJob1', 'refereeComp1', 'refereeAddress1',
                 'refereeNum1','refereeEmail1', 'refereeName2', 'refereeJob2', 'refereeComp2', 'refereeNum2',
                 'refereeAddress2', 'refereeEmail2']
        valuelist = []
        for i in fieldlist:
            valuelist.append(request.form.get(i, default="Error"))
        # title = request.form.get('title', default="Error")
        print("inserting contractor "+valuelist[1])
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO form_data ('title', 'firstName', 'surname', 'gender', 'dob', 'niNumber', 'eAddress', 'contactNumber','postCode', 'addressLine1', 'addressLine2', 'addressLine3', 'town', 'emergContact','emergContactNumber', 'workReq', 'quali', 'nameOfCompany', 'eligibility',\
                                    'proofOfEligibility', 'licence', 'criminalConviction', 'criminalDetails', 'disability','disabilityDetails', 'refereeName1', 'refereeJob1', 'refereeComp1', 'refereeAddress1','refereeNum1','refereeEmail1','refereeName2', 'refereeJob2', 'refereeComp2','refereeAddress2','refereeNum2','refereeEmail2')\
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (valuelist[0],valuelist[1],valuelist[2],valuelist[3],valuelist[4],valuelist[5],valuelist[6],valuelist[7],valuelist[8],valuelist[9],valuelist[10],valuelist[11],valuelist[12],valuelist[13],\
                            valuelist[14],valuelist[15],valuelist[16],valuelist[17],valuelist[18],valuelist[19],valuelist[20],valuelist[21],valuelist[22],valuelist[23],valuelist[24],valuelist[25],valuelist[26],valuelist[27],valuelist[28],valuelist[29],valuelist[30],valuelist[31],valuelist[32],valuelist[33],\
                            valuelist[34],valuelist[35],valuelist[36]) )
            conn.commit()
            msg = "Record sucessfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return msg


#     dob = request.form.get('dob', default="Error")
#     niNumber = request.form.get('niNumber', default="Error")
#     eAddress = request.form.get('eAddress', default="Error")
#     contactNumber = request.form.get('contactNumber', default="Error")
#     postCode = request.form.get('postCode', default="Error")
#     addressLine1 = request.form.get('addressLine1', default="Error")
#     addressLine2 = request.form.get('addressLine2', default="Error")
#     addressLine3 = request.form.get('addressLine3', default="Error")
#     town = request.form.get('town', default="Error")
#     emergContact = request.form.get('emergContact', default="Error")
#     emergContactNumber = request.form.get('emergContactNumber', default="Error")
#     workReq = request.form.get('workReq', default="Error")
#     quali = request.form.get('quali', default="Error")
#     nameOfCompany = request.form.get('nameOfCompany', default="Error")
#     eligibility = request.form.get('eligibility', default="Error")
#     proofEligibility = request.form.get('proofEligibility', default="Error")
#     licence = request.form.get('licence', default="Error")
#     criminalConviction = request.form.get('criminalConviction', default="Error")
#     criminalDetails = request.form.get('criminalDetails', default="Error")
#     disability = request.form.get('disability', default="Error")
#     disabilityDetails = request.form.get('disabilityDetails', default="Error")
#     RefereeName1 = request.form.get('RefereeName1', default="Error")
#     RefereeJob1 = request.form.get('RefereeJob1', default="Error")
#     RefereeComp1 = request.form.get('RefereeComp1', default="Error")
#     RefereeAddress1 = request.form.get('RefereeAddress1', default="Error")
#     RefereeNum1 = request.form.get('RefereeNum1', default="Error")
#     RefereeEmail1 = request.form.get('RefereeEmail1', default="Error")
#     RefereeName2 = request.form.get('RefereeName2', default="Error")
#     RefereeJob2 = request.form.get('RefereeJob2', default="Error")
#     RefereeComp2 = request.form.get('RefereeComp2', default="Error")
#     RefereeAddress2 = request.form.get('RefereeAddress2', default="Error")
#     RefereeNum2 = request.form.get('RefereeNum2', default="Error")
#     RefereeEmail2 = request.form.get('RefereeEmail2', default="Error")
#     CV = request.form.get('CV', default="Error")


if __name__ == '__main__':
    app.run(debug=True)
