# camino financial take home test

 Build:  
 `docker-compose build`  
 Start docker instance:  
 `docker-compose up -d`  
 Shut down:  
 `docker-compose down`  
 Run Unit Tests:  
 `docker-compose run web python manage.py test`  

 #Note:  
 #May need to run docker-compose up twice, as the database is often not ready by the time the django instance is running
