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
                sh '/var/jenkins_home/workspace/dqe_pytest_pipeline/demo_run.sh'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}