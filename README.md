Before you start:
	
	Project is based on Python and Allure reporting tool. 
	Make sure to install Python and Allure on your machine before running project.
	Python: https://www.python.org/downloads/
	Allure: https://github.com/allure-framework

	Open Terminal window and navigate to project directory using following command:
		cd <path_to_project_directory>
		
	Install required packages:
		pip install -r requirements.txt
		
	Update connection details in "variables.py":
		SERVER = <your-server-location>
		DATABASE = <your-db-name>
		USERNAME = <your-db-username>
		PASSWORD = <your-db-password>
		DRIVER = <your-odbc-driver> 	#e.g.: 'ODBC Driver 17 for SQL Server'


How to run tests:

	You can run individual test suits using following command:
		pytest <path-to-test-suit>
	Make sure to specify path to test.py file you want to run.
	
	To run all tests you need to use path to 'tests' directory and following command:
		pytest .\tests
	

Generating Allure Reports:

	To generate Allure reports for your test results, follow these commands:

	Generate the initial Allure report data:

		pytest .\tests --alluredir=allure-report


	Serve the Allure report:

		allure serve allure-report
  end
