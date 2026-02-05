pipeline {
    agent any
    
    environment {
        dockerhubUser = 'tupeshg' 
        appName       = 'furnitureapp'
        imagetag      = "${BUILD_NUMBER}"
        imageName     = "${dockerhubUser}/${appName}:${imagetag}"
    }
    options {
        // Timeout counter starts AFTER agent is allocated
        timeout(time: 1, unit: 'SECONDS')
    }
    stages { 
        stage('Build Docker Image') {
            steps {
                echo "Creating Docker Image..."
                sh "docker build -t ${imageName} ."
            }
        }

        stage('Trivy Security Scan') {
            steps {
                echo "Scanning Image for Vulnerabilities..."
                //sh "trivy image ${imageName}"
            }
        }

        stage('Image Push') {
	      steps {
        	script {
          	   docker.withRegistry('', 'dockercred') {
  		   docker.image("${imageName}").push()
  		   docker.image("${imageName}").push('latest')

	 }
        }
      }
    }

}
}