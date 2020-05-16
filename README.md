# Docker Project for fast database generation
Quick database generator with docker


## About this Open Source Project
This open-source project is for you(community). Im using this for fast database development, you only need to add more classes for tables and think in your fake data or table relations. Also you could add this project in your development projects just adding the docker-composer.yml stack.



## How to build and run this project

* Install using Docker Compose [**Recommended Method**] 
    * Clone this repo.
    * Make a copy of **.env.example** file to **.env**.
    * Install Docker and Docker Compose. [Find Instructions Here](https://docs.docker.com/install/).
    * Execute `docker-compose up -d --build` in terminal from the repo directory.
    * If you wanna see what happend with your scripts type `docker logs -f mariadb_seed`
    * For quick modification you could run `docker-compose up -d --build && docker logs -f mariadb_seed`
    * You will be able to access the database from http://localhost:3306
    * *If having any issue* then make sure 3306 port is not occupied else provide a different port in **.env** file.

### Find this project useful ? :heart:
* Support it by clicking the :star: button on the upper right of this page. :v:

### License
```
   Copyright (C) 2020 MINDORKS NEXTGEN PRIVATE LIMITED

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
     
 
