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
		input(id: "Deploy Gate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
	}
	}

	stage('Run app')
	{
	steps {
		echo "deploying the application"
		sh 'source venv/bin/activate && python main.py > log.txt 2>&1 &'
	}
	}
}

post {
		always {
			echo 'The pipeline completed'
			junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
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
