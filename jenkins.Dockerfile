FROM jenkins/jenkins

USER root
RUN apt-get update
RUN apt-get install docker.io vim wget -y

USER jenkins