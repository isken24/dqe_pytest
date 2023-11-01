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