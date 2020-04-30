pipeline {
    agent any

    stages {
        stage('Build') { 
            steps {
                echo 'Building' 
                sh 'touch ./tmpfile'
                git 'https://github.com/rhymemime/blog.git'
                sh """
                python -m virtualenv venv
                . ./venv/bin/activate
                pip install wheel
                ls
                pwd
                python setup.py bdist_wheel
                """
            }
        }
    }
}