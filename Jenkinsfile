pipeline {
  agent any

  environment {
    AWS_ACCOUNT_ID="112255298705" // AWS 계정의 12자리 ID
    AWS_DEFAULT_REGION="ap-northeast-2a" // 서비스의 리전 코드
    IMAGE_REPO_NAME="kpet-repo" // ECR에 존재하는 레포지토리 이름
    IMAGE_TAG="latest"
    REPOSITORY_URI="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
    AWS_CREDENTIALS = "{aws_cre_id}" // Jenkins에서 지정한 아마존 자격증명 ID
    GIT_CREDENTIAL_ID = "{git_cre_id}" // Jenkins에서 지정한 깃허브 자격증명 ID
    DEPLOY_ACCOUNT = "deploy_user" // IAM에서 생성한 유저명
    DEPLOY_ROLE = "arn:aws:iam::112255298705:user/deploy_user" // IAM에서 생성한 역할의 arn id
    //CLUSTER_NAME = '{ECS Cluster Name}' // ECS 클러스터 이름
    //SERVICE_NAME = '{ECS Service Name}' // 클러스터내 서비스 이름
    BRANCH = 'master' // 깃허브 브런치
    GIT_URL = 'https://github.com/Nagony213/Test01.git' // 깃허브 레포지토리 주소
  }

  stages {
    stage('AWS ECR Login'){
      steps {
        withAWS(credentials: "${AWS_CREDENTIALS}", role: "${DEPLOY_ROLE}", roleAccount: "${DEPLOY_ACCOUNT}", externalId: 'externalId'){
          sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
        }
      }
    }

    stage ('Git Clone'){ 
      steps { 
        git branch: BRANCH, 
        credentialsId: GIT_CREDENTIAL_ID, 
        url: GIT_URL
       } 
    }

    stage('Docker Build') {
      steps {
        script { sh "docker build -t ${IMAGE_REPO_NAME}:${IMAGE_TAG} ." }
      }
    }

    stage ('ECR Push') {
      steps {
        script {
          sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}"
          sh "docker push ${REPOSITORY_URI}"
        }
      }
    }

    stage('Clean docker image') {
      steps{
        sh "docker rmi -f ${IMAGE_REPO_NAME} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
      }
    }
    
    stage ('ECS Deploy') {
      steps {
        script {
          withAWS(credentials: "${AWS_CREDENTIALS}", role: "${DEPLOY_ROLE}", roleAccount: "${DEPLOY_ACCOUNT}", externalId: 'externalId'){
            sh "aws ecs update-service --region ${AWS_DEFAULT_REGION} --cluster ${CLUSTER_NAME} --service ${SERVICE_NAME} --force-new-deployment"
          }
        }
      }        
    }
    
  }
}
