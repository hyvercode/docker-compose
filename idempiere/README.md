## Default Accounts

1. [x] System Management : 
`    user: System
     pass: System`
2. [x] System Management or any role/company:
`    user: System
    pass: System`
3. [x] Sample Client Administration:
`    user: GardenAdmin
    pass: GardenAdmin`
4. [x] Sample Client User
`     user: GardenUser
      pass: GardenUser`

## Default Ports
    1. 8080	    Default HTTP port for iDempiere
    2. 8443	    Default HTTPS port for iDempiere
    3. 12612    Default OSGI port for telnet connection
    4. 4554	    Default remote debug port

## Volumes

    Docker stack:
    volumes:
    - idempiere_data:/var/lib/postgresql/data

## iDempiere Plugins

    volumes:
        - idempiere_config:/opt/idempiere/configuration
        - idempiere_plugins:/opt/idempiere/plugins

## iDempiere Logs
    volumes:
        - idempiere_log:/opt/idempiere/log