# TIG stack (*T*elegraf/*I*nfluxDB/*G*rafana)

## How to use it?

    $ git clone https://github.com/alekece/tig-stack.git
    $ cd tig-stack
    $ docker-compose up -d 

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
    - `3000`  
InfluxDB:   
    - `8083`   
    - `8086`   

## License
Copyright © 2019 ALexis Le Provost. See LICENSE for details.