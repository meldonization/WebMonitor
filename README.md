docker build . -t webmonitor:latest

docker exec -it webmonitor bash

docker run -it -p 6060:6060 test:latest /bin/bash

docker run -d --name webmonitor -v ./db:/app/db -p 6060:6060 -e PORT=6060 -e USERNAME=admin -e PASSWORD=admin webmonitor:latest


https://logicjake.github.io/WebMonitor/#/how?id=正则表达式


https://github.com/LogicJake/WebMonitor
https://github.com/whyour/qinglong
