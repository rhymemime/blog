pipeline {
    agent any

    stages {
        stage('Build') { 
            steps {
                echo 'Building' 
                sh 'touch ./tmpfile'
                git 'https://github.com/rhymemime/blog.git'
                sh """
                python3 -m virtualenv venv
                . ./venv/bin/activate
                pip install wheel
                ls
                pwd
                python setup.py bdist_wheel
                ls ./dist
                sudo /bin/cp /var/lib/jenkins/workspace/personal-site-build/dist/flaskr-1.0.0-py3-none-any.whl /home/site-manager/personalSite/
                deactivate
                sudo su - site-manager <<HERE
                cd
                whoami
                ls
                cd ./personalSite
                . ./venv/bin/activate
                pip install --upgrade --force-reinstall /home/site-manager/flaskr-1.0.0-py3-none-any.whl
                sudo systemctl restart personalsite
                HERE
                echo 'finishing!'
                """
            }
        }
    }
}