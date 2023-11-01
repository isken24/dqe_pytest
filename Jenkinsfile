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
                sh "apt-get install pip"
                sh "pip install python"
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "${env.WORKSPACE}/demo_run.sh"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}