pipeline {
agent any
stages {
	stage('Build') {
	parallel {
		stage('Build') {
		steps {
			sh 'echo "building the repo"'
		}
		}
	}
	}

	stage('Install dependencies') {
	steps {
		sh 'python3 -m venv venv'
		sh 'source venv/bin/activate && pip install -r requirements.txt'
	}
	}

	stage('Test') {
	steps {
	    sh 'source venv/bin/activate && pytest'
	}
	}

	stage('Run app')
	{
	steps {
		echo "deploying the application"
		sh 'source venv/bin/activate && python main.py'
	}
	}
}

post {
		always {
			echo 'The pipeline completed'
		}
		success {
			echo "Flask Application Up and running!!"
		}
		failure {
			echo 'Build stage failed'
			error('Stopping early…')
		}
	}
}
