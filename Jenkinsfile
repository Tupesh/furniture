pipeline {    
    agent any
    environment {
        dockerhubUser = 'tupeshg' 
        appName       = 'furnitureapp'
        imagetag      = "${BUILD_NUMBER}"
        imageName     = "${dockerhubUser}/${appName}:${imagetag}"
        devIp         = '192.168.56.22'
    }

    stages { 
        stage('Build Docker Image') {
            agent {
                node {
                    label 'docker-trivy-machine'
                }
            }
            steps {
                echo "Creating Docker Image..."
                sh "docker build -t ${imageName} ."
            }
        }

        stage('Trivy Security Scan') {
            agent {
                node {
                    label 'docker-trivy-machine'
                }
            }
            steps {
                echo "Scanning Image for Vulnerabilities..."
                sh "trivy image ${imageName}"
            }
        }

        stage('Image Push') {
            agent {
                node {
                    label 'docker-trivy-machine'
                }
            }
	      steps {
        	script {
          	   docker.withRegistry('', 'dockercred') {
  		   docker.image("${imageName}").push()
  		   docker.image("${imageName}").push('latest')

	 }
        }
      }
    }
    stage("Deploy to dev") {
        agent {
            node {
                label 'dev-prod-manger'
            }
        }
        steps {
            echo "Deploying to Dev Environment..."
            sh '''
            ansible-playbook ansibleconfigs/playbook.yml \
            -e "imageName=$dockerhubUser/$appName" \
            -e "tagName=$imagetag" \
            -e "hostEnv=devserver"
             '''
            }
        post {
            success {
                echo "Application deployed successfully to Dev Environment!"
                echo "Check at http://${devIp}:8000"
            }
            failure {
                echo "Deployment to Dev Environment failed."
            }

        }
    }

}
}