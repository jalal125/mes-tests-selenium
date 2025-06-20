// Jenkinsfile (adapté pour Windows et Sysnative)
pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Setup Python') {
      steps {
        bat """
        set "SYSNATIVE=%SystemRoot%\\Sysnative"
        "%SYSNATIVE%\\cmd.exe" /c python -m venv venv
        "%SYSNATIVE%\\cmd.exe" /c venv\\Scripts\\python.exe -m pip install --upgrade pip
        "%SYSNATIVE%\\cmd.exe" /c venv\\Scripts\\python.exe -m pip install -r requirements.txt
        """
      }
    }
    stage('Unit Tests') {
      steps {
        bat """
        set "SYSNATIVE=%SystemRoot%\\Sysnative"
        "%SYSNATIVE%\\cmd.exe" /c venv\\Scripts\\python.exe -m pytest tests/unit -q --junitxml=unit-results.xml
        """
      }
      post {
        always {
          junit 'unit-results.xml'
        }
      }
    }
    stage('Start Flask App') {
      steps {
        bat """
        set "SYSNATIVE=%SystemRoot%\\Sysnative"
        start /B "%SYSNATIVE%\\cmd.exe" /c venv\\Scripts\\python.exe -m flask --app app run --port 5000
        """
        sleep 5
      }
    }
    stage('Functional Tests') {
      steps {
        bat """
        set "SYSNATIVE=%SystemRoot%\\Sysnative"
        "%SYSNATIVE%\\cmd.exe" /c venv\\Scripts\\python.exe -m pytest tests/functional -q --junitxml=functional-results.xml
        """
      }
      post {
        always {
          junit 'functional-results.xml'
        }
      }
    }
  }

  post {
    success {
      echo 'Build terminé avec succès !'
    }
    failure {
      echo 'Build échoué – voir console pour détails.'
    }
  }
}
