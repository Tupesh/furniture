pipeline {    
    agent any
    environment {
        dockerhubUser = 'tupeshg' 
        appName       = 'furnitureapp'
        imagetag      = "${BUILD_NUMBER}"
        imageName     = "${dockerhubUser}/${appName}:${imagetag}"
        devIp         = '192.168.56.22'
        prodIp        = '192.168.56.23'
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
            ansible-playbook -i ansibleconfigs/inventory ansibleconfigs/playbook.yml -l dev \
            -e "imageName=$dockerhubUser/$appName" \
            -e "tagName=$imagetag"
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

      stage("Deploy to prod") {
        agent {
            node {
                label 'dev-prod-manger'
            }
        }
        steps {
            timeout(time:1, unit:'MINUTES'){
                 input message: 'Approve Production deployment?'
                 }
            echo "Deploying to prod Environment..."
            sh '''
            ansible-playbook -i ansibleconfigs/inventory ansibleconfigs/playbook.yml -l prod \
            -e "imageName=$dockerhubUser/$appName" \
            -e "tagName=$imagetag"
            '''
            }
        post {
            success {
                echo "Application deployed successfully to prod Environment!"
                echo "Check at http://${prodIp}:8000"
            }
            failure {
                echo "Deployment to prod Environment failed."
            }

        }
    }

}
}