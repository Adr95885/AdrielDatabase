pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install flask'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m unittest discover tests -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t task-app .'
            }
        }

        stage('Deploy to Staging') {
            steps {
                bat 'docker run -d -p 5001:5000 task-app'
            }
        }

        stage('Manual Approval') {
            steps {
                input message: 'Deploy to production?'
            }
        }

        stage('Deploy to Production') {
            steps {
                bat 'docker run -d -p 5000:5000 task-app'
            }
        }
    }
}
