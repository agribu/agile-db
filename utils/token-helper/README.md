* Open Firefox
* Open Web developer -> network analysis
* Open http://localhost:8000 and follow the login proceedure
* After login, go to the first entry in the network analysis tool
* Right-Click on '302 POST agile-local' --> Copy --> Copy as CURL address
* Extract the COOKIE Attribute and add to token.sh file
* You can now request new valid tokens by running the shell file
