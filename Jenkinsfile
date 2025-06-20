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
        // Crée un virtualenv et installe les dépendances sous Windows
        bat """
        python -m venv venv
        venv\\Scripts\\Activate.bat
        pip install --upgrade pip
        pip install -r requirements.txt
        """
      }
    }

    stage('Unit Tests') {
      steps {
        bat """
        venv\\Scripts\\Activate.bat
        pytest tests/unit -q --junitxml=unit-results.xml
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
        // Lance le serveur Flask en tâche de fond
        bat """
        start /B venv\\Scripts\\Activate.bat && python -m flask --app app run --port 5000
        """
        sleep 5  // laisse le temps au serveur de démarrer
      }
    }

    stage('Functional Tests') {
      steps {
        bat """
        venv\\Scripts\\Activate.bat
        pytest tests/functional -q --junitxml=functional-results.xml
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
      echo 'Build échoué, voir logs pour diagnostic.'
    }
  }
}
