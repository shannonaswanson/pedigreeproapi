# check if the Docker daemon is running
if ! docker info > /dev/null 2>&1; then
  echo "Docker daemon is not running. Please start Docker and try again."
  exit 1
fi

# Check if the image already exists and if it does delete it first
if docker image inspect pedigreeproapi:dev > /dev/null 2>&1; then
  docker rmi -f pedigreeproapi:dev

  # docker builder prune --all --force
  # docker image prune --all --force
  # docker volume prune --all --force
  # docker network prune --all --force
  # # Remove any stopped containers
  # docker container prune --force
fi

docker build -t pedigreeproapi:dev .