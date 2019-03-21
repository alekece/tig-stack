# TIG stack (*T*elegraf/*I*nfluxDB/*G*rafana)

## How to use it?

    $ git clone https://github.com/alekece/tig-stack.git
    $ cd tig-stack
    $ docker-compose -f docker-compose.yml up -d


## Additional Info
* By default Grafana will have all available plugins installed.   
* To access grafana go to: `http://localhost:3000`   

## Environment
### Grafana  
`GF_SECURITY_ADMIN_USER` - Admin Username. Default: `admin`  
`GF_SECURITY_ADMIN_PASSWORD`- Admin User Password. Default:`admin`  
`GF_SECURITY_SECRET_KEY` - Secret key. Default: `grafana`  
`GF_USERS_ALLOW_SIGN_UP` - Allow singup to Grafana. Default: `"true"`  
`GF_USERS_ALLOW_ORG_CREATE` - Allow user create new Orgs. Default: `"true"`  
`GF_AUTH_ANONYMOUS_ENABLED` - Anonymus autthorization enabled. Default: `"true"`  
`GF_AUTH_ANONYMOUS_ORG_NAME` - Anonymus defaul Org Name. Default: `grafana`   
`GF_DASHBOARDS_JSON_ENABLED` - Dashboards as JSON enabled. Default: `"true"`   
`GF_DASHBOARDS_JSON_PATH` - Path where JSON Dashboards are stored. Default: `/opt/grafana`   
`GRAFANA_PLUGINS_ENABLED` - Install all available Grafana Plugins. Default: `true`

### InfluxDB  
`INFLUX_DATABASE` - InfluxDB Database Name. Default:  `"telegraf"`   
`INFLUX_ADMIN_USER` - InfluxDB Admin Username. Default: `"grafana"`  
`INFLUX_ADMIN_PASS` - InfluxDB Admin Password. Default: `"grafana"`    

### Telegraf  
`HOST_NAME` - Telegraf Default Hostane. Default: `"telegraf"`  
`INFLUXDB_HOST` - IndluxDB Database Host. Default: `"influxdb"`  
`INFLUXDB_PORT` - InfluxDB Default Port. Default: `"8086"`  
`DATABASE` - InfluxDB Database where telegraf stores data. Default: `"telegraf"`  

## Ports
Grafana:   
    - `3000` - in Docker   
    - `3001` - on Host   
InfluxDB:   
    - `8083`   
    - `8086`   

## License
Copyright © 2016-2018 Mateusz Trojak. See LICENSE for details.