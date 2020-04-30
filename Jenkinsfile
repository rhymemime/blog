pipeline {
    agent any

    stages {
        stage('Build') { 
            steps {
                echo 'Spinning up Jankins, like Jenkins but janky'
                echo 'Building' 
                git 'https://github.com/rhymemime/blog.git'
                echo 'Starting shell script that actually does all the work'
                sh """
                python3 -m virtualenv venv
                . ./venv/bin/activate
                pip install wheel
                python setup.py bdist_wheel
                sudo /bin/cp /var/lib/jenkins/workspace/personal-site-build/dist/flaskr-1.0.0-py3-none-any.whl /home/site-manager/personalSite/
                deactivate
                sudo su - site-manager <<HERE
                cd ./personalSite
                . ./venv/bin/activate
                pip install --upgrade --force-reinstall /home/site-manager/personalSite/flaskr-1.0.0-py3-none-any.whl
                sudo systemctl restart personalsite
                HERE
                """
                echo 'If this were Jenkins, we would do some testing, but it\'s not, so bye from Jankins'
            }
        }
    }
}