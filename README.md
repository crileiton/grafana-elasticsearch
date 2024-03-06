# grafana-elasticsearch

 docker compose up -d

 <http://localhost:3000/>

 user: admin

 password: admin

 python3 script.py > results.json

 curl -X POST "<http://localhost:9200/index_cleiton/type_jmeter/_bulk>" -H 'Content-Type: application/json' --data-binary @results.json > /dev/null
 curl -X POST "<http://localhost:9200/index_cleiton/type_jmeter/_bulk>" -H 'Content-Type: application/json' --data-binary @results.json | jq

### Datasource elasticsearch

 <http://elasticsearch:9200>

 curl -X GET "<http://localhost:9200/index_cleiton/type_jmeter/_search?q=responseTime:118>"
