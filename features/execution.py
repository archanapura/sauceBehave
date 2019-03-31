import subprocess

subprocess.Popen(
            'behave -f allure_behave.formatter:AllureFormatter -o reports ',shell=False)