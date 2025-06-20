pipeline {
  agent any

  environment {
    VENV = 'venv'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        sh 'python3 -m venv $VENV'
        sh '. $VENV/bin/activate && pip install --upgrade pip'
        sh '. $VENV/bin/activate && pip install -r requirements.txt'
      }
    }

    stage('Unit Tests') {
      steps {
        sh '. $VENV/bin/activate && pytest tests/unit --junitxml=report-unit.xml'
        junit 'report-unit.xml'
      }
    }

    stage('Start Flask App') {
      steps {
        // Démarrage de l’application en arrière-plan
        sh '. $VENV/bin/activate && nohup flask run --port 5000 &'
        sh 'sleep 5'
      }
    }

    stage('Functional Tests') {
      steps {
        sh '. $VENV/bin/activate && pytest tests/functional --junitxml=report-func.xml'
        junit 'report-func.xml'
      }
    }
  }

  post {
    success {
      echo 'Pipeline terminé avec succès !'
    }
    failure {
      mail to: 'equipe@example.com',
           subject: "Échec pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER}",
           body: "Consultez les logs Jenkins pour plus de détails."
    }
  }
}
