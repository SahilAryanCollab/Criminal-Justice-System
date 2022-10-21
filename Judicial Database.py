from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
import mysql.connector as mdb

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        # Loading the created UI file in the class
        uic.loadUi("tr1.ui", self)
        # Setting title of the window
        self.setWindowTitle("Judicial System")

        #Stacked Widget Declaration
        self.lay1 = self.findChild(QStackedWidget,"stackedWidget")
        self.lay1.setCurrentIndex(0)

        #Page 1
        self.stat = self.findChild(QLabel,"status")
        self.user_input = self.findChild(QLineEdit,"username_input")
        self.pass_input = self.findChild(QLineEdit,"password_input")
        self.log_in = self.findChild(QPushButton,"pushButton")


        #Page 2
        self.criminal_db = self.findChild(QPushButton,"criminal_dbs")
        self.criminal_trial_db = self.findChild(QPushButton,"criminal_trial_dbs")
        self.case_rec_db = self.findChild(QPushButton,"case_records_dbs")

        #Criminal Database
        self.crim_name1 = self.findChild(QLineEdit,"crim_name_input1")
        self.crim_age_less_than = self.findChild(QLineEdit,"age_less_than_input")
        self.crim_age_greater_than = self.findChild(QLineEdit,"age_greater_than_input")
        self.crim_crime = self.findChild(QComboBox,"crime_options")
        self.exit1 = self.findChild(QPushButton,"exit_pro")
        self.lst1 = self.findChild(QTableWidget,"table1")
        self.s1 = self.findChild(QPushButton,"pushButton_2")
        self.log_out1 = self.findChild(QPushButton,"Log_Out")
        self.back_1 = self.findChild(QPushButton,"back_1")
        self.stat.setHidden(True)

        #Criminal Trial
        self.crim_name2 = self.findChild(QLineEdit, "crim_name_input_3")
        self.lawyer_name = self.findChild(QLineEdit, "law_name")
        self.judge_name = self.findChild(QLineEdit,"judge_input")
        self.tri_date = self.findChild(QLineEdit, "trial_date")
        self.exit2 = self.findChild(QPushButton, "exit_pro_3")
        self.lst2 = self.findChild(QTableWidget, "table2")
        self.s2 = self.findChild(QPushButton, "s2")
        self.log_out2 = self.findChild(QPushButton, "Log_Out_3")
        self.back_2 = self.findChild(QPushButton,"back_2")

        #Case Records Database
        self.crim_name3 = self.findChild(QLineEdit,"crim_name_input_5")
        self.lawyer_name1 = self.findChild(QLineEdit,"law_name_3")
        self.judge_name1 = self.findChild(QLineEdit,"judge_input_3")
        self.lst3 = self.findChild(QTableWidget,"table3")
        self.s3 = self.findChild(QPushButton,"s3")
        self.log_out3 = self.findChild(QPushButton,"Log_Out_6")
        self.exit3 = self.findChild(QPushButton,"exit_pro_6")
        self.back_2 = self.findChild(QPushButton,"back_2")

        #Connections from buttons to their functions
        self.log_in.clicked.connect(self.logi)
        self.criminal_db.clicked.connect(self.pg_criminal)
        self.criminal_trial_db.clicked.connect(self.pg_criminal_trial)
        self.case_rec_db.clicked.connect(self.pg_records)
        self.exit1.clicked.connect(self.leave)
        self.exit2.clicked.connect(self.leave)
        self.exit3.clicked.connect(self.leave)
        self.s1.clicked.connect(self.select_data_criminal)
        self.s2.clicked.connect(self.select_data_criminal_trial)
        self.s3.clicked.connect(self.select_data_records)
        self.log_out1.clicked.connect(self.log_out)
        self.log_out2.clicked.connect(self.log_out)
        self.log_out3.clicked.connect(self.log_out)
        self.back_1.clicked.connect(self.backing)
        self.back_2.clicked.connect(self.backing)
        self.back_3.clicked.connect(self.backing)

        self.showMaximized()

    def pg_criminal(self):
        self.lay1.setCurrentIndex(2)
    def pg_criminal_trial(self):
        self.lay1.setCurrentIndex(3)
    def pg_records(self):
        self.lay1.setCurrentIndex(4)
    def backing(self):
        self.lay1.setCurrentIndex(1)
    def leave(self):
        exit()
    def log_out(self):
        self.user_input.setText("")
        self.pass_input.setText("")
        self.lay1.setCurrentIndex(0)
    def select_data_criminal(self):
        con = mdb.connect(host="localhost", user="root", passwd="drumStick_49", database="dbms_project")
        curs = con.cursor()
        criminal_name = self.crim_name1.text()
        print("c" +criminal_name)
        criminal_age_lessthan = self.crim_age_less_than.text()
        criminal_age_morethan = self.crim_age_greater_than.text()
        criminal_crime = self.crim_crime.currentText()
        print(criminal_crime)
        if criminal_name != "" and criminal_age_lessthan == "" and criminal_age_morethan == "" and criminal_crime == "":
            print("hello")
            q = f"select * from criminal where c_name like '%{criminal_name}%'"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                print(rows)
                ele = result[0]
                columns = len(ele)
                print(columns)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(["C_ID", "Criminal","Age","Crime Committed","Arrest Date","Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k,l,QTableWidgetItem(str(tup[l])))
                        self.lst1.setColumnWidth(3, 700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)


        elif criminal_name == "" and criminal_age_lessthan != "" and criminal_age_morethan == "" and criminal_crime == "":
            q = f"select * from criminal where c_age <= '{criminal_age_lessthan}'"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                ele = result[0]
                columns = len(ele)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(["C_ID", "Criminal","Age","Crime Committed","Arrest Date","Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k, l, QTableWidgetItem(str(tup[l])))
                self.lst1.setColumnWidth(3,700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)

        elif criminal_name == "" and criminal_age_lessthan == "" and criminal_age_morethan != "" and criminal_crime == "":
            q = f"select * from criminal where c_age >= '{criminal_age_morethan}'"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                ele = result[0]
                columns = len(ele)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(["C_ID", "Criminal","Age","Crime Committed","Arrest Date","Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k, l, QTableWidgetItem(str(tup[l])))
                self.lst1.setColumnWidth(3, 700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)
        elif criminal_name != "" and criminal_age_lessthan != "" and criminal_age_morethan == "" and criminal_crime == "":
            q = f"select * from criminal where c_age <= '{criminal_age_lessthan}' and c_name like '%{criminal_name}%'"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                ele = result[0]
                columns = len(ele)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(["C_ID", "Criminal","Age","Crime Committed","Arrest Date","Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k, l, QTableWidgetItem(str(tup[l])))
                self.lst1.setColumnWidth(3, 700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)

        elif criminal_name == "" and criminal_age_lessthan != "" and criminal_age_morethan != "" and criminal_crime == "":
            q = f"select * from criminal where c_age >= '{criminal_age_morethan}' and c_age <= '{criminal_age_lessthan}'"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                ele = result[0]
                columns = len(ele)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(["C_ID", "Criminal","Age","Crime Committed","Arrest Date","Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k, l, QTableWidgetItem(str(tup[l])))
                self.lst1.setColumnWidth(3,700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)

        elif criminal_name != "" and criminal_age_lessthan != "" and criminal_age_morethan != "" and criminal_crime == "":
            q = f"select * from criminal where c_age >= '{criminal_age_morethan}' and c_age <= '{criminal_age_lessthan}' and c_name like '%{criminal_name}%'"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                ele = result[0]
                columns = len(ele)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(["C_ID", "Criminal","Age","Crime Committed","Arrest Date","Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k, l, QTableWidgetItem(str(tup[l])))
                self.lst1.setColumnWidth(3,700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)

        elif criminal_name == "" and criminal_age_lessthan != "" and criminal_age_morethan != "" and criminal_crime != "":
            q = f"select * from criminal where c_age >= '{criminal_age_morethan}' and c_age <= '{criminal_age_lessthan}' and crime_committed like '%{criminal_crime}%'"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                ele = result[0]
                columns = len(ele)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(["C_ID", "Criminal","Age","Crime Committed","Arrest Date","Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k, l, QTableWidgetItem(str(tup[l])))
                self.lst1.setColumnWidth(3,700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)

        elif criminal_name == "" and criminal_age_lessthan == "" and criminal_age_morethan == "" and criminal_crime != "":
            q = f"select * from criminal where crime_committed like '%{criminal_crime}%'"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                ele = result[0]
                columns = len(ele)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(["C_ID", "Criminal","Age","Crime Committed","Arrest Date","Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k, l, QTableWidgetItem(str(tup[l])))
                self.lst1.setColumnWidth(3,700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)

        elif criminal_name == "" and criminal_age_lessthan == "" and criminal_age_morethan == "" and criminal_crime == "":
            q = f"select * from criminal"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                ele = result[0]
                columns = len(ele)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(["C_ID", "Criminal","Age","Crime Committed","Arrest Date","Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k, l, QTableWidgetItem(str(tup[l])))
                self.lst1.setColumnWidth(3,700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)

        elif criminal_name != "" and criminal_age_lessthan != "" and criminal_age_morethan != "" and criminal_crime != "":
            q = f"select * from criminal where c_age >= '{criminal_age_morethan}' and c_age <= '{criminal_age_lessthan}' and crime_committed like '%{criminal_crime}%' and c_name like '%{criminal_name}%'"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            if result != []:
                rows = len(result)
                ele = result[0]
                columns = len(ele)
                self.lst1.setRowCount(rows)
                self.lst1.setColumnCount(columns)
                self.lst1.setHorizontalHeaderLabels(
                    ["C_ID", "Criminal", "Age", "Crime Committed", "Arrest Date", "Bail Date"])
                for k in range(rows):
                    for l in range(columns):
                        tup = result[k]
                        self.lst1.setItem(k, l, QTableWidgetItem(str(tup[l])))
                self.lst1.setColumnWidth(3, 700)
            else:
                self.lst1.clear()
                self.lst1.setRowCount(0)

            con.commit()
            con.close()
    def select_data_criminal_trial(self):
        con = mdb.connect(host="localhost", user="root", passwd="drumStick_49", database="dbms_project")
        curs = con.cursor()
        criminal_name1 = self.crim_name2.text()
        judge_nam = self.judge_name.text()
        lawyer_nam = self.lawyer_name.text()
        trial_date = self.tri_date.text()

        if criminal_name1 == "" and judge_nam == "" and lawyer_nam == "" and trial_date == "":
            q = f"select ct.c_id,c_name as Criminal,ct.j_id,j_name as Judge,ct.l_id ,l_name Lawyer,Trial_Date from criminal_trial as ct,criminal as c,judge as j,lawyer as l where ct.c_id = c.c_id and ct.j_id = j.j_id and ct.l_id = l.l_id;"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            print("result"+str(rows))
            ele = result[0]
            columns = len(ele)
            print(columns)
            self.lst2.setRowCount(rows)
            self.lst2.setColumnCount(columns)
            #self.lst.setHorizontalHeaderLabels(["C_ID", "Criminal", "J_ID","Judge","L_ID","Lawyer","Trial_Date"])
            for m in range(rows):
                for n in range(columns):
                    tup = result[m]
                    self.lst2.setItem(m,n,QTableWidgetItem(str(tup[n])))
        elif criminal_name1 != "" and judge_nam == "" and lawyer_nam == "" and trial_date == "":
            q = f"select ct.c_id,c_name as Criminal,ct.j_id,j_name as Judge,ct.l_id ,l_name Lawyer,Trial_Date from criminal_trial as ct,criminal as c,judge as j,lawyer as l where ct.c_id = c.c_id and ct.j_id = j.j_id and ct.l_id = l.l_id and c_name like '%{criminal_name1}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            ele = result[0]
            columns = len(ele)
            self.lst2.setRowCount(rows)
            self.lst2.setColumnCount(columns)
            self.lst2.setHorizontalHeaderLabels(["C_ID", "Criminal", "J_ID", "Judge", "L_ID", "Lawyer", "Trial_Date"])
            for k in range(rows):
                for l in range(columns):
                    tup = result[k]
                    self.lst2.setItem(k, l, QTableWidgetItem(str(tup[l])))
        elif criminal_name1 == "" and judge_nam != "" and lawyer_nam == "" and trial_date == "":
            q = f"select ct.c_id,c_name as Criminal,ct.j_id,j_name as Judge,ct.l_id ,l_name Lawyer,Trial_Date from criminal_trial as ct,criminal as c,judge as j,lawyer as l where ct.c_id = c.c_id and ct.j_id = j.j_id and ct.l_id = l.l_id and j_name like '%{judge_nam}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            ele = result[0]
            columns = len(ele)
            self.lst2.setRowCount(rows)
            self.lst2.setColumnCount(columns)
            self.lst2.setHorizontalHeaderLabels(["C_ID", "Criminal", "J_ID", "Judge", "L_ID", "Lawyer", "Trial_Date"])
            for k in range(rows):
                for l in range(columns):
                    tup = result[k]
                    self.lst2.setItem(k, l, QTableWidgetItem(str(tup[l])))
        elif criminal_name1 == "" and judge_nam == "" and lawyer_nam != "" and trial_date == "":
            q = f"select ct.c_id,c_name as Criminal,ct.j_id,j_name as Judge,ct.l_id ,l_name Lawyer,Trial_Date from criminal_trial as ct,criminal as c,judge as j,lawyer as l where ct.c_id = c.c_id and ct.j_id = j.j_id and ct.l_id = l.l_id and l_name like '%{lawyer_nam}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            ele = result[0]
            columns = len(ele)
            self.lst2.setRowCount(rows)
            self.lst2.setColumnCount(columns)
            self.lst2.setHorizontalHeaderLabels(["C_ID", "Criminal", "J_ID", "Judge", "L_ID", "Lawyer", "Trial_Date"])
            for k in range(rows):
                for l in range(columns):
                    tup = result[k]
                    self.lst2.setItem(k, l, QTableWidgetItem(str(tup[l])))

        elif criminal_name1 == "" and judge_nam == "" and lawyer_nam == "" and trial_date != "":
            q = f"select ct.c_id,c_name as Criminal,ct.j_id,j_name as Judge,ct.l_id ,l_name Lawyer,Trial_Date from criminal_trial as ct,criminal as c,judge as j,lawyer as l where ct.c_id = c.c_id and ct.j_id = j.j_id and ct.l_id = l.l_id and trial_date like '%{trial_date}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            ele = result[0]
            columns = len(ele)
            self.lst2.setRowCount(rows)
            self.lst2.setColumnCount(columns)
            self.lst2.setHorizontalHeaderLabels(["C_ID", "Criminal", "J_ID", "Judge", "L_ID", "Lawyer", "Trial_Date"])
            for k in range(rows):
                for l in range(columns):
                    tup = result[k]
                    self.lst2.setItem(k, l, QTableWidgetItem(str(tup[l])))

            con.commit()
            con.close()
    def select_data_records(self):
        con = mdb.connect(host="localhost", user="root", passwd="drumStick_49", database="dbms_project")
        curs = con.cursor()
        criminal_name2 = self.crim_name3.text()
        judge_nam1 = self.judge_name1.text()
        lawyer_nam1 = self.lawyer_name1.text()

        if criminal_name2 == "" and judge_nam1 == "" and lawyer_nam1 == "":
            q = f"select case_id,cc.c_id,c_name,cc.j_id,j_name,cc.o_id,o_name,cc.l_id,l_name,verdict from case_court as cc,criminal as c,judge as j,lawyer as l,officer as o where cc.c_id = c.c_id and cc.j_id = j.j_id and cc.l_id = l.l_id and cc.o_id = o.o_id;"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            print("result" + str(rows))
            ele = result[0]
            columns = len(ele)
            print(columns)
            self.lst3.setRowCount(rows)
            self.lst3.setColumnCount(columns)
            self.lst3.setHorizontalHeaderLabels(["Case_ID","C_ID","Criminal", "J_ID","Judge","O_ID","Officer","L_ID","Lawyer","Verdict"])

            for m in range(rows):
                for n in range(columns):
                    tup = result[m]

                    self.lst3.setItem(m, n, QTableWidgetItem(str(tup[n])))
            self.lst3.setColumnWidth(9,1000)


        elif criminal_name2 != "" and judge_nam1 == "" and lawyer_nam1 == "":
            q = f"select case_id,cc.c_id,c_name,cc.j_id,j_name,cc.o_id,o_name,cc.l_id,l_name,verdict from case_court as cc,criminal as c,judge as j,lawyer as l,officer as o where cc.c_id = c.c_id and cc.j_id = j.j_id and cc.l_id = l.l_id and cc.o_id = o.o_id and c_name like '%{criminal_name2}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            print("result" + str(rows))
            ele = result[0]
            columns = len(ele)
            print(columns)
            self.lst3.setRowCount(rows)
            self.lst3.setColumnCount(columns)
            self.lst3.setHorizontalHeaderLabels(["Case_ID", "C_ID", "Criminal", "J_ID", "Judge", "O_ID", "Officer", "L_ID", "Lawyer", "Verdict"])
            for m in range(rows):
                for n in range(columns):
                    tup = result[m]
                    self.lst3.setItem(m, n, QTableWidgetItem(str(tup[n])))
            self.lst3.setColumnWidth(9,1000)

        elif criminal_name2 == "" and judge_nam1 != "" and lawyer_nam1 == "":
            q = f"select case_id,cc.c_id,c_name,cc.j_id,j_name,cc.o_id,o_name,cc.l_id,l_name,verdict from case_court as cc,criminal as c,judge as j,lawyer as l,officer as o where cc.c_id = c.c_id and cc.j_id = j.j_id and cc.l_id = l.l_id and cc.o_id = o.o_id and j_name like '%{judge_nam1}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            print("result" + str(rows))
            ele = result[0]
            columns = len(ele)
            print(columns)
            self.lst3.setRowCount(rows)
            self.lst3.setColumnCount(columns)
            self.lst3.setHorizontalHeaderLabels(["Case_ID", "C_ID", "Criminal", "J_ID", "Judge", "O_ID", "Officer", "L_ID", "Lawyer", "Verdict"])
            for m in range(rows):
                for n in range(columns):
                    tup = result[m]
                    self.lst3.setItem(m, n, QTableWidgetItem(str(tup[n])))
            self.lst3.setColumnWidth(9,1000)

        elif criminal_name2 == "" and judge_nam1 == "" and lawyer_nam1 != "":
            q = f"select case_id,cc.c_id,c_name,cc.j_id,j_name,cc.o_id,o_name,cc.l_id,l_name,verdict from case_court as cc,criminal as c,judge as j,lawyer as l,officer as o where cc.c_id = c.c_id and cc.j_id = j.j_id and cc.l_id = l.l_id and cc.o_id = o.o_id and l_name like '%{lawyer_nam1}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            print("result" + str(rows))
            ele = result[0]
            columns = len(ele)
            print(columns)
            self.lst3.setRowCount(rows)
            self.lst3.setColumnCount(columns)
            self.lst3.setHorizontalHeaderLabels(["Case_ID", "C_ID", "Criminal", "J_ID", "Judge", "O_ID", "Officer", "L_ID", "Lawyer", "Verdict"])
            for m in range(rows):
                for n in range(columns):
                    tup = result[m]
                    self.lst3.setItem(m, n, QTableWidgetItem(str(tup[n])))
        elif criminal_name2 == "" and judge_nam1 != "" and lawyer_nam1 != "":
            q = f"select case_id,cc.c_id,c_name,cc.j_id,j_name,cc.o_id,o_name,cc.l_id,l_name,verdict from case_court as cc,criminal as c,judge as j,lawyer as l,officer as o where cc.c_id = c.c_id and cc.j_id = j.j_id and cc.l_id = l.l_id and cc.o_id = o.o_id and l_name like '%{lawyer_nam1}%' and j_name like '%{judge_nam1}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            print("result" + str(rows))
            ele = result[0]
            columns = len(ele)
            print(columns)
            self.lst3.setRowCount(rows)
            self.lst3.setColumnCount(columns)
            self.lst3.setHorizontalHeaderLabels(["Case_ID", "C_ID", "Criminal", "J_ID", "Judge", "O_ID", "Officer", "L_ID", "Lawyer", "Verdict"])
            for m in range(rows):
                for n in range(columns):
                    tup = result[m]
                    self.lst3.setItem(m, n, QTableWidgetItem(str(tup[n])))
            self.lst3.setColumnWidth(9,1000)

        elif criminal_name2 != "" and judge_nam1 != "" and lawyer_nam1 == "":
            q = f"select case_id,cc.c_id,c_name,cc.j_id,j_name,cc.o_id,o_name,cc.l_id,l_name,verdict from case_court as cc,criminal as c,judge as j,lawyer as l,officer as o where cc.c_id = c.c_id and cc.j_id = j.j_id and cc.l_id = l.l_id and cc.o_id = o.o_id and j_name like '%{judge_nam1}%' and c_name like '%{criminal_name2}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            print("result" + str(rows))
            ele = result[0]
            columns = len(ele)
            print(columns)
            self.lst3.setRowCount(rows)
            self.lst3.setColumnCount(columns)
            self.lst3.setHorizontalHeaderLabels(["Case_ID", "C_ID", "Criminal", "J_ID", "Judge", "O_ID", "Officer", "L_ID", "Lawyer", "Verdict"])
            for m in range(rows):
                for n in range(columns):
                    tup = result[m]
                    self.lst3.setItem(m, n, QTableWidgetItem(str(tup[n])))
            self.lst3.setColumnWidth(9,1000)

        elif criminal_name2 != "" and judge_nam1 == "" and lawyer_nam1 != "":
            q = f"select case_id,cc.c_id,c_name,cc.j_id,j_name,cc.o_id,o_name,cc.l_id,l_name,verdict from case_court as cc,criminal as c,judge as j,lawyer as l,officer as o where cc.c_id = c.c_id and cc.j_id = j.j_id and cc.l_id = l.l_id and cc.o_id = o.o_id and l_name like '%{lawyer_nam1}%' and c_name like '%{criminal_name2}%';"
            curs.execute(q)
            result = curs.fetchall()
            print(result)
            rows = len(result)
            print("result" + str(rows))
            ele = result[0]
            columns = len(ele)
            print(columns)
            self.lst3.setRowCount(rows)
            self.lst3.setColumnCount(columns)
            # self.lst.setHorizontalHeaderLabels(["C_ID", "Criminal", "J_ID","Judge","L_ID","Lawyer","Trial_Date"])
            for m in range(rows):
                for n in range(columns):
                    tup = result[m]
                    self.lst3.setItem(m, n, QTableWidgetItem(str(tup[n])))
            self.lst3.setColumnWidth(9,1000)

    def logi(self):
        con = mdb.connect(host="localhost", user="root", passwd="drumStick_49", database="dbms_project")
        curs = con.cursor()
        user = self.user_input.text()
        passwd = self.pass_input.text()
        print(user)
        print(passwd)
        if user == "" and passwd == "":
            self.stat.setText("Enter Credentials")
            self.user_input.setText("")
            self.pass_input.setText("")
        elif user != "" and passwd == "":
            self.stat.setText("Enter Password")
            self.stat.setHidden(False)

        elif user == "" and passwd != "":
            self.stat.setText("Enter Username")
        elif user != "" and passwd != "":
            q = f"select exists(select username from users  where username = '{user}')"
            curs.execute(q)
            res3 = curs.fetchall()
            print(res3)
            tup1 = res3[0]
            des = tup1[0]
            if des != 0:
                q = f"select password from users where username = '{user}'"
                curs.execute(q)
                res4 = curs.fetchall()
                tup1 = res4[0]
                right_pass = tup1[0]
                print(right_pass)
                if passwd == right_pass:
                    self.lay1.setCurrentIndex(1)
            else:
                self.stat.setText("Invalid User")
                self.stat.setHidden(False)
                self.user_input.setText("")
                self.pass_input.setText("")
app = QApplication(sys.argv)
UIWindow = mainwindow()
app.exec_()