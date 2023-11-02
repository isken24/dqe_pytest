pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Demo run') {
            steps {
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "pip install -r /my_app/requirements.txt"
                sh "./demo_run.sh"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}