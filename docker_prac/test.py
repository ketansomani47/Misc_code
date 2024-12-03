export DB_USER=root
export DB_PASSWORD=Password@123
export DB_NAME=nagp_flask
export DB_HOST=localhost

docker run -p 80:2000 ketansomani/nagp_flask --env DB_USER=$DB_SUER --env DB_PASSWORD=$DB_PASSWORD --env DB_HOST=$DB_HOST --env DB_NAME=$DB_NAME

docker run -e DB_USER=root -e DB_PASSWORD=Password@123 -e DB_HOST=localhost -e DB_NAME=nagp_flask -p 80:2000 ketansomani/nagp_flask