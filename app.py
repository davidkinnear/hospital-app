from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rocket_3101'  # Use your MySQL root password
app.config['MYSQL_DB'] = 'Hospital'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_patient', methods=['POST'])
def update_patient():
    patient_id = request.form['patient_id']
    phone = request.form['phone']
    cursor = mysql.connection.cursor()
    sql = "UPDATE patient SET customer_phone = %s WHERE patient_id = %s"
    cursor.execute(sql, (phone, patient_id))
    mysql.connection.commit()
    cursor.close()
    return 'Patient phone number updated successfully!'

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    doctor_id = request.form['doctor_id']
    doctor_name = request.form['doctor_name']
    doctor_specialization = request.form['doctor_specialization']
    department_id = request.form['department_id']  # New line to handle department ID
    cursor = mysql.connection.cursor()
    sql = "INSERT INTO doctor (doctor_id, doctor_name, doctor_specialization, department_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (doctor_id, doctor_name, doctor_specialization, department_id))
    mysql.connection.commit()
    cursor.close()
    return 'New doctor added successfully!'

@app.route('/add_patient', methods=['POST'])
def add_patient():
    patient_id = request.form['patient_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    address = request.form['address']
    gender = request.form['gender']
    phone = request.form['phone']

    cursor = mysql.connection.cursor()
    sql = """
    INSERT INTO patient (patient_id, customer_first_name, customer_last_name, customer_date, customer_address, customer_gender, customer_phone)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (patient_id, first_name, last_name, dob, address, gender, phone))
    mysql.connection.commit()
    cursor.close()

    return 'New patient added successfully!'


@app.route('/update_doctor', methods=['POST'])
def update_doctor():
    doctor_id = request.form['doctor_id']
    doctor_specialization = request.form['doctor_specialization']
    department_id = request.form['department_id']  # Assuming you want to allow updating this field
    cursor = mysql.connection.cursor()
    sql = "UPDATE doctor SET doctor_specialization = %s, department_id = %s WHERE doctor_id = %s"
    cursor.execute(sql, (doctor_specialization, department_id, doctor_id))
    mysql.connection.commit()
    cursor.close()
    return 'Doctor information updated successfully!'


@app.route('/add_register', methods=['POST'])
def add_register():
    register_id = request.form['register_id']
    arrival_time = request.form['arrival_time']
    patient_id = request.form['patient_id']
    medical_complaint = request.form['medical_complaint']
    assessment = request.form['assessment']
    treatment = request.form['treatment']
    follow_up = request.form['follow_up']
    cursor = mysql.connection.cursor()
    sql = """
    INSERT INTO register (register_id, arrival_time, patient_id, medical_complaint, assessment, treatment, follow_up)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (register_id, arrival_time, patient_id, medical_complaint, assessment, treatment, follow_up))
    mysql.connection.commit()
    cursor.close()
    return 'New register entry added successfully!'

@app.route('/update_register', methods=['POST'])
def update_register():
    register_id = request.form['register_id']
    treatment = request.form['treatment']
    follow_up = request.form['follow_up']
    cursor = mysql.connection.cursor()
    sql = "UPDATE register SET treatment = %s, follow_up = %s WHERE register_id = %s"
    cursor.execute(sql, (treatment, follow_up, register_id))
    mysql.connection.commit()
    cursor.close()
    return 'Register entry updated successfully!'

@app.route('/add_medical_record', methods=['POST'])
def add_medical_record():
    record_id = request.form['record_id']
    register_id = request.form['register_id']
    diagnosis = request.form['diagnosis']
    medication = request.form['medication']
    cursor = mysql.connection.cursor()
    sql = "INSERT INTO medical_record (record_id, register_id, diagnosis, medication) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (record_id, register_id, diagnosis, medication))
    mysql.connection.commit()
    cursor.close()
    return 'Medical record added successfully!'

@app.route('/update_medical_record', methods=['POST'])
def update_medical_record():
    record_id = request.form['record_id']
    diagnosis = request.form['diagnosis']
    medication = request.form['medication']
    cursor = mysql.connection.cursor()
    sql = "UPDATE medical_record SET diagnosis = %s, medication = %s WHERE record_id = %s"
    cursor.execute(sql, (diagnosis, medication, record_id))
    mysql.connection.commit()
    cursor.close()
    return 'Medical record updated successfully!'

@app.route('/display_patients')
def display_patients():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM patient")
    patients = cursor.fetchall()
    cursor.close()
    return render_template('display_patients.html', patients=patients)

@app.route('/display_doctors')
def display_doctors():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM doctor")
    doctors = cursor.fetchall()
    cursor.close()
    return render_template('display_doctors.html', doctors=doctors)

@app.route('/display_registers')
def display_registers():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM register")
    registers = cursor.fetchall()
    cursor.close()
    return render_template('display_registers.html', registers=registers)

@app.route('/display_departments')
def display_departments():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM department")
    departments = cursor.fetchall()
    cursor.close()
    return render_template('display_departments.html', departments=departments)

@app.route('/display_medical_records')
def display_medical_records():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM medical_record")
    medical_records = cursor.fetchall()
    cursor.close()
    return render_template('display_medical_records.html', medical_records=medical_records)

@app.route('/display_all_tables')
def display_all_tables():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM patient")
    patients = cursor.fetchall()
    cursor.execute("SELECT * FROM doctor")
    doctors = cursor.fetchall()
    cursor.execute("SELECT * FROM register")
    registers = cursor.fetchall()
    cursor.execute("SELECT * FROM department")
    departments = cursor.fetchall()
    cursor.execute("SELECT * FROM medical_record")
    medical_records = cursor.fetchall()
    cursor.close()
    return render_template('display_all_tables.html', patients=patients, doctors=doctors, registers=registers, departments=departments, medical_records=medical_records)


@app.route('/search_patient', methods=['GET'])
def search_patient():
    search_query = request.args.get('search_query')
    cursor = mysql.connection.cursor()

    # Attempt to treat the search query as an ID first, then as a name
    try:
        # Check if search_query can be converted to an integer (ID)
        patient_id = int(search_query)
        cursor.execute("SELECT * FROM patient WHERE patient_id = %s", (patient_id,))
    except ValueError:
        # Search by name if the query is not an integer
        cursor.execute("""
            SELECT * FROM patient 
            WHERE customer_first_name LIKE %s OR customer_last_name LIKE %s
        """, (f"%{search_query}%", f"%{search_query}%"))

    patient = cursor.fetchone()

    if patient:
        patient_id = patient[0]
        # Fetch register entries for the found patient
        cursor.execute("SELECT * FROM register WHERE patient_id = %s", (patient_id,))
        registers = cursor.fetchall()

        # Fetch medical records for each register entry
        medical_records = []
        for register in registers:
            cursor.execute("SELECT * FROM medical_record WHERE register_id = %s", (register[0],))
            records = cursor.fetchall()
            medical_records.extend(records)
        
        cursor.close()
        return render_template('search_results.html', patient=patient, registers=registers, medical_records=medical_records)
    else:
        cursor.close()
        return 'No patient found'

@app.route('/search_doctor', methods=['POST'])
def search_doctor():
    search_input = request.form['doctor_search']
    cursor = mysql.connection.cursor()
    # Check if input is numeric and prepare SQL accordingly
    if search_input.isdigit():
        sql = """
        SELECT doctor.doctor_id, doctor.doctor_name, doctor.doctor_specialization, department.dept_name, department.location
        FROM doctor
        JOIN department ON doctor.department_id = department.department_id
        WHERE doctor.doctor_id = %s
        """
    else:
        sql = """
        SELECT doctor.doctor_id, doctor.doctor_name, doctor.doctor_specialization, department.dept_name, department.location
        FROM doctor
        JOIN department ON doctor.department_id = department.department_id
        WHERE doctor.doctor_name LIKE %s
        """
        search_input = f"%{search_input}%"  # Use wildcard for partial matching

    cursor.execute(sql, (search_input,))
    doctor_data = cursor.fetchone()
    cursor.close()

    if doctor_data:
        return render_template('display_doctor_info.html', doctor=doctor_data)
    else:
        return 'No doctor found with provided information'




if __name__ == '__main__':
    app.run(debug=True)
