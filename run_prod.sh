docker-compose -f docker-compose.base.yml -f docker-compose.prod.yml kill
docker-compose -f docker-compose.base.yml -f docker-compose.prod.yml build
docker-compose -f docker-compose.base.yml -f docker-compose.prod.yml up