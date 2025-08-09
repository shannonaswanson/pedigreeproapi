docker run -p 5001:5001 -e MONGODB_URI="mongodb://localhost:27017/" pedigreeproapi:dev
curl http://localhost:5001/hello