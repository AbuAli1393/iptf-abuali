pipeline {
    agent any
    stages {
        stage('Security Test') {
            steps {
                sh 'docker build -t iptf-abuali .'
                sh 'docker run iptf-abuali --target myapp.example.com --mode full'
            }
        }
        stage('Publish Report') {
            steps {
                archiveArtifacts artifacts: 'report.json', allowEmptyArchive: false
            }
        }
    }
}