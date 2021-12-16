# ip-details
This is a program that shows all the details of the given IP address. Build with **Python** and [ipinfo.io API](https://ipinfo.io/developers)

## Usage
To use this program, run the **main** Batch file, entering an **IPv4** address as argument.
```
$ ip 1.1.1.1
```

You can also add the `--save` or `-s` flag, to save the output to a file. The file will be named `details.log`, and will be stored inside the `saves` directory of the program (`saves/details.log`).
```
$ ip 1.1.1.1 --save
```
Or, if prefered:
```
$ ip 1.1.1.1 -s
```

### Example
```
$ ip 1.1.1.1

IP : 1.1.1.1
CITY : Miami
REGION : Florida
COUNTRY : US
LOC : 25.7867,-80.1800
ORG : AS13335 Cloudflare, Inc.
POSTAL : 33132
TIMEZONE : America/New_York
MAP : https://maps.google.com/maps/search/25.7867,-80.1800
```
And with the save option:
```
$ ip 1.1.1.1 --save

IP : 1.1.1.1
CITY : Miami
REGION : Florida
COUNTRY : US
LOC : 25.7867,-80.1800
ORG : AS13335 Cloudflare, Inc.
POSTAL : 33132
TIMEZONE : America/New_York
MAP : https://maps.google.com/maps/search/25.7867,-80.1800

Data saved to saves/details.log
```
`details.log` file:

![image](https://user-images.githubusercontent.com/61181201/146408576-b9319a15-b181-4766-b3a2-95c4aba00365.png)

## Requirements
[**Python**](https://www.python.org/) programming language

[**Requests**](https://pypi.org/project/requests/) python library