pipeline {
  agent any

  stages {
    stage('Checkout SCM') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        // Crée un venv puis installe pip + dépendances
        powershell """
          python -m venv venv
          .\\venv\\Scripts\\python.exe -m pip install --upgrade pip
          .\\venv\\Scripts\\python.exe -m pip install -r requirements.txt
        """
      }
    }

    stage('Unit Tests') {
      steps {
        powershell """
          .\\venv\\Scripts\\python.exe -m pytest tests/unit -q --junitxml=unit-results.xml
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
        // Démarre le serveur Flask en arrière‐plan
        powershell """
          Start-Process -NoNewWindow -FilePath .\\venv\\Scripts\\python.exe -ArgumentList '-m flask --app app run --port 5000'
        """
        // Laisse le temps au serveur de démarrer
        sleep 5
      }
    }

    stage('Functional Tests') {
      steps {
        powershell """
          .\\venv\\Scripts\\python.exe -m pytest tests/functional -q --junitxml=functional-results.xml
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
      echo 'Build échoué – consultez la console pour les erreurs.'
    }
  }
}
