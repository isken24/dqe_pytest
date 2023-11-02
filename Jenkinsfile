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
                sh "apt install -y python3-pytest"
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