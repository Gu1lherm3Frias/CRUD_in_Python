import mysql.connector

DB_NAME = "employees"

TABLES = {}

TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    " `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    " `birth_date` date NOT NULL,"
    " `first_name` varchar(16) NOT NULL,"
    " `last_name` varchar(16) NOT NULL,"
    " `gender` enum('M','F') NOT NULL,"
    " `hire_date` date NOT NULL,"
    " PRIMARY KEY(`emp_no`)"
    ") ENGINE=InnoDB"
)

TABLES['departments'] = (
    "CREATE TABLE `departments` ("
    " `dept_no` char(4) NOT NULL,"
    " `dept_name` varchar(40) NOT NULL,"
    " PRIMARY KEY(`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
    ") ENGINE=InnoDB"
)

TABLES['salaries'] = (
    "CREATE TABLE `salaries` ("
    " `emp_no` int(11) NOT NULL,"
    " `salary` int(11) NOT NULL,"
    " `from_date` date NOT NULL"
)
def main():
    cnx = mysql.connector.connect(user='scott', password='password', host='127.0.0.1', database='employes')
    cnx.close()


if __name__ == "__main__":
    main()