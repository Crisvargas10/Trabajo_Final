pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'develop', url: 'https://github.com/Crisvargas10/Trabajo_Final.git'
            }
        }

        stage('Ejecutar Transform') {
            steps {
                sh 'python transform.py'
            }
        }

        // stage('Ejecutar Transform') {
        //     steps {
        //         sh 'python transform.py'
        //     }
        // }

        // stage('Ejecutar Lectura') {
        //     steps {
        //         sh 'python lectura.py'
        //     }
        // }
    }
}
